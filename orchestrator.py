import sys
import toml
import json
import queue
import logging
import argparse
import threading
import subprocess
from random import randint
from time import sleep

class states:
    WAITTING = "WAITTING"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"

REPORT_DIR = "Reporting"
LOGS_DIR = "Logs"
OUTPUT_DIR_DOCKER = "/output"
INPUT_DIR_DOCKER = "/input"
DOCKER_CMD = "docker run --name {name} -v {output_volume}:{output_volume_docker}: \
-v {input_volume}:{input_volume_docker} \
-v /var/run/docker.sock:/var/run/docker.sock \
{image}:{tag} {option}"
DOCKER_RM = "docker rm -f {containers}"
DOCKER_IMAGE_RM = "docker image rm -f {images}"

OUTPUT_DIR = ""
INPUT_DIR = ""
CONFIG_FILE = ""

logger = None

semaphore = queue.Queue()
semaphore.put(1)

to_clean = []
threads = []
queues = {}
runs = {}

# Printing and Logging functions

def logSubprocess(cmd,exit_code):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    logger.info(f"[{exit_code:3d}] {cmd}")

def make_deps_tree(deps,res=[],before=""):
    """
    Make a tree based on a dictionary, the res has to be a list as strings are not mutable in python so this gymic needs to be used
    """
    space =  '    '
    branch = '│   '
    tee =    '├───'
    last =   '└───'
    count = 0
    length = len(deps)
    for d in deps:
        if length == 1:
            res += [before+last+d+"\n"]
        elif count == 0:
            res += [before+tee+d+"\n"]
        elif count < length-1:
            res += [before+tee+d+"\n"]
        else:
            res += [before+last+d+"\n"]
        if count == length-1:
            make_deps_tree(deps[d],res, before+space)
        else:
            make_deps_tree(deps[d],res, before+branch)
        count+=1
    return ''.join(res)

