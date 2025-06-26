#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_5.py
#   (___________)   Crea un directorio nuevo con la biblioteca pathlib
#  (_____________)  
#######################################################################

from pathlib import Path

# Obtenemos el directorio actual
my_current_path = Path.cwd()
print(my_current_path)

# Crea un directorio nuevo
Path(my_current_path, 'images').mkdir()




