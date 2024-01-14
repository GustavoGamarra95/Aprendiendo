"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nombre = 'Gustavo'
precio = 1995.655555
variavel = ' %s el precio es %.2f' % (nombre, precio)
print(variavel) 
print('El hexadecimal de un numero es %d es %04x' % (1500, 1500))