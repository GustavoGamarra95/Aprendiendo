
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito


entrada = input ( '[E]ntrar [S]alir: ')
password_digitado= input ('Password: ')

password_permitida = '123456'


#if condicion solo ejecuta si la expresion es True


if 'E' in entrada and password_digitado == password_permitida:
    print('Entrar')
else:
    salida = 'S'
print('Salir')

#avaliacion de corto circuito

print(True and True and True)
print(True and False and True)

if 0 and 1:
    print(True and 1)

if 1 and 1:
    print( True and 1 and False)