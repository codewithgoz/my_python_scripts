#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_9.py
#   (___________)   Trabajar con rutas absolutas y relativas con
#  (_____________)  las bibliotecas pathlib y os
#######################################################################

from pathlib import Path
import os

# Creando una ruta absoluta con pathlib
my_absolute_path = Path.cwd()
print(my_absolute_path)
print(my_absolute_path.is_absolute())

# Creando una ruta relativa con pathlib
my_relative_path = Path('data','csv','2025')
print(my_relative_path)
print(my_relative_path.is_absolute())

# Obtener una ruta absoluta de una ruta relativa con pathlib
my_complete_path = Path.cwd() / my_relative_path
print(my_complete_path)
print(my_complete_path.is_absolute())

# Obtener un string de una ruta absoluta con os
print(os.path.abspath('.'))
print(os.path.abspath(my_relative_path))

# Comprobando rutas absolutas y relativas con os
print(os.path.isabs(my_absolute_path))
print(os.path.isabs(my_relative_path))

# Obtener un string de una ruta relativa a partir
# de una ruta absoluta, esta se genera del path
# de inicio hasta el path os.path.relpath(path, path de inicio)
print(my_complete_path)
print(os.path.relpath(my_complete_path, '/home/goz/'))










