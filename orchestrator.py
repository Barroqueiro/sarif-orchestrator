"""
Docker conatiner orchestrator for SARIF reporting tools
"""
import os
import toml
import json
import shlex
import queue
import logging
import argparse
import threading
import subprocess
from enum import Enum
from jinja2 import Environment, FileSystemLoader

# Example of runs object for consideration

# "<tool_name>": {
#         "option": "",
#         "args": [
#             ""
#         ],
#         "custom_args": "",
#         "depends_on": [],
#         "state": "WAITTING/RUNNING/FINISHED",
#         "queue": <Queue>
#     }

# States simulation of an enumerate to keep things cleaner (Using enums)

class states(str, Enum):
    """
    Enum class for a tool state
    """
    WAITTING = "WAITTING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"


# Constants
REPORT_DIR = "Reporting"                                    # Directory that will store the reports generated
LOGS_DIR = "Logs"                                           # Directory that wills store the logs created (By this orchestrator and each tool)
OUTPUT_DIR_DOCKER = "/output"                               # Default directory that is used to share output information (From docker's prespective)
INPUT_DIR_DOCKER = "/input"                                 # Default directory that is used to share input information (From docker's prespective)
CONFIG_DIR_DOCKER = "/config"                               # Default directory that is used to share configuration information (From docker's prespective)
LOG_FILE = f'{OUTPUT_DIR_DOCKER}/{LOGS_DIR}/app.log'        # Log file

# Logger object
logger = None

# Semaphore to keep access to shared resources controlled
semaphore = queue.Queue()
semaphore.put(1)

# Printing and Logging functions
def log_subprocess(cmd,exit_code):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    logger.info(f"[{exit_code:3d}] {cmd}")

def print_config(config):
    """
    Printing the global configuration in a user friendly way using json indent
    """
    print(json.dumps(config,indent=4))

# Semaphore access

def acquire():
    """
    Acquire the semaphore for shared resource usage
    """
    globals()["semaphore"].get()

def release():
    """
    Release the semaphore for shared resource usage
    """
    globals()["semaphore"].put(1)

# Reporting functions

def populate_level(results, rules):
    """
    populate the level atribute of sarif results if not included
    """
    for r in results:
        if "level" not in r:
            if "defaultConfiguration" in rules[r["ruleId"]]:
                if "level" in rules[r["ruleId"]]["defaultConfiguration"]:
                    r["level"] = rules[r["ruleId"]]["defaultConfiguration"]["level"]
                else:
                    r["level"] = "warning"
            else:
                r["level"] = "warning"

