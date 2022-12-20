from Cuenta import *


class CuentaJoven(Cuenta, Persona):
    def __init__(self, titular, edad, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.edad = edad
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @property
    def edad(self):
        return self.__dad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @bonificacion.setter
    def bonificacion(self, valor):
        self.__bonificacion = valor

    @bonificacion.getter
    def bonificacion(self):
        return self.__bonificacion

    @edad.getter
    def edad(self):
        return self.__edad

    # esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    def esTitularValido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False



    def retirar(self, cantidad):
        if self.esTitularValido():
            if cantidad <= self.cantidad:
                self.cantidad = self.cantidad - cantidad
                print("Retirada realizada con éxito")
            else:
                print("No se puede retirar esa cantidad")
        else:
            print("No se puede retirar dinero")

    def mostrar(self):
        print("Titular: ", self.titular)
        print("Edad: ", self.edad)
        print("Cantidad: ", self.cantidad)
        print("Bonificación: ", self.bonificacion, "%")
