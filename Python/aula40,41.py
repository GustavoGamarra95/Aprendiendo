""" Calculadora con while"""
while True:
    numero_1 = input('Digite un numero: ')
    numero_2 = input('Digite un numero: ')
    operador = input('Digite un operador (+-/*): ')

    numeros_validos = True
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        numeros_validos = True

    if numeros_validos is None:
        print('Uno o ambos numeros no son validos')
        continue

    operadores_validos = '+-/*'
    if operadores_validos not in operadores_validos:
        print('Uno o ambos numeros no son validos')
        continue

    if len(operador) > 1:
        print('Digite apenas un operador')
        continue

    print('Realizando el calculo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float )
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float )

    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float )


    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float )

        
    else:
        print('No se deve mostrar este mensaje')

    salir = input('Deseas Salir? [s]i: ').lower().startswith('s')
    if salir is True:
        break

    