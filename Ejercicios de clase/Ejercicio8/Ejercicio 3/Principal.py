# EJERCICIO 3) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
# clase CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la
# cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los
# siguientes métodos para la clase:
# • Un constructor.
# • Los setters y getters para el nuevo atributo.
# • En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo
# tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# • Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# • El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir
from CuentaJoven import *
from Cuenta import *
from Persona import *

# Se crea un objeto de la clase Persona
persona1 = Persona("Marta", 15, "44544565M")
cuenta1 = Cuenta(persona1.nombre, 0)
cuentaJoven1 = CuentaJoven(persona1.nombre, persona1.edad, 0, 5)

persona2 = Persona("Juan", 20, "44594146K")
cuenta2 = Cuenta(persona2.nombre, 0)
cuentaJoven2 = CuentaJoven(persona2.nombre, persona2.edad, 0, 5)

persona3 = Persona("Pedro", 35, "25606812S")
cuenta3 = Cuenta(persona3.nombre, 0)
cuentaJoven3 = CuentaJoven(persona3.nombre, persona3.edad, 0, 5)

# mostrar cuenta menor de edad sin modificar
print("Cuenta menor de edad sin modificar")
cuentaJoven1.mostrar()

# ingresar dinero en cuenta menor de edad
print("\nCuenta menor de edad ingresar 100 euros")
cuentaJoven1.ingresar(100)
cuentaJoven1.mostrar()

# retirar dinero en cuenta menor de edad
print("\nCuenta menor de edad retirar 50 euros")
cuentaJoven1.retirar(50)

# mostrar cuenta mayor de edad sin modificar
print("\nCuenta mayor de edad sin modificar")
cuentaJoven2.mostrar()

# ingresar dinero en cuenta mayor de edad
print("\nCuenta mayor de edad con 100 euros")
cuentaJoven2.ingresar(100)
cuentaJoven2.mostrar()

# retirar dinero en cuenta mayor de edad
print("\nCuenta mayor de edad retirar 50 euros")
cuentaJoven2.retirar(50)
cuentaJoven2.mostrar()

# mostrar cuenta mayor de 25 sin modificar
print("\nCuenta mayor de 25 sin modificar")
cuentaJoven3.mostrar()

# ingresar dinero en cuenta mayor de 25
print("\nCuenta mayor de 25 con 100 euros")
cuentaJoven3.ingresar(100)
cuentaJoven3.mostrar()

# retirar dinero en cuenta mayor de 25
print("\nCuenta mayor de 25 retirar 50 euros")
cuentaJoven3.retirar(50)
cuentaJoven3.mostrar()






