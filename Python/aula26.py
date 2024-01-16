"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variable = 'abc'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}')
print(f'{variable: ^10}')
print (f'{1000.4875645:0>+10,.1f}')
print(f'El hexadecimal de 1500 es {1500:08x}')
print(f'{variable!r}')





