
'''
Indices pueden ser usadas de forma repetida dentro de las funciones
Es mas recomendado utilizar parametros nominados
todo lo que viene despues de un parametro nominado deve ser nominado
'''
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome2} b={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3= c
)

print (formato)