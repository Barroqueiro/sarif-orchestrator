import os
import json 

from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader

# Local modules
from src.constants import *

# Reporting functions

def populate_level(results, rules):
    """
    Populate the level atribute of sarif results if not included
    """
    for r in results:
        if "level" not in r:
            # Check for default configuration inside the rule
            if "defaultConfiguration" in rules[r["ruleId"]]:
                if "level" in rules[r["ruleId"]]["defaultConfiguration"]:
                    r["level"] = rules[r["ruleId"]]["defaultConfiguration"]["level"]
                else:
                    r["level"] = "warning"
            else:
                r["level"] = "warning"

def produce_sarif_reports(types):
    """
    Walk through a directory and find all sarif files, produce a report for each type for each file
    """
    for t in types.split(","):
        for subdir, dirs, files in os.walk(INPUT_DIR_DOCKER):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ".sarif" in file and t in ["MD","HTML","PDF"]:
                    produce_single_sarif(os.path.join(subdir, file),OUTPUT_DIR_DOCKER, t)

def produce_single_sarif(file, output_dir, t):
    """
    Given a sarif file, recover information and craft a markdown file that represents the findings
    """
    basename = os.path.basename(file)

    with open(file,"r") as f:
        data = json.loads(f.read())

    # Get information on the tool and it's rules 
    info_rules_tools = data["runs"][0]["tool"]["driver"]

    # Produce dictionary with rules
    if "rules" in info_rules_tools:
        rules_info = {r["id"]: r for r in info_rules_tools["rules"]}
    else:
        rules_info = {}

    # Produce dictionary for tool information without the rules
    tool_info = {key: value for key, value in info_rules_tools.items() if key != "rules"}

    # Populate the level of results to then order it
    results = data["runs"][0]["results"]
    populate_level(results, rules_info)

    results_info = [r for r in sorted(results, key=lambda x: "f" if x["level"] == "warning" else x["level"])]
    extension = EXTENSIONS[t]

    # Load template and produce final report
    env = Environment(loader=FileSystemLoader("templates"), autoescape=True, extensions=['jinja2.ext.do'])
    template = env.get_template(f'Sarif_to_{t}.jinja2')
    output_from_parsed_template = template.render(tool=tool_info,rules=rules_info,results=results_info)
    if t == "PDF":
        pisa.CreatePDF(
            src=output_from_parsed_template,  # HTML to convert
            dest=open(output_dir + "/" + basename.split(".sarif")[0]+extension,"w+b"))
    else:
        with open(output_dir + "/" + basename.split(".sarif")[0]+extension,"w") as f:
            f.write(output_from_parsed_template)