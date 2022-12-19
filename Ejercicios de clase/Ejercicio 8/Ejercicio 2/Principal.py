# import clase persona y clase cuenta

from Persona import Persona
from Cuenta import Cuenta

# creamos un objeto persona

persona1 = Persona("Juan", 25, "12345678A")

# creamos un objeto cuenta

cuenta1 = Cuenta(persona1, 1000)

# mostramos los datos de la cuenta

cuenta1.mostrar()

# ingresamos 500

cuenta1.ingresar(500)

# mostramos los datos de la cuenta

cuenta1.mostrar()

# retiramos 2000

cuenta1.retirar(2000)

# mostramos los datos de la cuenta

cuenta1.mostrar()

# retiramos 500

cuenta1.retirar(500)

# mostramos los datos de la cuenta

cuenta1.mostrar()








