# Escribir un programa para el control de una agenda telefónica con los nombres y
# teléfonos de los clientes de una tienda de electrónica.
# El programa tendrá que incorporar funciones
# para crear el fichero con la agenda si no existe, para hacer una consulta sobre el teléfono de un
# cliente, añadir el teléfono de un nuevo cliente y borrar el teléfono de un cliente. La agenda
# telefónica debe estar guardada en el fichero de texto agenda.txt donde el nombre del cliente y su
# teléfono deben aparecer separados por un punto y coma, y cada cliente en una línea distinta.
# Por Alejandro Rodriguez Mena

import os

# Función para crear la agenda si no existe
def crear_agenda():
    if os.path.isfile("agenda.txt"):
        print("El archivo agenda.txt ya existe")
    else:
        with open("agenda.txt", "w") as agenda:
            agenda.write("")
        print("El archivo agenda.txt ha sido creado")


# Función para consultar el teléfono de un cliente
def consultar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    with open("agenda.txt", "r") as agenda:
        for linea in agenda:
            if nombre in linea:
                print(linea)
                return
    print("El cliente no existe")


# Función para añadir el teléfono de un nuevo cliente
def anadir_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    with open("agenda.txt", "a") as agenda:
        agenda.write(nombre + ";" + telefono + " \n")
    print("El cliente ha sido añadido")


# Función para borrar el teléfono de un nuevo cliente
def borrar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    with open("agenda.txt", "r") as agenda:
        lineas = agenda.readlines()
    with open("agenda.txt", "w") as agenda:
        for linea in lineas:
            if nombre not in linea:
                agenda.write(linea)
    print("El cliente ha sido borrado")


# Función para mostrar el menú
def menu():
    print("1. Crear agenda")
    print("2. Consultar teléfono")
    print("3. Añadir teléfono")
    print("4. Borrar teléfono")
    print("5. Salir")
    opcion = int(input("Introduce una opción: "))
    return opcion


# Función principal
def main():
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            crear_agenda()
        elif opcion == 2:
            consultar_telefono()
        elif opcion == 3:
            anadir_telefono()
        elif opcion == 4:
            borrar_telefono()
        opcion = menu()


main()
