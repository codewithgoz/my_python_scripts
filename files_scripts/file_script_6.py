#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_6.py
#   (___________)   Crea varias carpetas con la biblioteca os
#  (_____________)  
#######################################################################

from pathlib import Path
import os

# Obtenemos el directorio actual
my_current_path = Path.cwd()
print(my_current_path)

# Creamos una nueva ruta
new_directories = my_current_path / Path('data','json','reports')
print(new_directories)

# Crea no solo una sino todas las carpetas necesarias
os.makedirs(new_directories)




