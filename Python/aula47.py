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

palabra_secreta = 'Uniamerica'
letras_correctas = ''
while True:
    letra_digitada = input('Digite una letra: ')
    if len(letra_digitada)> 1:
        print('Digite apenas una letra.')
        continue
   
    if palabra_secreta in palabra_secreta:
        letras_correctas += letra_digitada
        print(letras_correctas)