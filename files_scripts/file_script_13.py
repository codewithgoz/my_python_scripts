#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_13.py
#   (___________)   Obtener la lista de archivos de un directorio
#  (_____________)  con la biblioteca os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os

my_directory = Path.cwd() / Path('files_scripts')
print(my_directory)

# Obtenemos una lista con los archivos en el directorio
my_files = os.listdir(my_directory)

print(my_files)



