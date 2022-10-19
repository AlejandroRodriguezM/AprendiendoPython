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

from Persona import Persona

persona1 = Persona("Alejandro", 29)
persona2 = Persona("Paco", 35)

persona1.printPersona()
persona2.printPersona()

if persona1.es_mayor_que(persona2):
    print(persona1.get_nombre(), "es mayor que", persona2.get_nombre())
else:
    print(persona2.get_nombre(), "es mayor que", persona1.get_nombre())

if Persona.get_mayor(persona1, persona2):
    if persona1.es_mayor_que(persona2):
        print(persona1.printPersona())
    else:
        print(persona2.printPersona())
