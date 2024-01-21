"""
Introduccion a try/except
try -> ejecutar el codigo
except -> ocurrio algun error en el codigo

"""
# print(1234)
# print(456)
# int('a')

numero_str =  input('Puedo doblar el numero que coloques: ')
try:
   print('STR:', numero_str)
   numero_float = float(numero_str)
   print('Float:', numero_float)
   print(f'El doble de {numero_str} es {numero_float *2:.0f}')

except:
     print('Ese dato no es un numero')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'El doble de {numero_str} es {numero_float *2:.0f}')
# else:
#     print('Ese dato no es un numero')