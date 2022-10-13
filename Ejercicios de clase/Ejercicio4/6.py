# Escribe una función que devuelva una lista que será el resultado de aplicar la
# función que tiene como parámetro a la lista que también tiene como parámetro.
# Por Alejandro Rodriguez Mena..

def aplicarFuncion(listaNumeros, funcion):
    try:
        if len(listaNumeros) != 0:
            listaResultado = []
            for i in listaNumeros:
                listaResultado.append(funcion(i))
            print("La lista original es:",listaNumeros)
            print("Aplicada la funcion es:",listaResultado)
        else:
            raise ValueError("ERROR. La lista introducida esta vacia")
    except ValueError as e:
        print(e)
        raise aplicarFuncion()


def lista():
    try:
        listaNumeros = []
        for i in range(5):
            numero = int(input("Dime un numero: "))
            listaNumeros.append(numero)
        sumaLista()
        aplicarFuncion(listaNumeros, sumaLista())
    except ValueError as e:
        print(e)
        raise lista()


def sumaLista():
    suma = lambda x: x + 10
    return suma


lista()
