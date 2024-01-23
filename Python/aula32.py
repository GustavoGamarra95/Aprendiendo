"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""
# entrada = input('Digite un numero par: ')
# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'El valor digitado {entrada_int} es {par_impar_texto}')
# else:
#     print('El valor digitado es impar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input ('Me podrias informar la hora?: ')
# try:  
#     horario = int (horario)

#     if horario >= 0 and horario <= 11:
#         print('Buen dia')
#     elif horario >= 12 and horario <= 17:
#         print('Buenas tardes')

#     elif horario >= 18 and horario <= 23:
#         print('Buenas noches')
        
#     else:
#         print('No conozco ese horario')
        
# except: 
#     print('Por favor informe del horario verdadero: ')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input ('Digita tu nombre: ')
tamanho_nombre = len(nome)
if tamanho_nombre > 1:
    if tamanho_nombre <= 4:
        print('Tu nombre es corto')
    elif tamanho_nombre >= 5 and tamanho_nombre <= 6:  
        print('Tu nombre es normal')
    else:
        print('Tu nombre es muy grande')

else: 
    print('Por favor, digita mas de una letra.')