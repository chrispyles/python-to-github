##################################################
##### JS Menu Generator for Python to Github #####
#####           by Chris Pyles               #####
##################################################

import os
import string
import re

def list_files(directory = "."):
    """
    Returns a list of all non-hidden files in a specified directory
    
    Args:
        directory - directory to list files in; default = "."
    """
    return [file for file in os.listdir(directory) if file[0] != "."]

# list files in notebooks directory
files = list_files("../notebooks")

# initialize the strings that will become the JS files
menu_string = """var html = `<br><strong>Notebooks:</strong>"""
index_menu_string = """var html = `<br><strong>Notebooks:</strong>"""

# add index page to JS strings
menu_string += """ <a href="../index.html">Home</a>"""
index_menu_string += """ <a href="index.html">Home</a>"""

# iterate through each file to add it to the JS strings
for file in [file for file in files if file != "index.ipynb"]:
    
    # get title string
    title = file[3:-6].replace("-", " ")
    title = string.capwords(title)
    if "Eda" in title:
        title = re.sub("Eda", "EDA", title)
        
    # add title string to menu strings
    menu_string += """ | <a href="{}.html">{}</a>""".format(
        file[:-6],
        title
    )
    
    index_menu_string += """ | <a href="{}.html">{}</a>""".format(
        "export/" + file[:-6],
        title
    )
    
menu_string += """`; document.write(html);"""
index_menu_string += """`; document.write(html);"""

with open("../export/menus/menu.js", "w+") as file:
    file.write(menu_string)
    
with open("../export/menus/index-menu.js", "w+") as file:
    file.write(index_menu_string)