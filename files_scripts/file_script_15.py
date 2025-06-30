#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_15.py
#   (___________)   Validar rutas con las bibliotecas
#  (_____________)  pathlib y os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os

my_directory = Path.cwd() / Path('files_scripts')
print(my_directory)

my_file = Path.cwd() / Path('files_scripts/file_script_1.py')
print(my_file)


# Validando con pahtlib
# Validar existencia
print(my_directory.exists())

# Validar que sea directorio
print(my_directory.is_dir())

# Validar que sea archivo
print(my_directory.is_file())



# Validando con os
# Validar existencia
print(os.path.exists(my_directory))

# Validar que sea directorio
print(os.path.isdir(my_directory))

# Validar que sea archivo
print(os.path.isfile(my_directory))
