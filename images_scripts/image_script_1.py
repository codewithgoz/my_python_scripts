#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Imágenes  
#     (_______)     image_script_1.py
#   (___________)   Obtener la metadata de las imágenes con la
#  (_____________)  biblioteca pillow
#######################################################################

from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path


# Creamos una ruta hacia nuestra imagen
image_path = Path.cwd() / Path('images_scripts','images','image_2.jpg')

# Creamos una instancia de Image
my_image = Image.open(image_path)

# Obtenemos la metadata
print("Filename:", my_image.filename)
print("Image Size:", my_image.size)
print("Image Height:", my_image.height)
print("Image Width:", my_image.width)
print("Image Format:", my_image.format)
print("Image Mode:", my_image.mode)

# Obtenemos la EXIF data
exif_data = my_image.getexif()

# Iteramos sobre la EXIF data:
for tag_id, data in exif_data.items():
   # Obtenemos el nombre del tag en vez del id
   tag_name = TAGS.get(tag_id, tag_id)
   print(f"{tag_name:25}: {data}")





