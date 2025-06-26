#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_8.py
#   (___________)   Listar archivos dentro del árbol de directorios
#  (_____________)  utilizando la biblioteca pathlib
#######################################################################

from pathlib import Path

# Obtenemos el directorio actual
my_current_path = Path('.')
print(my_current_path)

# Obtenemos los archivos dentro del árbol de directorios
#my_python_scripts = list(my_current_path.glob('**/*.py'))
my_python_scripts = list(my_current_path.glob('**/*.*'))


print(my_python_scripts)

for my_script in my_python_scripts:
    print(my_script)









