texto = "Buenos dias Curso"
for caracter in texto:
    if caracter == "o":
        break

    print(caracter)

indice = 0
caracter = texto[indice] # B
while caracter != " ":
    indice += 1
    print(caracter)
    caracter = texto[indice]

    if caracter == "o":
        break
