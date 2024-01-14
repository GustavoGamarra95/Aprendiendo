# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  G u s t a v o
# -6-5-4-3-2-1
'''nome = 'Gustavo'
print(nome[2])
print(nome[-4])
print('avo' in nome)
print('Us' in nome) 
print(10 * '-')
print('avo' not in nome)
print('zero' not in nome)
'''

nombre = input ('Digita tu nombre: ')
encontrar = input ('Digite las letras que buscas en tu Nombre y Apellido =): ')

if encontrar in nombre:
    print(f'{encontrar } esta en el Nombre')

else:
    print (f'{encontrar} no se encuentra en {nombre}')


