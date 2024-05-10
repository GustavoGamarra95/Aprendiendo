"""
Listas en Python 
Tipo List - Mutable
Soporta varios valores de cualquier tipo
Conocimientos reutilizables - indice y porcionamiento
medotos utiles: append, insert, pop, del, clear, extend, + -  cadena de listas
crear, lee, alterar, borar = lista[i] CRUD
"""

#......................01234
#.....................-54321
# import os
# string = 'ABCDE' #5caracteres
# lista = [123, True, 'Gustavo', 1.2,[]] # ''
# os.system('clear')

# lista[2] = 300
# del lista[2]
# print (lista)
# print(lista[2])
# lista.append(50,)
# lista.append(60,)
# lista.append(70,)
# ultimo_valor = lista.pop(3)
# print (lista, 'removido', ultimo_valor)

#print(bool(lista)) # false
#print(lista, type(lista))
# print(lista)
# lista = [10, 20, 30, 40]
# lista.append('Gustavo')
# nome = lista.pop()
# lista.append(1233)
# del lista [-1]
# # lista.clear()
# lista.insert(0, 5)
# print(lista)
# lista_a =[1,2,3]
# lista_b= [4,5,6]
# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
# print(lista_c)

"""
Cuidados con datos mutables
= - copiado o valor (inmutables)    
= - apunta para el mismo valor de la memoria (mutable)
"""
# nombre = 'Gustavo'
# notro_variable = nombre
# nombre = 'Ariel'
# print (nombre)
# print (notro_variable)
lista_a = ['gustavo', 'alicia']
lista_b = lista_a

lista_a[0] = 'cualquier cosa'
print(lista_a)
print(lista_b)














 