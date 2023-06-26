diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
    }
}

print(diccionario1["Profesion"])
print(diccionario1.get("Edad"))

diccionario1["Profesion"] = "Medico"
diccionario1["Ciudad"] = "Bogota"

print(diccionario1)