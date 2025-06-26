
#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_2.py
#   (___________)   Obtener el directorio de trabajo actual
#  (_____________)  pathlib y os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os

# Utilizando pathlib
print(Path.cwd())
print(type(Path.cwd))

# Utilizando os
print(os.getcwd())
print(type(os.getcwd()))
