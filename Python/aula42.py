frase = 'Python es un lenguaje de programacion'\
    'multiparadigma. '\
    'Python fue creado por Guido vn Rossum'
i = 0
ctd_mas_veces = 0
letra_aparecio_mas_veces = ''
while i < len(frase):
    letra_actual = frase[i]
    if letra_actual == '':
         i += 1
         continue

    cantidad_de_letras = frase.count(letra_actual)
    if ctd_mas_veces < letra_aparecio_mas_vecess:
        letra_aparecio_mas_veces = cantidad_de_letras
        ctd_mas_veces = letra_aparecio_mas_veces


print(
        'La letra que aparecio mas veces es'
        f'{letra_aparecio_mas_veces} que aparecio'
        f'{ctd_mas_veces} veces.'
    )