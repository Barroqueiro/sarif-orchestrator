"""
Upload module to integrate the automatic upload of sarif files to DefectDojo
"""

import os
import requests

# Local modules
from src.constants import *

# Upload Functions

def upload_file(config, file):
    """
        Upload a specific SARIF file to an engagement in DefectDojo 
    """

    params = {k:v for k,v in config.items() if k not in ["url","file","dir","auth"]}
    params["scan_type"] = "SARIF"

    headers = {'Authorization': 'token {}'.format(config["auth"])}

    with open(file) as f:
        r = requests.post("{url}/api/v2/import-scan/".format(url=config["url"]), files={'file': f}, data=params, headers=headers)

    print("Upload comcluded with code: ",r.status_code)

def upload_dir(config):
    """
    Upload all SARIF files inside a directory to DefectDojo making use of the upload_file function
    """

    directory = config["dir"]
    for subdir, dirs, files in os.walk(f"{INPUT_DIR_DOCKER}/{directory}"):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ".sarif" in file:
                upload_file(config, os.path.join(subdir, file))