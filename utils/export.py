##########################################################
##### Jupyter Notebook Exported for Python to Github #####
#####                 by Chris Pyles                 #####
##########################################################

import nbformat
from nbconvert import HTMLExporter

# run the menu generator
from generate_menus import *

# load the files in the notebooks directory
files = list_files("../notebooks")

# instantiate the nbconvert exporter
html_exporter = HTMLExporter()

# iterate through the non-index notebooks to write the HTML
for file in [file for file in files if file != "index.ipynb"]:
    notebook = nbformat.read("../notebooks/" + file, as_version = 4)
    body, _ = html_exporter.from_notebook_node(notebook)
    with open("../export/" + file[:-6] + ".html", "w+") as f:
        f.write(body)
        
# export index.ipynb file
notebook = nbformat.read("../notebooks/index.ipynb", as_version = 4)
body, _ = html_exporter.from_notebook_node(notebook)
with open("../index.html", "w+") as f:
    f.write(body)