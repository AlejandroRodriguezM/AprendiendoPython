from Persona import *

persona1 = Persona("Juan", 20, "12345678A")
persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad\n")
else:
    print("No es mayor de edad\n")

persona2 = Persona("Ana", 15, "87654321B")
persona2.mostrar()
if persona2.esMayorDeEdad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")






