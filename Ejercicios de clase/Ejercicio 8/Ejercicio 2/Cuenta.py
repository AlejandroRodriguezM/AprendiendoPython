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
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def set_titular(self, titular):
        self.titular = titular

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar(self):
        print(f"El titular es: {self.titular}, y la cantidad es: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print("Ingreso realizado con éxito")
        else:
            print("No se puede ingresar una cantidad negativa")

    def retirar(self, cantidad):
        if self.cantidad - cantidad < 0:
            print("No se puede retirar esa cantidad")
        else:
            self.cantidad -= cantidad

