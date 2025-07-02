#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     organizer.py
#   (___________)   Script para organizar nuestros archivos
#  (_____________)  
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os
import re
import shutil

my_directory = Path.cwd() / Path('sandbox')
my_current_directory = Path.cwd()

Path(my_current_directory, 'my_super_files').mkdir()
my_super_files = Path.cwd() / Path('my_super_files')

for folder_name, subfolders, filenames in os.walk(my_directory):
    for filename in filenames:
        my_pattern = r"\w+\.jpeg"
        #my_pattern = r"\w+\.(jpeg|png)"
        #my_pattern = r"\Aimage[0-9]*\.jpeg"
        #my_pattern = r"\A[a-z]+[0-9]+\_[A-Z]{4}\.xlsx"

        if re.search(my_pattern, filename):
            my_image_path = Path(folder_name, filename)  
            print(my_image_path) 
            shutil.copy(my_image_path, my_super_files)











