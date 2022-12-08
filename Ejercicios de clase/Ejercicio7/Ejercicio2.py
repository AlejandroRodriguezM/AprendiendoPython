# Define una función que reciba como argumento primero un número seguido de
# una serie de artículos y sus precios (pueden ser los que quieras, pero mínimo 5) y devuelva el
# importe total de cada uno de los artículos por el número de unidades que se haya especificado como
# primer argumento, así como la suma total.

def calcularImporte(unidades, *articulos):
    # array asociativo con el total de cada artículo
    total_articulos = {}
    # recorro el array de articulos
    for i in range(0, len(articulos), 2):
        # calculo el total de cada artículo
        total_articulos[articulos[i]] = articulos[i + 1] * unidades
        # muestro el total de cada artículo
        print("El total de", articulos[i], "es:", total_articulos[articulos[i]], "€")
    # calculo el total de todos los articulos
    total = 0
    for i in total_articulos:
        total += total_articulos[i]
    # muestro el total de todos los articulos
    print("El total de todos los articulos es:", total, "€")


def main():
    articulos = ["libro", 10, "bolígrafo", 2, "cuaderno", 5, "goma", 1, "lapicero", 3]
    numArticulos = 5
    calcularImporte(numArticulos, *articulos)


main()
