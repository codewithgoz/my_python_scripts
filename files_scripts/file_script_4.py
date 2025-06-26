#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     file_script_4.py
#   (___________)   Creación de rutas con la biblioteca pathlib
#  (_____________)  
#######################################################################

# Recordemos que:
# En windows utilizamos '\'  
# C:\Users\batman
# En linux y mac utilizamos '/'
# /home/batman

# ¿Qué pasa cuando necesitamos que nuestro
# programa pueda trabajar con ambas rutas?

from pathlib import Path

my_path = Path('Users','batman','weapons')

# Lo anterior genera un:
# WindowsPath object para Windows
# PosixPath object para Linux y Mac
print(type(my_path))
print(my_path)
print(str(my_path))
print('***********************************')


# pathlib fue introducido en Python 3.4 para reemplazar os.path
# https://docs.python.org/3/library/pathlib.html

# Uso del operador / en Paths
# Nos ahorra mucho trabajo ya que nos permite modificar objetos Path

complete_path = my_path / 'data' / 'data.csv'
print(complete_path)
print(type(complete_path))

complete_path2 = my_path / Path('data/data.csv')
print(complete_path2)
print(type(complete_path2))

complete_path3 = my_path / Path('data','data.csv')
print(complete_path3)
print(type(complete_path3))

complete_path4 = my_path / Path('data','data2') / 'data.csv'
print(complete_path4)
print(type(complete_path4))

complete_path5 = my_path / Path('data','data2') /  Path('data3','data4') / 'data.csv'
print(complete_path5)
print(type(complete_path5))

# Lo anterior es más seguro que realizar concatenaciones o joins
# Recuerda que cuando uses / siempre debe haber un Path
# El operador / reemplaza al antiguo os.path.join()









