#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_10.py
#   (___________)   Obtener las partes de una ruta con la biblioteca
#  (_____________)  pathlib
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path

my_path = Path.cwd() / Path('libraries','old','admin.py')
print(my_path)

# Obtener el directorio principal del sistema
print(my_path.anchor)
print(type(my_path.anchor))

# Obtener los directorios de la ruta
print(my_path.parent)
print(type(my_path.parent))

# Obtener algunos directorios de la ruta
print(my_path.parents[3])
print(type(my_path.parents))

# Obtener el nombre y extensión del archivo en la ruta
print(my_path.name)
print(type(my_path.name))

# Obtener el nombre del archivo en la ruta
print(my_path.stem)
print(type(my_path.stem))

# Obtener la extensión del archivo en la ruta
print(my_path.suffix)
print(type(my_path.suffix))

# Obtener el drive de la ruta en Windows
print(my_path.drive)
print(type(my_path.drive))
