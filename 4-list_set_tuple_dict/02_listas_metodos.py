#
lista = ["Hola", "Buenos dias", "Como estas", "Buen dia"]
for saludo in lista:
    print(saludo)

#Agregar un elem,en to
lista.append("Buenas tardes")
print(lista)

lista.insert(2, "Buenas noches")
print(lista)

#Eliminar un elemento
lista.remove("Como estas") #el objeto debe existir en la lista
#lista.remove("Que tal")

print(lista)