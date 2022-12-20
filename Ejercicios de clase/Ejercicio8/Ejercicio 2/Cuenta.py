# ) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es
# una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# • mostrar(): Muestra los datos de la cuenta.
# • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

# importar clase persona.
from Persona import Persona


class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    # get y setters con comprobacion de datos
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor

    @titular.getter
    def titular(self):
        return self.__titular

    @cantidad.getter
    def cantidad(self):
        return self.__cantidad

    # Funcion para ingresar o retirar dinero
    def ingresar(self, cantidad):
        if self.comprobarCantidad():
            self.__cantidad += cantidad
        else:
            print("La cantidad no es valida")

    def retirar(self, cantidad):
        if self.comprobarCantidad():
            if self.__cantidad >= cantidad:
                self.__cantidad -= cantidad
            else:
                print("No hay suficiente dinero en la cuenta")
        else:
            print("La cantidad no es valida")

    # Se comprueba si la cantidad es válida
    def comprobarCantidad(self):
        if self.__cantidad >= 0:
            return True
        else:
            return False

    def totalCantidad(self):
        return self.__cantidad

    # Funcion que muestra los datos de la cuenta
    def mostrar(self):
        print(self.__str__())

    def __str__(self):
        return "Titular: " + self.__titular + "\nCantidad: " + str(self.__cantidad)
