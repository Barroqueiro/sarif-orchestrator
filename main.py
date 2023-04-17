"""
Docker container orchestrator for SARIF reporting tools
"""
import toml
import argparse

from src.orchestrator import *
from src.reporting import *
from src.upload import *
from src.constants import *

def parse():
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

    report_parser = subparsers.add_parser("report", help="Produce Markdown reports from sarif files")
    report_parser.add_argument('--type', type=str, required=True,
                        help='Type of report to produce')

    upload_parser = subparsers.add_parser("upload", help="Upload results to DefectDojo")
    upload_parser.add_argument('--config', type=str, required=True,
                        help='Configuration file for upload')
    args = parser.parse_args()
    command_args = vars(args)

    return command_args


# Main
def main():
    command_args = parse()
    command = command_args["command"]

    if command == "orchestrator":

        config = toml.loads(open(command_args["config"]).read())

        setup()
        
        runs = get_runs(config)
        print_config(runs)

        to_clean = run_tasks(runs, command_args["input_dir_host"], command_args["output_dir_host"], command_args["config_dir_host"])

        finish(to_clean, command_args["keep_images"])

        update_sarif_reports()
    
    if command == "report":

        produce_sarif_reports(command_args["type"])

    if command == "upload":

        config = toml.loads(open(command_args["config"]).read())
        print_config(config)

        if config["file"]:
            upload_file(config, "{input_dir}/{file}".format(input_dir=INPUT_DIR_DOCKER,file=config["file"]))
        else:
            upload_dir(config)

if __name__ == "__main__":
    main()
