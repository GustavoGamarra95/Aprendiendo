''' texto = 'Python'
i = 0  
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1 ''' 
''' senha_salva = '1234'
senha_digitada = ''
repeticiones = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticiones}s): ')
    repeticiones += 1

print(repeticiones)
print('O laço acima pode ter repeticoes infinitas')
'''

texto = 'Phyton'

for letra in texto:
    print(letra)