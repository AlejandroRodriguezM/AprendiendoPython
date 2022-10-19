# EJERCICIO 1) Este ejercicio consta de varias partes:
# 1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”,
# “get_edad” y “print_persona”. Luego generar dos objetos del tipo Persona e imprimirlos.
# 2. Agregarle a la clase anterior un constructor que reciba nombre y edad.
# 3. Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
# 4. Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad
# con la del objeto actual.
# 5. Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de
# edad mayor.
# Por Alejandro Rodriguez Mena
class Persona:
    # Atributos
    nombre = ""
    edad = 0

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodos get y set
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    # Metodo para imprimir datos del objeto persona
    def printPersona(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    # Metodo que devuelve un booleano segun la edad de objeto
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    # Metodo que compara la edad 2 objetos y devuelve un booleano segun la edad
    def es_mayor_que(self, persona):
        if self.edad > persona.edad:
            return True
        else:
            return False

    # Metodo estatico que compara la edad 2 objetos y devuelve el objeto con mayor edad
    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.edad > persona2.edad:
            return persona1
        else:
            return persona2
