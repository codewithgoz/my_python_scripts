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


from pathlib import Path
import os

# Los directorios home:
# En Linux /home/goz
# En Windows C:\Users
# En Mac \Users

# Recuerda que tus scripts se ejecutarán si tienes permisos en el directorio

# Utilizando pathlib
my_home_1 = Path.home()
print(my_home_1)
print(type(my_home_1))

# Utilizando os
my_home_2 = os.path.expanduser('~')
print(my_home_2)
print(type(my_home_2))






