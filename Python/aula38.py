"""
Repeticiones
while (encuanto)
Ejecuta una accion encuanto una condicion es verdadera
Loop infinito -> cuando un codigo no tiene fin

"""

qtd_lineas = 5
qtd_columnas = 5

linea = 1
while linea <= qtd_lineas:
    columnas = 1
    while columnas <= qtd_columnas:
        print(f'{linea = }, {columnas = }')
        columnas += 1
    linea += 1
print ('acabo')