lista = [7, 3, 9, 0, 2, 1]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#eliminar un elemento
elemento = lista.pop()
print(elemento)
print(lista)

lista.pop(1)
print(lista)