import sys
import toml
import json
import logging
import argparse
import subprocess

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
res = ""

OUTPUT_DIR = ""
INPUT_DIR = ""
CONFIG_FILE = ""

logger = None

processes = []

def logSubprocess(cmd,exit_code):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    logger.info(f"[{exit_code:3d}] {cmd}")

def printDeps(deps,before=""):
    global res
    space =  '    '
    branch = '|   '
    tee =    '|---'
    last =   '\___'
    count = 0
    length = len(deps)
    for d in deps:
        if length == 1:
            res += before+last+str(d)+"\n"
        elif count == 0:
            res += before+tee+str(d)+"\n"
        elif count < length-1:
            res += before+tee+str(d)+"\n"
        else:
            res += before+last+str(d)+"\n"
        if count == length-1:
            printDeps(deps[d], before+space)
        else:
            printDeps(deps[d], before+branch)
        count+=1

def printConfig(config):
    """
    Printing the global configuration in a user friendly way
    """
    print(json.dumps(config,indent=4))

def finish(ran,keep_images):
    """
    Waits for all processes to end logs their return codes, closes all log files used for each process and removes all containers, if desired also delets the images of said containers
    """
    for call, p, f in globals()["processes"]:
        p.wait() 
        logSubprocess(call,p.returncode)
        f.close()

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
    if tool not in dependencies.values():
        return {tool:[]}
    else:
        return {tool:[getDeps(x,dependencies) for x in dependencies if dependencies[x] == tool]}

def getRuns(config):
    depends = {}

    runs = config["runs"]

    for tool in runs:
        if "depends_on" in tool:
            depends[tool["tool"]] = tool["depends_on"]
        else:
            depends[tool["tool"]] = ""

    print(depends)

    count = 0
    total = len(depends)
    res = {}

    for tool in depends:
        if depends[tool] == "":
            res.update(getDeps(tool,depends))

    print()
    #printDeps(res)

    # batches = [[]]
    # idx = 0

    # for i,tool in enumerate(depends):
    #     if depends[tool] == "":
    #         batches[0].append(tool)
    #         count += 1

    # while count < total:
    #     if count == total:
    #         break
    #     batches.append([])
    #     for i,tool in enumerate(depends):
    #         if depends[tool] in batches[idx]:
    #             batches[idx+1].append(tool)
    #             count += 1
    #     idx += 1

    return res

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
    call = DOCKER_CMD.format(output_volume=OUTPUT_DIR,input_volume=INPUT_DIR,\
                        output_volume_docker=output_volume_docker,input_volume_docker=input_volume_docker,\
                        image=config["image"],tag=config["tag"],option=option_cmd, name=name)

    # Create log file and run the process
    f = open(f'{OUTPUT_DIR}/{LOGS_DIR}/{tool}.log',"w")
    p = subprocess.Popen(call, shell=True, stdout=f, stderr=f)
    globals()["processes"].append((call, p, f))

    return (tool, config["image"], config["tag"])

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
    printConfig(config)

    setup(command_args)

    runs = getRuns(config)
    print(runs)
    exit()

    ran = []

    for r in runs:
        ran.append(runTool(*r))

    finish(ran,command_args["keep_images"])

if __name__ == "__main__":
    main()