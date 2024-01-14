
'''
Ejercicio de comparacion con If
'''
primer_valor = input('Digite un valor: ')
segundo_valor = input('Digite un segundo valor: ')

if primer_valor >=  segundo_valor:
    print(
        f'{primer_valor =} es mayor o igual' 
        f'al valor de {segundo_valor = }'
    )
else:
    print(
        f'{segundo_valor = } es mayor o igual'
        f'al valor de {primer_valor} '
    )