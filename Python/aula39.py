''''
Iteraccion de strings con while

'''
nombre = 'Gustavo'
indice = 0 
nuevo_nombre = ''
while indice < len(nombre):
    letra = nombre[indice]
    nuevo_nombre += f'*{letra}'
    indice += 1

print(nuevo_nombre)