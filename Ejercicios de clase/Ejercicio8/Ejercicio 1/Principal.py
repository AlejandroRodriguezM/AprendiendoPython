# EJERCICIO 1) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# • mostrar(): Muestra los datos de la persona.
# • esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
from Persona import *

persona = Persona("Juan", 20, "12345678A")
persona.mostrar()
persona.esMayorDeEdad()

print()

persona2 = Persona("Marta", 15, "44544565M")
persona2.mostrar()
persona2.esMayorDeEdad()








