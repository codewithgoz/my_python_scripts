#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_1.py
#   (___________)   Obtener el directorio home con las bibliotecas
#  (_____________)  pathlib y os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import os

# Los directorios home:
# En Linux /home/goz
# En Windows C:\Users
# En Mac \Users

# Recuerda que tus scripts se ejecutarán si tienes permisos en el directorio

# Utilizando pathlib
print(Path.home())
print(type(Path.home()))

# Utilizando os
print(os.path.expanduser('~'))
print(type(os.path.expanduser('~')))






