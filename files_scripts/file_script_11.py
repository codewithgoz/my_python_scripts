#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_11.py
#   (___________)   Obtener las partes de una ruta con la biblioteca
#  (_____________)  os
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
import os

my_path = '/home/goz/my_python_scripts/data.txt'
print(my_path)

# Obtener los directorios de la ruta en un string
print(os.path.dirname(my_path))

# Obtener el nombre del archivo en la ruta
print(os.path.basename(my_path))

# Obtener los directorios y el nombre de la ruta
# en una tupla
print(os.path.split(my_path))

# Obtener todas las partes de una ruta
# en una lista
print(my_path.split(os.sep))




