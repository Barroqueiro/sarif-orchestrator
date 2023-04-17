import os
import toml
import json
import shlex
import queue
import hashlib
import logging
import threading
import subprocess
from enum import Enum
from datetime import datetime

from src.constants import *


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

# Logger object
logger = None

# Semaphore to keep access to shared resources controlled
semaphore = queue.Queue()
semaphore.put(1)

# States simulation of an enumerate to keep things cleaner (Using enums)

class states(str, Enum):
    """
    Enum class for a tool state
    """
    WAITTING = "WAITTING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"

# Printing and Logging functions
def log_subprocess(cmd,exit_code):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"[{time}] [{exit_code:3d}] {cmd}")

def print_config(config):
    """
    Printing the global configuration in a user friendly way using json indent
    """
    print(json.dumps(config, indent=4))

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

def setup():
    """
    setup function creates the reporting and logs directories if they don't exist already, sets up up the logger
    """

    mkdir_output_cmd = f'mkdir -m777 {OUTPUT_DIR_DOCKER}/{REPORT_DIR}'
    mkdir_logs_cmd = f'mkdir -m777 {OUTPUT_DIR_DOCKER}/{LOGS_DIR}'

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
        res[tool].setdefault("sha256", None)
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

    docker_cmd = "docker create {network} --name {name} {platform} -v {output_volume}:{output_volume_docker}:rw \
                    -v {input_volume}:{input_volume_docker}:rw \
                    -v {config_volume}:{config_volume_docker}:ro  \
                    {socket} \
                    {designation} {option}" 

    option = tool_values["option"]
    args = tool_values["args"]
    custom_args = tool_values["custom_args"]
    platform = f"--platform={tool_values['platform']}" if tool_values["platform"] else ""
    digest = f"@sha256:{tool_values['sha256']}" if tool_values["sha256"] else ""


    # Load tool config
    config = toml.loads(open(f"tools/{tool}.toml").read())

    network = "--network host" if config["share_network"] else ""
    socket = "-v /var/run/docker.sock:/var/run/docker.sock" if config["share_socket"] else ""

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

    if digest:
        designation = "{image}{digest}".format(image=image, digest=digest)
    else:
        designation = "{image}:{tag}".format(image=image, tag=tag)

    call = docker_cmd.format(output_volume=output_dir_host, input_volume=input_dir_host, config_volume=config_dir_host,\
                        output_volume_docker=output_volume_docker, input_volume_docker=input_volume_docker, config_volume_docker=CONFIG_DIR_DOCKER,  \
                        designation=designation, option=option_cmd, name=name, platform=platform, network=network, socket=socket)

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
    tool_values = {a:runs[tool][a] for a in runs[tool] if a in ["option", "args", "custom_args","platform","sha256"]}

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

# Vulnerability ignoring functions

def hash_vuln(vuln):
    """
    Produce a SHA-256 hash of a result object
    """
    return hashlib.sha256(str(vuln).encode("utf-8")).hexdigest()

def update_single_sarif(filename):
    """
    Update a SARIF file with the hashes for each vulnerability found, if an hash or id is found within the ignoring files they are discarded from the final results
    """

    # Get items to ignore
    if os.path.isfile(CONFIG_DIR_DOCKER + "/" + HASH_IGNORE_FILE):
        hashes = open(CONFIG_DIR_DOCKER + "/" + HASH_IGNORE_FILE).read().split("\n")
        hashes = [h for h in hashes if h != "" and h[0] != "#" ]
    else:
        hashes = []

    if os.path.isfile(CONFIG_DIR_DOCKER + "/" + ID_IGNORE_FILE):
        ids = open(CONFIG_DIR_DOCKER + "/" + ID_IGNORE_FILE).read().split("\n")
        ids = [i for i in ids if i != "" and i[0] != "#" ]
    else:
        ids = []

    # Load information
    with open(filename,"r") as f:
        data = json.loads(f.read())
    runs = data["runs"]

    # Remove or update the vulnerability entries
    for r in runs:
        iterator = [x for x in r["results"]]
        results = r["results"]
        for res in iterator:

            # Remove ids
            if res["ruleId"] in ids:
                results.remove(res)
                continue

            # Get hash if it exists else hash the vulnerability
            if "properties" in res and "hash" in res["properties"]:
                hash = res["properties"]["hash"]
            else:
                hash = hash_vuln(res)
                if "properties" in res:
                    res["properties"]["hash"] = hash
                else:
                    res["properties"] = {"hash": hash}

            # Remove hashes
            if hash in hashes:
                results.remove(res)

    # Store the information back
    data["runs"] = runs

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def update_sarif_reports():
    """
    Walk through a directory and find all sarif files, update each with hashing information
    """
    for subdir, dirs, files in os.walk(OUTPUT_DIR_DOCKER + "/" +REPORT_DIR):
        for file in files:
            if ".sarif" in file:
                update_single_sarif(os.path.join(subdir, file))