def printConfig(config):
    """
    Printing the global configuration in a user friendly way
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

def addToClean(name, image, tag):
    acquire()
    globals()["to_clean"].append((name,image,tag))
    release()

def updateState(tool, state):
    acquire()
    globals()["runs"][tool]["state"] = state
    release()

def releaseTool(tool):
    globals()["queues"][tool].put(1)

def setInitialState():
    acquire()
    for items in globals()["runs"].values():
        items["state"] = "WAITTING"
    release()

def startTasks():
    acquire()
    for t in globals()["threads"]:
        t.start()
    release()

def waitForFullCompletion():
    acquire()
    for t in globals()["threads"]:
        t.join()
    release()

def createTasks():
    acquire()
    for tool,args in globals()["runs"].items():
        
        q = queue.Queue()
        t = threading.Thread(target=runToolThread, args=(tool,args,q,))

        if not args["depends_on"]:
            q.put(1)

        globals()["threads"].append(t)
        globals()["queues"][tool] = q

    release()

def finish(keep_images):
    """
    Function to remove the docker containers, the argument specifies if the function should keep the images downloaded or purge them from docker as well
    """
    ran = globals()["to_clean"]

    tools = [r[0] for r in ran]
    images = [r[1] + ":" + r[2] for r in ran]
    rm = DOCKER_RM.format(containers=" ".join(tools))
    exit_docker_rm = subprocess.run(rm, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    logSubprocess(rm, exit_docker_rm)

    if not keep_images:

        image_rm = DOCKER_IMAGE_RM.format(images=" ".join(images))
        exit_docker_rm = subprocess.run(image_rm, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
        logSubprocess(image_rm, exit_docker_rm)


def setup(args):
    """
    Creates the reporting and logs deps if they don't exist already, also setups up the logger
    """
    globals()["OUTPUT_DIR"] = args["output_dir"]
    globals()["INPUT_DIR"] = args["input_dir"]
    globals()["CONFIG_FILE"] = args["config"]
    logging.basicConfig(filename=f'{OUTPUT_DIR}/{LOGS_DIR}/app.log', filemode='w', format='[%(name)-8s]  [%(levelname)-8s]  %(message)s', level=logging.DEBUG)
    globals()["logger"] = logging.getLogger()

    mkdir_output_cmd = f"mkdir {OUTPUT_DIR}/{REPORT_DIR}"
    mkdir_logs_cmd = f"mkdir {OUTPUT_DIR}/{LOGS_DIR}"

    exit_code_mkdir_output = subprocess.run(mkdir_output_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    logSubprocess(mkdir_output_cmd,exit_code_mkdir_output)
    exit_code_mkdir_logs = subprocess.run(mkdir_logs_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    logSubprocess(mkdir_logs_cmd,exit_code_mkdir_logs)

def getDeps(tool,dependencies):
    """
    Get the dependecies of a root tool (A tool that has no dependents)
    """
    if tool not in dependencies.values():
        return {tool:{}}
    else:
        tmp = {}
        for x in dependencies:
            if dependencies[x] == tool:
                tmp.update(getDeps(x,dependencies))
        return {tool:tmp}

def getRuns(config):
    res = {}
    for run in config["runs"]:
        if "custom_args" not in run:
            run["custom_args"] = ""
        if "depends_on" not in run:
            run["depends_on"] = []
        res[run["tool"]] = run
        del run["tool"]
    return res


def getD(config):
    """
    Get the dictionary containing the tools used nesting the dependencies each have
    """
    depends = {}

    runs = config["runs"]

    for tool in runs:
        if "depends_on" in tool:
            depends[tool["tool"]] = tool["depends_on"]
        else:
            depends[tool["tool"]] = ""

    res = {}

    for tool in depends:
        if depends[tool] == "":
            res.update(getDeps(tool,depends))

    print(res)

    return res

def runPossible():
    """
    Function that evaluates all the non root tools and whose state is WAITTING and checks for the FINISH state within the dependencies it has, it all dependencies are FINISHED,
    lauch the tool
    """

    acquire()

    for tool,args in globals()["runs"].items():

        if args["depends_on"] != [] and args["state"] == "WAITTING":

            depends = args["depends_on"]
            can_run = all([runs[d]["state"] == "FINISHED" for d in depends])

            if can_run:
                
                print("Lauching ",tool)
                updateState(tool, states.RUNNING)
                releaseTool(tool)
                

    release()



def runToolThread(tool,args,q):
    """
    Function each thread will execute, this function will remain blocked until the tools that this tool depends on are FINISHED 
    """
    
    # Blocking call
    q.get()

    # Run the docker and wait for it's completion
    runTool(tool,args["option"],args["args"],args["custom_args"])

    # Update the state to finished when the runTool function returns
    updateState(tool, states.FINISHED)

    # Run the tools that can start running
    runPossible()



def runTool(tool,option=None,args=[],custom_args=""):
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
    call = DOCKER_CMD.format(output_volume=OUTPUT_DIR,input_volume=INPUT_DIR,\
                        output_volume_docker=output_volume_docker,input_volume_docker=input_volume_docker,\
                        image=image,tag=tag,option=option_cmd, name=name)

    # Create log file and run the process
    f = open(f'{OUTPUT_DIR}/{LOGS_DIR}/{tool}.log',"w")
    p = subprocess.run(call, shell=True, stdout=f, stderr=f).returncode
    logSubprocess(call,p)

    addToClean(name,image,tag)

    return p

def main():

    parser = argparse.ArgumentParser(description="Orchestrating sarif tools")
    parser.add_argument('--input-dir', type=str, required=True,
                        help='Directory to be shared with docker for input')
    parser.add_argument('--output-dir', type=str, required=True,
                        help='Directory to be shared with docker for output')
    parser.add_argument('--config', type=str, required=True,
                        help='Current path')
    parser.add_argument('--keep-images', action='store_true',
                        help='Output style')
    args = parser.parse_args()
    command_args = vars(args)

    config = toml.loads(open(command_args["config"]).read())
    print("Full config: ")
    printConfig(config)

    setup(command_args)

    globals()["runs"] = getRuns(config)
    setInitialState()

    createTasks()

    startTasks()

    waitForFullCompletion()

    finish(command_args["keep_images"])

if __name__ == "__main__":
    main()