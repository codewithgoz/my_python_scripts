#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_17.py
#   (___________)   Mover archivos y directorios con la biblioteca
#  (_____________)  shutil
#######################################################################

# pathlib y shutil forman parte de la biblioteca estándar
from pathlib import Path
import shutil


my_directory = Path.cwd() / Path('files_scripts')
print(my_directory)

my_file = Path.cwd() / Path('files_scripts/data.txt')
print(my_file)

# Creamos un directorio nuevo
Path(my_directory, 'my_copies3').mkdir()
my_new_directory = Path(my_directory, 'my_copies3')

# Movemos my_file al directorio nuevo
shutil.move(my_file, my_new_directory)


# Creamos un directorio nuevo
Path(my_directory, 'all_copies').mkdir()
my_new_directory2 = Path(my_directory, 'all_copies')

# Movemos copies3 a all_copies
shutil.move(my_new_directory, my_new_directory2)


