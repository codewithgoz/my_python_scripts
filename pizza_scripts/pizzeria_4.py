# Python desde Cero - Code with Goz
# https://codewithgoz.com
# Autor: Goz
# Modifica el programa de la Parte 3 agregando lo siguiente:
# Al iniciar el programa debe presentar un mensaje de bienvenida y un menú con las siguientes opciones:
# 1.- Pedir Pizza
# 2.- Ver nuestra ubicación
# 3.- Nuestra Historia
# Salir del programa (s)
# Al escribir en 1 se corre la Parte 3
# Al escribir en 2 se muestra la dirección de la pizzería (invéntala)
# Al escribir en 3 se muestra la historia de la pizzería (invéntala)
# Al escribir s el programa termina


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
order_5 = 'Precio:'
location = "Estamos ubicados en Calle La Cascada #24234"
history = "Tenemos más de 60 años preparando las pizzas más deliciosas del planeta"
main_instructions_1 = 'Elige una opción:'
main_option_1 = '1.- Pedir Pizza'
main_option_2 = '2.- Ver nuestra ubicación'
main_option_3 = '3.- Nuestra Historia'
main_option_4 = 'Salir del programa (s)'
main_question_1 = '¿Que quieres hacer?'
error_message = 'La opción no es correcta'

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



main_status = True
while main_status:
    # Imprime en pantalla las distintas secciones
    print(separator)
    print(title)
    print(welcome)
    print(separator)
    print(main_instructions_1)
    print(main_option_1)
    print(main_option_2)
    print(main_option_3)
    print(main_option_4)
    # Solicitamos al usuario su selección
    main_selection = input()

    if main_selection == '1':
        status = True
        while status:
            # Imprime en pantalla las distintas secciones
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

    elif main_selection == "2":
        print(location)
    elif main_selection == "3":
        print(history)
    elif main_selection == "s":
        main_status = False
    else:
        print(error_message)
