# Ejercicio 5 Por Alejandro Rodriguez Mena

nombre = input("Introduce un nombre: ")
apellido = input("Introduce un apellido: ")
diccionario = {nombre: apellido}

while True:
    print(diccionario)
    ordenar = input("¿Quieres ordenar el diccionario? (s/n): ")
    if ordenar == "s":
        orden = input("¿Quieres ordenarlo por nombre o por apellido? (n/a): ")
        if orden == "n":
            print(sorted(diccionario))
            salir = input("¿Quieres salir del programa? (s/n): ")
            if salir == "s":
                nombre = input("Introduce un nombre: ")
                apellido = input("Introduce un apellido: ")
                diccionario = {nombre: apellido}
            else:
                print("Gracias por usar el programa")
                break
        elif orden == "a":
            print(sorted(diccionario.values()))
            salir = input("¿Quieres salir del programa? (s/n): ")
            if salir == "n":
                nombre = input("Introduce un nombre: ")
                apellido = input("Introduce un apellido: ")
                diccionario = {nombre: apellido}
            else:
                print("Gracias por usar el programa")
                break
    elif ordenar == "n":
        salir = input("¿Quieres salir del programa? (s/n): ")
        if salir == "n":
            nombre = input("Introduce un nombre: ")
            apellido = input("Introduce un apellido: ")
            diccionario = {nombre: apellido}
        else:
            print("Gracias por usar el programa")
            break