def produce_sarif_reports(input_dir, output_dir):
    for subdir, dirs, files in os.walk(input_dir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in [".sarif", ".json.sarif"]:
                produce_single_sarif(os.path.join(subdir, file),output_dir)

def produce_single_sarif(file, output_dir):
    basename = os.path.basename(file)

    with open(file,"r") as f:
        data = json.loads(f.read())

    # Get information on the tool and it's rules 
    info_rules_tools = data["runs"][0]["tool"]["driver"]

    # Produce dictionary with rules
    if "rules" in info_rules_tools:
        rules_info = {r["id"]: r for r in info_rules_tools["rules"]}
    else:
        rules_info = {}

    # Produce dictionary for tool information without the rules
    tool_info = {key: value for key, value in info_rules_tools.items() if key != "rules"}

    # Populate the level of results to then order it
    results = data["runs"][0]["results"]
    populate_level(results, rules_info)

    results_info = [r for r in sorted(results, key=lambda x: x["level"])]

    # Load template and produce final report
    env = Environment(loader=FileSystemLoader("templates"), autoescape=True, extensions=['jinja2.ext.do'])
    template = env.get_template('Sarif_to_Markdown.jinja2')
    output_from_parsed_template = template.render(tool=tool_info,rules=rules_info,results=results_info)
    with open(output_dir + "/" + basename.replace(".sarif",".md"),"w") as f:
        f.write(output_from_parsed_template)


# Setup and Cleaning functions

def setup():
    """
    setup function creates the reporting and logs directories if they don't exist already, sets up up the logger
    """

    mkdir_output_cmd = f'mkdir {OUTPUT_DIR_DOCKER}/{REPORT_DIR}'
    mkdir_logs_cmd = f'mkdir {OUTPUT_DIR_DOCKER}/{LOGS_DIR}'

    exit_code_mkdir_output = subprocess.run(shlex.split(mkdir_output_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    exit_code_mkdir_logs = subprocess.run(shlex.split(mkdir_logs_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode

    logging.basicConfig(filename=LOG_FILE, filemode='w', format='[%(name)-8s]  [%(levelname)-8s]  %(message)s', level=logging.DEBUG)
    globals()["logger"] = logging.getLogger()

    log_subprocess(mkdir_output_cmd, exit_code_mkdir_output)
    log_subprocess(mkdir_logs_cmd, exit_code_mkdir_logs)

def finish(to_clean, keep_images):
    """
    finish function removes the docker containers from the list and images if asked to

    :param to_clean: List of tuples containing the name, image and tag of a certain tool configuration p.e (trivy_image, aquasec/trivy, 0.34.0)
    :param keep_images: If false removes the images from the tools
    """

    docker_rm = "docker rm -f {containers}"
    docker_image_rm = "docker image rm -f {images}"

    tools = [r[0] for r in to_clean]
    images = [r[1] + ":" + r[2] for r in to_clean]

    container_rm = docker_rm.format(containers=" ".join(tools))
    exit_docker_rm = subprocess.run(shlex.split(container_rm), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    log_subprocess(container_rm, exit_docker_rm)

    if not keep_images:

        image_rm = docker_image_rm.format(images=" ".join(images))
        exit_docker_rm = subprocess.run(shlex.split(image_rm), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
        log_subprocess(image_rm, exit_docker_rm)

# Parsing functions

def get_runs(config):
    """
    get_runs function takes the list of tools and arguments from the run.toml file for this iteration and sets the defaults for custom arguments,
    dependencies and option, sets the initial state as WAITTING for all tools and returns a dictionary with the keys as the name of tools and the
    arguments as values (option, args, custom_Args, depends_on and state)

    :param config: List of tools to run taken directly from the toml configuration file
    """

    res = {}
    for run in config["runs"]:
        tool = run["tool"]

        res[tool] = {r:run[r] for r in run if r != "tool"}
        res[tool].setdefault("option", None)
        res[tool].setdefault("platform", None)
        res[tool].setdefault("custom_args","")
        res[tool].setdefault("depends_on",[])
        res[tool]["state"] = states.WAITTING

    return res

# Tool running functions

def start_container(tool, container):
    """
    start_container function starts a docker container

    :param container: Container name
    :param tool: Tool being ran
    """
    docker_start = "docker start {name} -a"     # -a needed to attach the output and not run in deamon mode

    call = docker_start.format(name=container)
    f = open(f'{OUTPUT_DIR_DOCKER}/{LOGS_DIR}/{tool}.log',"w")
    p = subprocess.run(shlex.split(call), stdout=f, stderr=f).returncode
    log_subprocess(call,p)
    f.close()

def run_possible(runs):
    """
    run_possible function evaluates all the non root tools and whose state is WAITTING and checks for the FINISH state within the dependencies it has,
    if all dependencies are FINISHED, lauch the tool
    """
    acquire()

    for tool, args in runs.items():
        # Check if the tool should actually be started
        if args["depends_on"] != [] and args["state"] == states.WAITTING:
            
            # Make sure all states of the dependencies are FINISHED
            if all([runs[d]["state"] == states.FINISHED for d in args["depends_on"]]):

                runs[tool]["queue"].put(1)      # Unblock tool

    release()

def create_tool(tool, input_dir_host, output_dir_host, config_dir_host , to_clean, tool_values):
    """
    create_tool function creates the container for a certain tool using the configuration provided within the tool's file, volumes are configured
    using the default options or the ones within the config, the name, image and tag are appended to a shared list for future clean up

    :param tool: Tool name
    :param input_dir_host: Directory within the host shared with docker (to mount) for input
    :param output_dir_host: Directory within the host shared with docker (to mount) for output
    :param to_clean: List to append information for clean up (name, image, tag)
    :param arguments: Dictionary with tool specific arguments
    """

    docker_cmd = "docker create --name {name} {platform} -v {output_volume}:{output_volume_docker}:rw \
                    -v {input_volume}:{input_volume_docker}:ro \
                    -v {config_volume}:{config_volume_docker}:ro  \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    {image}:{tag} {option}" 

    option = tool_values["option"]
    args = tool_values["args"]
    custom_args = tool_values["custom_args"]
    platform = f"--platform={tool_values['platform']}" if tool_values["platform"] else ""

    # Load tool config
    config = toml.loads(open(f"tools/{tool}.toml").read())

    # Set a default option if none was specified
    if not option:
        option = config["default_option"]

    # If no volumes for input or output are configured setup the defaults
    output_volume_docker = OUTPUT_DIR_DOCKER if config["output_volume_docker"] == "" else config["output_volume_docker"] 
    input_volume_docker = INPUT_DIR_DOCKER if config["input_volume_docker"] == "" else config["input_volume_docker"]

    # Output file
    output = f"{output_volume_docker}/{REPORT_DIR}/{tool}_{option}.sarif"

    # Format the options
    option_cmd = config["options"][option].format(*args,output_place=output,custom_args=custom_args)

    # Format full docker command
    name = tool + "_" + option
    image = config["image"]
    tag = config["tag"]
    call = docker_cmd.format(output_volume=output_dir_host, input_volume=input_dir_host, config_volume=config_dir_host,\
                        output_volume_docker=output_volume_docker, input_volume_docker=input_volume_docker, config_volume_docker=CONFIG_DIR_DOCKER,  \
                        image=image, tag=tag, option=option_cmd, name=name, platform=platform)

    # Create log file and run the process
    p = subprocess.run(shlex.split(call), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    log_subprocess(call,p)

    to_clean.append((name,image,tag))

    return name

def run_tool_thread(tool, input_dir_host, output_dir_host, config_dir_host, runs, to_clean):
    """
    run_tool_thread will be executed by each thread, this function will create the docker container for a future run of a certain tool,
    it will then remain blocked until the tools that this tool depends on are FINISHED (They will unblock this tools thread), when FINISHED
    it shall update it's state and run other possible tools that are WAITTING

    :param tool: Tool name
    :param input_dir_host: Directory within the host shared with docker (to mount) for input
    :param output_dir_host: Directory within the host shared with docker (to mount) for output
    :param args: Arguments specific to this tool
    :param runs: Runs object with information on all tools
    :param to_clean: List to append information for clean up (name, image, tag)
    """
    # Get the arguments for a tool run
    tool_values = {a:runs[tool][a] for a in runs[tool] if a in ["option", "args", "custom_args","platform"]}

    # Create the docker container
    container = create_tool(tool, input_dir_host, output_dir_host, config_dir_host, to_clean, tool_values)

    # Blocking call
    runs[tool]["queue"].get()
    runs[tool]["state"] = states.RUNNING

    # Run the container
    start_container(tool, container)

    # Update the state to finished when the start_container function returns
    runs[tool]["state"] = states.FINISHED

    # Run the tools that can start running
    run_possible(runs)

def run_tasks(runs, input_dir_host, output_dir_host, config_dir_host):
    """
    run_tasks function creates a thread for all tools with a corresponding queue, appends this information to the runs object to be shared.
    It starts and waits for the completion of all threads.
    Returns the to_clean list which is passes to all threads to indicate the name, image and tag of the containers/images to clean

    :param runs: Runs object with tool information needed to run each tool
    :param input_dir_host: Directory within the host shared with docker (to mount) for input
    :param output_dir_host: Directory within the host shared with docker (to mount) for output
    """
    to_clean = []
    threads = []

    for tool, args in runs.items():

        q = queue.Queue()
        t = threading.Thread(target=run_tool_thread, args=(tool, input_dir_host, output_dir_host, config_dir_host, runs, to_clean))

        # If the tool has no dependencies run it imediatly
        if not args["depends_on"]:
            q.put(1)

        threads.append(t)
        runs[tool]["queue"] = q

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return to_clean

# Main
def main():
    parser = argparse.ArgumentParser(description="Orchestrating sarif tools")
    subparsers = parser.add_subparsers(title="subcommands", help="Different commands", dest="command")
    orchestrator_parser = subparsers.add_parser("orchestrator", help="Orchestrate tools to produce sarif reporting")
    orchestrator_parser.add_argument('--input-dir-host', type=str, required=True,
                        help='Directory to be shared with docker for input')
    orchestrator_parser.add_argument('--output-dir-host', type=str, required=True,
                        help='Directory to be shared with the docker runs for output')
    orchestrator_parser.add_argument('--config-dir-host', type=str, required=True,
                        help='Directory to be shared with the docker runs for configuration')
    orchestrator_parser.add_argument('--config', type=str, required=True,
                        help='Current path')
    orchestrator_parser.add_argument('--keep-images', action='store_true',
                        help='Keep images after finishing')

    reporting_parser = subparsers.add_parser("report", help="Produce Markdown reports from sarif files")
    reporting_parser.add_argument('--input-dir', type=str, required=True,
                        help='Directory with the sarif files')
    reporting_parser.add_argument('--output-dir', type=str, required=True,
                        help='Directory to output the results')
    args = parser.parse_args()
    command_args = vars(args)

    command = command_args["command"]

    if command == "orchestrator":

        config = toml.loads(open(command_args["config"]).read())
        print("Full config: ")

        setup()
        runs = get_runs(config)
        print_config(runs)

        to_clean = run_tasks(runs, command_args["input_dir_host"], command_args["output_dir_host"], command_args["config_dir_host"])

        finish(to_clean, command_args["keep_images"])
    
    if command == "report":

        produce_sarif_reports(command_args["input_dir"],command_args["output_dir"])


if __name__ == "__main__":
    main()
