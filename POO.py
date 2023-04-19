# Definimos la clase Animal con atributos y métodos
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def hacer_sonido(self):
        pass

# Definimos la clase Perro que hereda de Animal y sobrescribe el método hacer_sonido
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Definimos la clase Gato que hereda de Animal y sobrescribe el método hacer_sonido
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Creamos instancias de las clases Perro y Gato
mi_perro = Perro("Fido", 3)
mi_gato = Gato("Luna", 5)

# Accedemos a los atributos y métodos de las instancias
print(mi_perro.get_nombre()) # Output: Fido
print(mi_gato.get_edad()) # Output: 5
print(mi_perro.hacer_sonido()) # Output: Guau
print(mi_gato.hacer_sonido()) # Output: Miau