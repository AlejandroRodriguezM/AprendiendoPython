class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI)

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
