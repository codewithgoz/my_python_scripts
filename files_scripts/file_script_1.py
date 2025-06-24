#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     Ejercicio 1
#   (___________)   Obtener el directorio home
#  (_____________)
#######################################################################


# Obtener el directorio home

from pathlib import Path
import os

# Utilizando pathlib
my_home = Path.home()
print(my_home)
print(type(my_home))

# Utilizando os
my_home = os.path.expanduser('~')
print(my_home)
print(type(my_home))


# En Linux /home/goz
# En Windows C:\Users
# En Mac \Users

# Recuerda que tus scripts se ejecutarán si tienes permisos en el directorio



