# EJERCICIO 2) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
# una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# • mostrar(): Muestra los datos de la cuenta.
# • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos
from Cuenta import *
from Persona import *

# Se crea un objeto de la clase Persona
persona = Persona("Marta", 15, "44544565M")
cuenta = Cuenta(persona.nombre, 0)

# Se muestra la cuenta
print("cuenta")
cuenta.mostrar()

# Se ingresa dinero
print("\nSe ingresa 100")
cuenta.ingresar(100)
cuenta.mostrar()

# Se retira dinero
print("\nSe retira 50")
cuenta.retirar(50)
cuenta.mostrar()

# Se retira dinero
print("\nSe retira 100")
cuenta.retirar(100)
cuenta.mostrar()






