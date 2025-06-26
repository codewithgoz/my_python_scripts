#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_7.py
#   (___________)   Listar subdirectorios con la biblioteca pathlib
#  (_____________)  
#######################################################################

from pathlib import Path


# Utilizando la ruta absoluta
my_current_path = Path.cwd()
print(my_current_path)

subdirectories = [x for x in my_current_path.iterdir() if x.is_dir()]
print(type(subdirectories))
print(subdirectories)


# Utilizando la ruta relativa
my_current_path = Path('.')
print(my_current_path)

subdirectories = [x for x in my_current_path.iterdir() if x.is_dir()]
print(type(subdirectories))
print(subdirectories)






