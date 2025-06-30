#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_14.py
#   (___________)   Obtener la lista de archivos de un directorio
#  (_____________)  utilizando patrones glob de la biblioteca pathlib
#######################################################################


# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path

my_directory = Path.cwd() / Path('files_scripts')
print(my_directory)

# Búsqueda de archivos por patrón
my_files = my_directory.glob('*')
print(type(my_files))
for file in my_files:
    print(file)

print('***********************************')

# Búsqueda de archivos por patrón
my_script_files = my_directory.glob('*.py')
print(type(my_script_files))
for file in my_script_files:
    print(file)

print('***********************************')

# Búsqueda de archivos por patrón
my_txt_files = my_directory.glob('*.txt')
print(type(my_txt_files))
for file in my_txt_files:
    print(file)

print('***********************************')

# Búsqueda de archivos por patrón
my_pattern_files = my_directory.glob('file_script_?.py')
print(type(my_pattern_files))
for file in my_pattern_files:
    print(file)   




