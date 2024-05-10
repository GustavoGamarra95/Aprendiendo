"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os 

palabra_secreta = 'Uniamerica'
letras_correctas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite una letra: ')
    numero_tentativas += 1
    if len(letra_digitada)> 1:
        print('Digite apenas una letra.')
        continue

    if palabra_secreta in palabra_secreta:
        letras_correctas += letra_digitada

    palabra_formada = ''
    for letra_secreta in palabra_secreta:
        if letra_secreta in letras_correctas:
            palabra_formada += letra_secreta
        else:
            palabra_formada += '*'
    
    print('palabra_formada:', palabra_formada)

    if palabra_formada == palabra_secreta:
        os.system('clear')
        print ('Descubriste la palabra oculta!!!, Felicidades!!!')
        print('Tentativas', numero_tentativas)
        numero_tentativas = 0
        letra_secreta = ''