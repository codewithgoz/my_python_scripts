#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_21.py
#   (___________)   Recorrer el árbol de directorios con
#  (_____________)  la biblioteca os
#######################################################################

from pathlib import Path
import os

my_disordered_files = Path.cwd() / Path('sandbox')

print(my_disordered_files)


for folder_name, subfolders, filenames in os.walk(my_disordered_files):
    print('El directorio ' + folder_name)

    for subfolder in subfolders:
        print('Tiene el subdirectorio ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('Tiene el archivo ' + folder_name + ': '+ filename)   
    
    print('')









