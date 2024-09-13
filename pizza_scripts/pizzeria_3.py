# Python desde Cero - Code with Goz
# https://codewithgoz.com
# Autor: Goz
# Modifica el programa de la Parte 2 agregando lo siguiente:
# pizzas   | infantil | mediana | grande | gigante | morbida | 
# mexicana | 50       | 160     | 260    | 370     | 480 |
# peperoni | 50       | 160     | 260    | 370     | 480 |
# hawaiana | 50       | 160     | 280    | 370     | 480 |
# especial | 57       | 190     | 260    | 390     | 520 |
# campirana| 50       | 180     | 280    | 370     | 480 |
# festiva  | 50       | 180     | 280    | 370     | 480 |
# Con base a la tabla de precios modifica el programa para que se muestren los precios al seleccionar el
# tamaño de pizza y que en el resumen final se muestre la cuenta por pizza y por total.


# Asignando formato y colores a los textos de las secciones
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
order_5 = 'Precio:'

pizzas = ['Mexicana', 'Peperoni', 'Hawaiana', 'Especial', 'Campirana', 'Festiva']
sizes = ['infantil','mediana','grande','gigante','morbida']

prices = {
    'Mexicana':{'infantil':50, 'mediana':160, 'grande':260, 'gigante':370, 'morbida':480},
    'Peperoni':{'infantil':50, 'mediana':160, 'grande':260, 'gigante':370, 'morbida':480},
    'Hawaiana':{'infantil':50, 'mediana':160, 'grande':280, 'gigante':370, 'morbida':480},
    'Especial':{'infantil':57, 'mediana':190, 'grande':260, 'gigante':390, 'morbida':520},
    'Campirana':{'infantil':50, 'mediana':180, 'grande':280, 'gigante':370, 'morbida':480},
    'Festiva':{'infantil':50, 'mediana':180, 'grande':280, 'gigante':370, 'morbida':480}
}

separator = 56 * '*'
separator_2 = 56 * '-'


# Lista en la que almacenaremos todo el pedido del cliente
complete_order = []
client_contact = []

status = True
while status:
    # Imprime en pantalla las distintas secciones
    print(separator)
    print(title)
    print(welcome)
    print(separator)
    print(instructions_1)

    # Recorremos el diccionario para imprimir los tipos de pizza
    for index, pizza in enumerate(pizzas):
        print(f"{index + 1}. {pizza}")
    print(separator)
    # Solicitamos al usuario su selección de pizza
    pizza_selection = input(instructions_2)
    # Almacenamos el tipo de pizza en la lista client_order
    client_order = []
    client_order.append(pizzas[int(pizza_selection) - 1])

    # Recorremos el diccionario para imprimir los tamaños y precios de pizza
    for index, size in enumerate(sizes): 
        print(f"{index + 1}. {size} | ${prices[client_order[-1]][size]}")
    print(separator)
    # Solicitamos al usuario su selección de pizza
    size_selection = input(instructions_3)
    # Almacenamos el tipo de pizza en la lista client_order
    client_order.append(sizes[int(size_selection) - 1])
    client_order.append(prices[client_order[0]][client_order[1]])
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
    print(f'{order_5} ${pizza[2]}')
print(separator)
print(f'{order_3} {client_contact[0]}')
print(f'{order_4} {client_contact[1]}')

# Imprime el total del pedido
print(separator)
total = 0
for price in complete_order:
    total += price[2]

print(f"Total: ${total}")


