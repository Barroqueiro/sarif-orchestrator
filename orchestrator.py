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

LOGGER = None

def logSubprocess(cmd,exit_code):
    LOGGER.info(f"[{exit_code}] {cmd}")

def dirSetup():
    """
    Create dirs for reporting and logging
    """
    mkdir_output_cmd = f"mkdir {OUTPUT_DIR}/{REPORT_DIR}"
    mkdir_logs_cmd = f"mkdir {OUTPUT_DIR}/{LOGS_DIR}"
    exit_code_mkdir_output = subprocess.run(mkdir_output_cmd, shell=True).returncode
    exit_code_mkdir_logs = subprocess.run(mkdir_logs_cmd, shell=True).returncode

    logSubprocess(mkdir_output_cmd,exit_code_mkdir_output)
    logSubprocess(mkdir_logs_cmd,exit_code_mkdir_logs)

def runTool(tool,option=None,args=[]):
    config = toml.loads(open(f"tools/{tool}.toml").read())

    cmd = DOCKER_CMD
    image = config["image"]
    tag = config["tag"]

    if not option:
        option = config["default_option"]

    if config["output_volume_docker"] == "":
        output_volume_docker = OUTPUT_DIR_DOCKER
    else:
        output_volume_docker = config["output_volume_docker"]

    if config["input_volume_docker"] == "":
        input_volume_docker = INPUT_DIR_DOCKER
    else:
        input_volume_docker = config["input_volume_docker"]

    output = f"{output_volume_docker}/{REPORT_DIR}/{tool}_{option}.sarif"

    option_cmd = config["options"][option].format(*args,output_place=output)

    call = cmd.format(output_volume=OUTPUT_DIR,input_volume=INPUT_DIR,\
                        output_volume_docker=output_volume_docker,input_volume_docker=input_volume_docker,\
                        image=image,tag=tag,option=option_cmd)

    exit_code_run = subprocess.run(call, shell=True).returncode

    logSubprocess(call,exit_code_run)


def main():

    logging.basicConfig(filename=F'{OUTPUT_DIR}/{LOGS_DIR}/app.log', filemode='w', format='[%(name)-8s]  [%(levelname)-8s]  %(message)s', level=logging.DEBUG)
    globals()["LOGGER"] = logging.getLogger()

    config = toml.loads(open("input/run.toml").read())
    print(json.dumps(config,indent=4))
    dirSetup()

    for run in config["runs"]:
        runTool(run["tool"],run["option"],run["args"])

if __name__ == "__main__":
    main()