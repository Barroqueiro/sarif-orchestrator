import toml
import json
import shlex
import queue
import logging
import argparse
import threading
import subprocess
from enum import Enum

# States simulation of an enumerate to keep things cleaner (Using enums)

class states(str, Enum):
    WAITTING = "WAITTING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"

# Constants
REPORT_DIR = "Reporting"        # Directory that will store the reports generated
LOGS_DIR = "Logs"       # Directory that wills store the logs created (By this orchestrator and each tool)
OUTPUT_DIR_DOCKER = "/output"       # Default directory that is used to share output information (From docker's prespective)
INPUT_DIR_DOCKER = "/input"         # Default directory that is used to share input information (From docker's prespective)

# Docker commands to format
docker_cmd = "docker run --name {name} -v {output_volume}:{output_volume_docker}: \
-v {input_volume}:{input_volume_docker} \
-v /var/run/docker.sock:/var/run/docker.sock \
{image}:{tag} {option}"         # Command used to run a tool
docker_rm = "docker rm -f {containers}"         # Remove a list of containers
docker_image_rm = "docker image rm -f {images}"         # Remove a list of images

# Configurable globals
output_dir = ""         # Directory to where to output results and logs
output_dir_host = ""    # Output directory on the host to share with docker
input_dir = ""          # Input directory on the host to share with docker
config_file = ""        # Config file for this run of the orchestrator

# Globals needed for executions
logger = None       # Logger object
to_clean = []        # List of tools (Tuple with name, image and tag) to clean at the end of execution
threads = []        # Thread list with a thread per tool to be executed
queues = {}         # Queues for each tool (tool:queue) to (un)block execution
runs = {}       # Information on the different tools and their initial configuration

# Semaphore to keep access to shared resources controlled
semaphore = queue.Queue()
semaphore.put(1)

# Printing and Logging functions

def log_action(action,placeholder="-"):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    logger.info(f"[{placeholder:3s}] {action}")

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

# Smaller function to keep the global accesses clean

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

def add_to_clean(name, image, tag):
    """
    Adds a tuple to be cleaned containing the name of the container ("trivy_image"), the image name and the tag
    """
    globals()["to_clean"].append((name,image,tag))

def update_state(tool, state):
    """
    Updates the state of a tool
    """
    globals()["runs"][tool]["state"] = state


def release_tool(tool):
    """
    Adds something to the tool's queue making it go on with execution
    """
    globals()["queues"][tool].put(1)

def start_tasks():
    """
    Start all threads queued
    """
    for t in globals()["threads"]:
        t.start()

def wait_for_taks():
    """
    Wait for all threads to finish execution
    """
    for t in globals()["threads"]:
        t.join()

def create_tasks():
    """
    For each tool, create a thread for a future run and create queues for blocking threads that shall wait on others
    """
    for tool,args in globals()["runs"].items():
        
        q = queue.Queue()
        t = threading.Thread(target=run_tool_thread, args=(tool,args,q,))

        # If the tool has no dependencies run it imediatly
        if not args["depends_on"]:
            q.put(1)

        globals()["threads"].append(t)
        globals()["queues"][tool] = q

# Setup and Cleaning functions

