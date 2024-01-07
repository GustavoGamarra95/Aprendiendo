#Fstrings

nombre = 'Gustavo'
altura = 1.90
peso = 135
imc = peso / (altura**2)


linea_1 = f'{nombre} tiene {altura:.2f} de altura, pesa {peso} kilos y su IMC es {imc:.2f}'
linea_2 = f'pesa {peso} kilos y su IMC es {imc:.2f}'
linea_3 = f'{imc:.2f}'
print (linea_1)
print (linea_2)
print (linea_3)


# print(linea_1)
# print('pesa', peso, 'quilos y su IMC es',)
# print(imc)