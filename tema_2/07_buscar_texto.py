texto = "Bienvenidos al curso de Python"
curso_existe = "curso" in texto

posicion_curso = texto.index("curso")
posicion_curso_2 = texto.find("curso")

print(curso_existe)
print(posicion_curso)
print(posicion_curso_2)