# Python desde Cero - Code with Goz
# https://codewithgoz.com
# Autor: Goz
# 1. Pedidos en Pizzería (Parte 1)
# Escribe un programa que le permita al usuario pedir una pizza.
# Requerimientos:
# - Al inicio el programa saluda al usuario
# - El programa muestra el mensaje "Selecciona una pizza" y muestra las siguientes pizzas:
#   mexicana, peperoni, hawaiana, especial, campirana, festiva.
# - El usuario selecciona su pizza
# - El programa muestra el mensaje "Selecciona el tamaño de tu pizza" y muesta las siguientes opciones:
#   infantil, mediana, grande, gigante, morbida
# - El usuario selecciona el tamaño
# - El programa pide al usuario que escriba la dirección de su domicilio.
# - El programa pide al usuario que escriba su número de teléfono.
# - El programa muestra un resumen de todo el pedido.


# Asignando textos de las secciones
title = 'Pizzas Panuchi'
welcome = 'Bienvenido/a desde este sistema puedes pedir tu pizza'
instructions_1 = 'Selecciona una pizza:'
instructions_2 = 'Escribe el numero del tipo de pizza: '
instructions_3 = 'Escribe el numero del tamaño de pizza: '
instructions_4 = 'Escribe tu dirección: '
instructions_5 = 'Escribe tu número telefónico: '
instructions_6 = 'El resumen de tu orden es:'
# Diccionarios con los tipos y tamaños de pizza
pizza_types = {'1':'mexicana', '2':'peperoni', '3':'hawaiana', '4':'especial', '5':'campirana', '6':'festiva'}
pizza_sizes = {'1':'infantil', '2':'mediana', '3':'grande', '4':'gigante', '5':'morbida'}
# Definimos un separador
separator = 56 * '*'

# Lista en la que almacenaremos todo el pedido del cliente
client_order = []

# Imprime en pantalla las distintas secciones
print(separator)
print(title)
print(welcome)
print(separator)
print(instructions_1)

# Recorremos el diccionario pizza_types para imprimir los tipos de pizza
for key, value in pizza_types.items():
    print(f'{key}. {value.capitalize()}')
print(separator)
# Solicitamos al usuario su selección de pizza
pizza_selection = input(instructions_2)
# Almacenamos el tipo de pizza en la lista client_order
client_order.append(pizza_types[pizza_selection])

print(separator)
# Recorremos el diccionario pizza_selection para imprimir los tamaños de pizza
for key, value in pizza_sizes.items():
    print(f'{key}. {value.capitalize()}')
print(separator)
# Solicitamos al usuario su selección de tamaño
size_selection = input(instructions_3)
print(separator)
# Almacenamos el tamaño de pizza en la lista client_order
client_order.append(pizza_sizes[size_selection])

# Solicitamos al usuario su dirección
client_address = input(instructions_4)
# Almacenamos la dirección del cliente en la lista client_order
client_order.append(client_address)
print(separator)

# Solicitamos al usuario su teléfono
client_phone = input(instructions_5)
# Almacenamos el teléfono del cliente en la lista client_order
client_order.append(client_phone)
print(separator)

# Imprime el resumen del pedido
print(instructions_6)
print(f'Tipo de pizza: {client_order[0].capitalize()}')
print(f'Tamaño de pizza: {client_order[1].capitalize()}')
print(f'Entregar en: {client_order[2]}')
print(f'Teléfono: {client_order[3]}')
print(separator)