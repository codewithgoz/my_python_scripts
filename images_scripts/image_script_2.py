#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Imágenes  
#     (_______)     image_script_2.py
#   (___________)   Obtener la metadata de las imágenes con la
#  (_____________)  biblioteca exif
#######################################################################

from exif import Image
from pathlib import Path

# https://exiftool.org/TagNames/EXIF.html

# Creamos una ruta hacia nuestra imagen
image_path = Path.cwd() / Path('images_scripts','images','image_6.jpg')

with open(image_path, "rb") as image_file:
    image = Image(image_file)

    if image.has_exif:
        # Mostramos los atributos del EXIF
        print(sorted(image.list_all()))

        # Obtenemos los valores del EXIF:
        for tag in sorted(image.list_all()):
            try:
                value = image.get(tag, 'no data')
                print(f"{tag}: {value}")
            except:
                print(f'No se puede cargar el valor {tag}')

    else:
        print("El archivo no tiene EXIF info")
