#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_18.py
#   (___________)   Copiar archivos y directorios con la biblioteca
#  (_____________)  shutil
#######################################################################

# pathlib y shutil forman parte de la biblioteca estándar
from pathlib import Path
import shutil


my_file = Path.cwd() / Path('files_scripts/data.txt')
print(my_file)

my_file2 = Path.cwd() / Path('files_scripts/data2.txt')
print(my_file2)

# Cambiamos el nombre del archivo
shutil.move(my_file, my_file2)


my_directory = Path.cwd() / Path('files_scripts')

# Creamos un directorio nuevo
Path(my_directory, 'all_data').mkdir()
my_new_directory = Path(my_directory, 'all_data')

# Creamos otro directorio nuevo
my_new_directory2 = Path(my_directory, 'all_data2')

# Cambiamos el nombre del directorio
shutil.move(my_new_directory, my_new_directory2)


