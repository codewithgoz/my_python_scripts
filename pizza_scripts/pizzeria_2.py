# Python desde Cero - Code with Goz
# https://codewithgoz.com
# Autor: Goz
# 2. Pedidos en Pizzería (Parte 2)
# Modifica el programa de la Parte 1 agregando lo siguiente:
# - El programa al final debe preguntar si el usuario quiére otra pizza
# - En caso afirmativo todo el programa vuelve a hacer las preguntas y el resumen del final
#   debe mostrar toda la información del pedido.
# - Las preguntas de domicilio y teléfono sólo se pregunten una sola vez.


# Asignando textos de las secciones
title = 'Pizzas Panuchi'
welcome = 'Bienvenido/a desde este sistema puedes pedir tu pizza'
instructions_1 = 'Selecciona una pizza:'
instructions_2 = 'Escribe el numero del tipo de pizza: '
instructions_3 = 'Escribe el numero del tamaño de pizza: '
instructions_4 = 'Escribe tu dirección: '
instructions_5 = 'Escribe tu número telefónico: '
instructions_6 = 'El resumen de tu orden es:'
question_1 = '¿Quiéres agregar otra pizza? s/n '
order_1 = 'Tipo de pizza:'
order_2 = 'Tamaño de la pizza:'
order_3 = 'Dirección:'
order_4 = 'Teléfono:'

pizza_types = {'1':'mexicana', '2':'peperoni', '3':'hawaiana', '4':'especial', '5':'campirana', '6':'festiva'}
pizza_sizes = {'1':'infantil', '2':'mediana', '3':'grande', '4':'gigante', '5':'morbida'}

separator = 56 * '*'
separator_2 = 56 * '-'


# Lista en la que almacenaremos todo el pedido del cliente
complete_order = []
client_contact = []


status = True
while status:
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
    complete_order.append(client_order)

    other_pizza = input(f'{question_1}')
    if other_pizza == 'n':
        status = False

# Solicitamos al usuario su dirección
client_address = input(instructions_4)
# Almacenamos la dirección del cliente en la lista client_order
client_contact.append(client_address)
print(separator)

# Solicitamos al usuario su teléfono
client_phone = input(instructions_5)
# Almacenamos el teléfono del cliente en la lista client_order
client_contact.append(client_phone)
print(separator)

# Imprime el resumen del pedido
print(instructions_6)
for pizza in complete_order:
    print(separator_2)
    print(f'{order_1} {pizza[0].capitalize()}')
    print(f'{order_2} {pizza[1].capitalize()}')
print(separator)
print(f'{order_3} {client_contact[0]}')
print(f'{order_4} {client_contact[1]}')