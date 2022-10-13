# EJERCICIO 7) Escribe una función que dada una altura que introduzca el usuario, devuelva un
# arbol de navidad hecho con “*” de la altura dada.
# Por Alejandro Rodriguez Mena

def arbolNavidad(altura):
    try:
        if altura > 0:
            for i in range(altura):
                print(" " * (altura - i - 1) + "*" * (2 * i + 1))
        else:
            raise ValueError("ERROR. La altura introducida es negativa")
    except ValueError as e:
        print(e)
        raise arbolNavidad()


def alturaArbol():
    try:
        altura = int(input("Dime la altura del arbol: "))
        if altura > 0:
            arbolNavidad(altura)
        else:
            raise ValueError("ERROR. La altura introducida es negativa")
    except ValueError as e:
        print(e)
        raise alturaArbol()


alturaArbol()