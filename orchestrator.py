"""
Docker conatiner orchestrator for SARIF reporting tools
"""

import json
import shlex
import queue
import logging
import argparse
import threading
import subprocess
from enum import Enum

import toml

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

# Semaphore function

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

def create_tool(tool, input_dir_host, output_dir_host, to_clean, tool_values):
    """
    create_tool function creates the container for a certain tool using the configuration provided within the tool's file, volumes are configured
    using the default options or the ones within the config, the name, image and tag are appended to a shared list for future clean up

    :param tool: Tool name
    :param input_dir_host: Directory within the host shared with docker (to mount) for input
    :param output_dir_host: Directory within the host shared with docker (to mount) for output
    :param to_clean: List to append information for clean up (name, image, tag)
    :param arguments: Dictionary with tool specific arguments
    """

    docker_cmd = "docker create --name {name} -v {output_volume}:{output_volume_docker}: \
                    -v {input_volume}:{input_volume_docker} \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    {image}:{tag} {option}" 

    option = tool_values["option"]
    args = tool_values["args"]
    custom_args = tool_values["custom_args"]

    # Load tool config
    config = toml.loads(open(f"tools/{tool}.toml").read())

    # Set a default option if none was specified
    if not option:
        option = config["default_option"]

    # If no volumes for input or output are configured setup the defaults
    if config["output_volume_docker"] == "":
        output_volume_docker = OUTPUT_DIR_DOCKER
    else:
        output_volume_docker = config["output_volume_docker"]

    if config["input_volume_docker"] == "":
        input_volume_docker = INPUT_DIR_DOCKER
    else:
        input_volume_docker = config["input_volume_docker"]

    # Output file
    output = f"{output_volume_docker}/{REPORT_DIR}/{tool}_{option}.sarif"

    # Format the options
    option_cmd = config["options"][option].format(*args,output_place=output,custom_args=custom_args)

    # Format full docker command
    name = tool + "_" + option
    image = config["image"]
    tag = config["tag"]
    call = docker_cmd.format(output_volume=output_dir_host, input_volume=input_dir_host,\
                        output_volume_docker=output_volume_docker, input_volume_docker=input_volume_docker,\
                        image=image, tag=tag, option=option_cmd, name=name)

    # Create log file and run the process
    p = subprocess.run(shlex.split(call), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    log_subprocess(call,p)

    to_clean.append((name,image,tag))

    return name

def run_tool_thread(tool, input_dir_host, output_dir_host, runs, to_clean):
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
    tool_values = {a:runs[tool][a] for a in runs[tool] if a in ["option", "args", "custom_args"]}

    # Create the docker container
    container = create_tool(tool, input_dir_host, output_dir_host, to_clean, tool_values)

    # Blocking call
    runs[tool]["queue"].get()
    runs[tool]["state"] = states.RUNNING

    # Run the container
    start_container(tool, container)

    # Update the state to finished when the start_container function returns
    runs[tool]["state"] = states.FINISHED

    # Run the tools that can start running
    run_possible(runs)

def run_tasks(runs, input_dir_host, output_dir_host):
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
        t = threading.Thread(target=run_tool_thread, args=(tool, input_dir_host, output_dir_host, runs, to_clean))

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
    parser.add_argument('--input-dir-host', type=str, required=True,
                        help='Directory to be shared with docker for input')
    parser.add_argument('--output-dir-host', type=str, required=True,
                        help='Directory to be shared with the docker runs for output')
    parser.add_argument('--config', type=str, required=True,
                        help='Current path')
    parser.add_argument('--keep-images', action='store_true',
                        help='Output style')
    args = parser.parse_args()
    command_args = vars(args)

    config = toml.loads(open(command_args["config"]).read())
    print("Full config: ")

    setup()
    runs = get_runs(config)
    print_config(runs)

    to_clean = run_tasks(runs, command_args["input_dir_host"], command_args["output_dir_host"])

    finish(to_clean, command_args["keep_images"])


if __name__ == "__main__":
    main()
