diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
    }
}

for llave, valor in diccionario1.items():
    print(llave, ":", valor)