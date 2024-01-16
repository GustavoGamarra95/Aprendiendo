"""
Ejercicio
Pida al usuario para digitar su nombre
Pida al usuario para digitar su edad
Si nombre y edad fueses digitados:
    Mostrar:
    Tu nombre es {nombre}
    Tu nombre invertido es {nombre_invertido}
    Tu nombre tiene {n} letras
    La primera letra de su nombre es {letra}
    La ultima letra de tu nombre es {letra}
Si nada fuese digitado en nombre o edad:
    mostrar "Disculpe, es necesario no dejar campos vacios"
"""
nombre = input ('Digita tu nombre: ')
apellido = input('Digite tu apellido: ')
edad = input ('Digita tu edad: ')

if nombre and apellido and edad:
    print(f' Tu nombre es {nombre}')
    print(f' Tu nombre invertido es {nombre [::-1]}')

    if ' ' in nombre and apellido:
        print('Tu nombre contiene espacios')
    else:
        ('Tu nombre no contiene espacios')
        print(f'Tu nombre tiene {len(nombre and apellido)} letras')
        print(f'La primera letra de tu nombre es {nombre[0]}')
        print(f'La primera letra de tu nombre es {apellido[0]}')
        print(f'La ultima letra de tu nombre es {nombre[-1]}')
        print(f'La ultima letra de tu nombre es {apellido[-1]}')

else:
    print('Disculpe pero es necesario rellanar los campos vacios')



