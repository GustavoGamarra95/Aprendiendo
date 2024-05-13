"""
Tipo tupla - Una lista inmutable
"""
nomes = [ 'Maria', 'Helena', 'Luiz']
nomes[1] = 'outro'
_, _, nome, *resto = nomes
print(nomes)
print(nome)


