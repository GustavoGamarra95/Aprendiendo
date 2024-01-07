#Funcion Input
'''
sirve para colectar informaciones
es mejor colocar dentro de una nueva variable los numeros a ser ingresados 
de desta forma las lineas del codigo no se corrompen al momento de colocar un caracter especial
'''
# nombre = input('Cual es tu nombre?' )
numero_1 = input('Digite un numero: ')
numero_2 = input('Digite otro numero: ')
int_numero_1 = int(numero_1)
int_numero_2 = int (numero_2)

print(f'La suma de los numeros es: {int_numero_1 + int_numero_2 }')