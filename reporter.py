import sys
import json
from jinja2 import Environment, FileSystemLoader

def print_pretty(data):
    """
    Printing the global configuration in a user friendly way using json indent
    """
    print(json.dumps(data,indent=4))

with open(sys.argv[1],"r") as f:
    data = json.loads(f.read())

env = Environment(loader=FileSystemLoader("templates"), autoescape=True, extensions=['jinja2.ext.do'])
template = env.get_template('Sarif_to_Markdown.jinja2')
output_from_parsed_template = template.render(sarif=data)
with open("output"+".md","w") as f:
    f.write(output_from_parsed_template)