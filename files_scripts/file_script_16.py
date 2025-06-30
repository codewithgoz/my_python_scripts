#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_16.py
#   (___________)   Copiar archivos o directorios con 
#  (_____________)  la biblioteca shutil
#######################################################################

# pathlib y shutil forman parte de la biblioteca estándar
from pathlib import Path
import shutil

my_directory = Path.cwd() / Path('files_scripts')
print(my_directory)

my_file = Path.cwd() / Path('files_scripts/file_script_1.py')
print(my_file)

Path(my_directory, 'my_copies').mkdir()

# Copiamos el archivo
shutil.copy(my_file, my_directory / 'my_copies')

# Copiamos el directorio (crea el directorio nuevo)
shutil.copytree(my_directory / 'my_copies', my_directory / 'my_copies2')








