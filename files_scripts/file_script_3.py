#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_3.py
#   (___________)   Cambiar de directorio con la biblioteca os
#  (_____________)  
#######################################################################

from pathlib import Path
import os

# Revisamos el directorio de trabajo actual
print(Path.cwd())

# Cambiamos de directorio
os.chdir('/home/goz')

# Revisamos el nuevo directorio de trabajo
print(Path.cwd())

# Nota: 
# pathlib no tiene un función para cambiar de directorio debido a que
# cambiar el directorio de trabajo mientras un programa se está 
# ejecutando puede traer errores.
