class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    # SETTERS
    @nombre.setter
    def nombre(self, valor):
        if valor.isalpha():
            self.__nombre = valor
        else:
            print("El nombre no puede contener números ni caracteres especiales ni espacios")
            self.__nombre = ""

    @edad.setter
    def edad(self, valor):
        if str(valor).isnumeric():  # edad tiene que ser numérica
            self.__edad = valor
        else:
            print("La edad debe ser numérica")
            self.__edad = 0

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI
        self.verificarDNI()

    # GETTERS
    @nombre.getter
    def nombre(self):
        return self.__nombre

    @edad.getter
    def edad(self):
        return self.__edad

    @DNI.getter
    def DNI(self):
        return self.__DNI

    # Funcion que muestra los datos de la persona
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI)

    # Funcion que comprueba si la persona es mayor de edad
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    # verificar si el DNI es correcto
    def verificarDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__DNI) != 9:
            print("DNI incorrecto")
            self.__DNI = "N/A"
        else:
            letra = self.__DNI[8]
            num = int(self.__DNI[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__DNI = "N/A"