def setup(args):
    """
    Creates the reporting and logs directories if they don't exist already, setups up the logger and configures the global variables that come from configuration
    """
    global output_dir, output_dir_host, input_dir, config_file, logger
    output_dir = args["output_dir"]
    output_dir_host = args["output_dir_host"]
    input_dir= args["input_dir"]
    config_file = args["config"]

    mkdir_output_cmd = f'mkdir {output_dir}/{REPORT_DIR}'
    mkdir_logs_cmd = f'mkdir {output_dir}/{LOGS_DIR}'

    exit_code_mkdir_output = subprocess.run(shlex.split(mkdir_output_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    exit_code_mkdir_logs = subprocess.run(shlex.split(mkdir_logs_cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    
    logging.basicConfig(filename=f'{output_dir}/{LOGS_DIR}/app.log', filemode='w', format='[%(name)-8s]  [%(levelname)-8s]  %(message)s', level=logging.DEBUG)
    globals()["logger"] = logging.getLogger()

    log_subprocess(mkdir_output_cmd,exit_code_mkdir_output)
    log_subprocess(mkdir_logs_cmd,exit_code_mkdir_logs)

def finish(keep_images):
    """
    Function to remove the docker containers, the argument specifies if the function should keep the images downloaded or purge them from docker as well
    """
    ran = globals()["to_clean"]

    tools = [r[0] for r in ran]
    images = [r[1] + ":" + r[2] for r in ran]
    rm = docker_rm.format(containers=" ".join(tools))
    exit_docker_rm = subprocess.run(shlex.split(rm), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    log_subprocess(rm, exit_docker_rm)

    if not keep_images:

        image_rm = docker_image_rm.format(images=" ".join(images))
        exit_docker_rm = subprocess.run(shlex.split(image_rm), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
        log_subprocess(image_rm, exit_docker_rm)

# Parsing functions

def set_runs(config):
    res = {}
    for run in config["runs"]:

        if "custom_args" not in run:
            run["custom_args"] = ""

        if "depends_on" not in run:
            run["depends_on"] = []

        run["state"] = states.WAITTING

        res[run["tool"]] = run
        del run["tool"]

    globals()["runs"] = res

# Tool running functions

def run_possible():
    """
    Function that evaluates all the non root tools and whose state is WAITTING and checks for the FINISH state within the dependencies it has, it all dependencies are FINISHED,
    lauch the tool
    """
    acquire()

    for tool,args in globals()["runs"].items():
        # Check if the tool should actually be started
        if args["depends_on"] != [] and args["state"] == states.WAITTING:

            # Make sure all states of the dependencies are FINISHED
            if all([runs[d]["state"] == states.FINISHED for d in args["depends_on"]]):
                
                update_state(tool, states.RUNNING)
                release_tool(tool)
                
    release()

def run_tool_thread(tool,args,q):
    """
    Function each thread will execute, this function will remain blocked until the tools that this tool depends on are FINISHED 
    """
    # Blocking call
    q.get()
    log_action(tool, "Running Tool")

    # Run the docker and wait for it's completion
    run_tool(tool,args["option"],args["args"],args["custom_args"])

    # Update the state to finished when the run_tool function returns
    update_state(tool, states.FINISHED)

    # Run the tools that can start running
    run_possible()

def run_tool(tool,option=None,args=[],custom_args=""):
    """
    Runs a certain tool using the configuration provided within the tool's file, volumes are configured using the default options or the ones within the config, a process for
    each docker container is used to provide paralel analysis boosting effiency, processes are registered globally
    """

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
    call = docker_cmd.format(output_volume=globals()["output_dir_host"],input_volume=globals()["input_dir"],\
                        output_volume_docker=output_volume_docker,input_volume_docker=input_volume_docker,\
                        image=image,tag=tag,option=option_cmd, name=name)

    # Create log file and run the process
    f = open(f'{globals()["output_dir"]}/{LOGS_DIR}/{tool}.log',"w")
    p = subprocess.run(shlex.split(call), stdout=f, stderr=f).returncode
    log_subprocess(call,p)

    add_to_clean(name,image,tag)

    return p

# Main

def main():
    parser = argparse.ArgumentParser(description="Orchestrating sarif tools")
    parser.add_argument('--input-dir', type=str, required=True,
                        help='Directory to be shared with docker for input')
    parser.add_argument('--output-dir', type=str, required=True,
                        help='Directory to be shared with docker for output')
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
    print_config(config)

    setup(command_args)
    set_runs(config)

    create_tasks()       # Create all threads (One for each tool)
    start_tasks()        # Start all threads
    wait_for_taks()         # Wait for all threads to complete
    finish(command_args["keep_images"])         # Remove containers and images if asked for

if __name__ == "__main__":
    main()