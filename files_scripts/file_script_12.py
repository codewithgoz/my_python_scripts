#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_12.py
#   (___________)   Obtener el tamaño de los archivos con
#  (_____________)  la biblioteca os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os

my_path = Path.cwd() / Path('files_scripts','file_script_1.py')
print(my_path)

# Obtenemos el tamaño del archivo (bytes)
file_size = os.path.getsize(my_path)

print(file_size)

