contador = 0
while contador <= 100:
    contador += 1
    if contador == 6:
        print('No voy a mostrar el numero 6')
        continue
    if contador >= 10 and contador <= 27:
        print('No voy a mostrar el numero', contador)
        continue
    print(contador)

    if contador == 40:
        break
