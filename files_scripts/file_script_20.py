#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_20.py
#   (___________)   Eliminar de forma segura archivos y directorios
#  (_____________)  con la biblioteca send2trash
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import send2trash

my_directory = Path.cwd() / Path('files_scripts')

my_file = my_directory / Path('data.txt')
print(my_file)

# Elimina el archivo data1.txt
# send2trash.send2trash(my_file)

# Creamos una ruta a directorio
my_new_directory = Path(my_directory, 'all_data')

# Elimina el directorio vacío all_data
# send2trash.send2trash(my_new_directory)

# Elimina el directorio con archivos all_data
# send2trash.send2trash(my_new_directory)





