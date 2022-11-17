import sys
import toml
import json
import logging
import subprocess

OUTPUT_DIR = "/Users/cruz/Desktop/Bolsa/sarif-orchestrator/output"
INPUT_DIR = "/Users/cruz/Desktop/Bolsa/sarif-orchestrator/input"
REPORT_DIR = "Reporting"
LOGS_DIR = "Logs"
OUTPUT_DIR_DOCKER = "/output"
INPUT_DIR_DOCKER = "/input"
DOCKER_CMD = "docker run -v {output_volume}:{output_volume_docker}: -v {input_volume}:{input_volume_docker} -v /var/run/docker.sock:/var/run/docker.sock {image}:{tag} {option}"

logger = None

processes = []

def logSubprocess(cmd,exit_code):
    """
    Logging subprocesses and their exit codes in a standard way
    """
    logger.info(f"[{exit_code:3d}] {cmd}")

def printConfig(config):
    """
    Printing the global configuration in a user friendly way
    """
    print(json.dumps(config,indent=4))

def finish():
    """
    Waits for all processes to end logs their return codes, also closes all log files used for each process
    """
    for call, p, f in globals()["processes"]:
        p.wait() 
        logSubprocess(call,p.returncode)
        f.close()
    

def setup():
    """
    Creates the reporting and logs directories if they don't exist already, also setups up the logger
    """
    logging.basicConfig(filename=f'{OUTPUT_DIR}/{LOGS_DIR}/app.log', filemode='w', format='[%(name)-8s]  [%(levelname)-8s]  %(message)s', level=logging.DEBUG)
    globals()["logger"] = logging.getLogger()

    mkdir_output_cmd = f"mkdir {OUTPUT_DIR}/{REPORT_DIR}"
    mkdir_logs_cmd = f"mkdir {OUTPUT_DIR}/{LOGS_DIR}"

    exit_code_mkdir_output = subprocess.run(mkdir_output_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    logSubprocess(mkdir_output_cmd,exit_code_mkdir_output)
    exit_code_mkdir_logs = subprocess.run(mkdir_logs_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    logSubprocess(mkdir_logs_cmd,exit_code_mkdir_logs)

def getRuns(config):
    res = []
    for run in config["runs"]:
        if "custom_args" not in run:
            custom_args = ""
        else:
            custom_args = run["custom_args"]
        res.append((run["tool"],run["option"],run["args"],custom_args))

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
    call = DOCKER_CMD.format(output_volume=OUTPUT_DIR,input_volume=INPUT_DIR,\
                        output_volume_docker=output_volume_docker,input_volume_docker=input_volume_docker,\
                        image=config["image"],tag=config["tag"],option=option_cmd)

    # Create log file and run the process
    f = open(f'{OUTPUT_DIR}/{LOGS_DIR}/{tool}.log',"w")
    p = subprocess.Popen(call, shell=True, stdout=f, stderr=f)
    globals()["processes"].append((call, p, f))

def main():

    config = toml.loads(open("input/run.toml").read())
    printConfig(config)

    setup()

    for r in getRuns(config):
        runTool(*r)

    # TODO
    # - Cleanup the docker environemnt with deleting the containers (Add option to leave images)
    # - Add argument to pass the config file with the runs to allow for docker and local testing
    finish()

if __name__ == "__main__":
    main()