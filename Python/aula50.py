"""
EJERCICIO
exibir los indices de la lista
0 Maria
1 Helena
2 Luiz
"""

nombres = ["Maria", "Helena", "Luiz"]
# for i in range(len(nombres)):
#     indice = nombres.index(nombres[i])
#     print(f"Indice: {indice}, Nombre: {nombres[i]}")
indices = range(len(nombres))
for indice in indices:
    print(indice, nombres[indice], type(nombres[indice]))