# Constants
REPORT_DIR = "Reporting"                                    # Directory that will store the reports generated
LOGS_DIR = "Logs"                                           # Directory that will store the logs created (By this orchestrator and each tool)
OUTPUT_DIR_DOCKER = "/output"                               # Default directory that is used to share output information (From docker's prespective)
INPUT_DIR_DOCKER = "/input"                                 # Default directory that is used to share input information (From docker's prespective)
CONFIG_DIR_DOCKER = "/config"                               # Default directory that is used to share configuration information (From docker's prespective)
LOG_FILE = f'{OUTPUT_DIR_DOCKER}/{LOGS_DIR}/app.log'        # Log file
HASH_IGNORE_FILE = ".hashignore"
ID_IGNORE_FILE = ".idignore"
EXTENSIONS = {"MD": ".md", "HTML":".html", "PDF": ".pdf"}