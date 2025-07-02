#######################################################################
#       __
#      (00)         Code With Goz - https://codewithgoz.com
#      \__/         Curso: Automatiza Tareas con Python
#      /^/          Autor: Goz
#     ( (            
#     \_\_____      Automatización de Archivos y Directorios   
#     (_______)     directory_creator.py
#   (___________)   Script para crear directorios a partir de
#  (_____________)  de un txt
#######################################################################

# pathlib y os forman parte de la biblioteca estándar
from pathlib import Path
import shutil

my_current_directory = Path.cwd()
my_sandbox2 = my_current_directory / Path('sandbox2')
my_data = my_current_directory / Path('sandbox2') / 'data.txt'
people_images_path = Path(my_sandbox2, 'people_images')


with open(my_data, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            people = line.split()
            id = people[0]
            name = people[1]
            Path(my_sandbox2, name).mkdir()
            person_path = Path(my_sandbox2, name, 'info.txt')
            person_path2 = Path(my_sandbox2, name)
        
            with open(person_path, 'a', encoding='utf-8') as person_file:
                person_file.write(f'Expediente de {name}')
                    
            images = list(people_images_path.glob('**/*.*'))

            for image in images:
                if image.stem == id:
                    shutil.copy(image, person_path2)














