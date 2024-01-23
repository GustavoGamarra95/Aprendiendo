"""
Flag - Marca un local
None = Ningun Valor
is y is not = es o no es (tipo, valor, identidad)
id = identidad
"""

# v1 = 'a'
# v2 = 'b'
# print(id (v1))
# print(id (v2))

condicion = True
passou_no_if = None

if condicion:
    passou_no_if = True
    print('Y si haces algo?')
else:
    passou_no_if = None
    print('No hagas nada')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)