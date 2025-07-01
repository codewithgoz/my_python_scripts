#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_19.py
#   (___________)   Eliminar archivos y directorios con las
#  (_____________)  bibliotecas shutil y os
#######################################################################

# shutil, pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import shutil
import os

my_directory = Path.cwd() / Path('files_scripts')

my_file = my_directory / Path('data.txt')
print(my_file)

# Elimina el archivo data1.txt
#os.unlink(my_file)

# Creamos una ruta a directorio
my_new_directory = Path(my_directory, 'all_data')

# Elimina el directorio vacío all_data
# os.rmdir(my_new_directory)

# Elimina el directorio con archivos all_data
# shutil.rmtree(my_new_directory)


