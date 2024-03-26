'''
Iteravel -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> entrega el proximo valor
iter -> entrega el iterador
'''

texto = 'Gustavo' #iterable

iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
