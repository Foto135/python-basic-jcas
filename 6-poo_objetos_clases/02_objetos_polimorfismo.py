class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau, miau!"

# Función que hace sonar a un animal
def hacer_sonar(animal):
    print(animal.hacer_sonido())

# Crear objetos de las clases derivadas
mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

# Llamar a la función con diferentes objetos
hacer_sonar(mi_perro)  # Salida: ¡Guau, guau!
hacer_sonar(mi_gato)  # Salida: ¡Miau, miau!