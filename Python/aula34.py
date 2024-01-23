"""
Repeticiones
while (encuanto)
Ejecuta una accion encuanto una condicion fuese verdadera
Loop infinito -> cuando el codigo no tiene fin

"""
condicion = False
while condicion:
       nombre = input('Digita tu nombre: ')
       print(f'Te llamas {nombre} ')
       
       if nombre == 'salir':
           break
print('Saliendo del sistema')

contador = 0

while contador <= 10:
     contador = contador + 1
     print(contador)
   
print('Llegamos al valor maximo')