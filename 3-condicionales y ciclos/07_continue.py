lista = [1, 2, 3, 4, 5, 6, 7]

indice = -1
while indice < len(lista):
    indice += 1
    if indice == 3:
        continue

    #ESTA LINEA NO SE EJECUTA SI LLAMO, CONTINUE
    print(lista[indice])
