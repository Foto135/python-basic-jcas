class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class Perro(Animal):
    def ladrar(self):
        print("¡Guau, guau!")

class Gato(Animal):
    def maullar(self):
        print("¡Miau, miau!")

# Crear objetos de las clases derivadas
mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

# Acceder a los métodos de la clase base y las clases derivadas
mi_perro.comer()  # Salida: Firulais está comiendo.
mi_gato.dormir()  # Salida: Michi está durmiendo.
mi_perro.ladrar()  # Salida: ¡Guau, guau!
mi_gato.maullar()  # Salida: ¡Miau, miau!