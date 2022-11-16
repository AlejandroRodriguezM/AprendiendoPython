# Este programa pedirá al usuario que introduzca veinte números enteros por
# pantalla. Estos números serán guardados en un array de 4 filas y 5 columnas. El resultado del
# programa será mostrar las sumas parciales de las filas y las columnas, como si fuera una hoja de
# cálculo. La suma de todos los números aparecerá en la esquina inferior derecha.

# Funcion que sirve para pedir los numeros
def pedirNumeros():
    global array
    try:
        for i in range(4):
            for j in range(5):
                print("Columna:", (i + 1), "Fila:", (j + 1))
                array[i][j] = int(input("Introduce un numero: "))
        return array
    except ValueError:
        print("Error. El caracter introducido no es valido.\nDebe de introduce un numero")
        raise SystemExit


# Funcion que suma las filas devuelve el valor de cada fila individualmente
def sumaFilas(array):
    for i in range(4):
        suma = 0
        for j in range(5):
            suma += array[i][j]
    print(suma, end="\t")


# Funcion que suma las columnas
def sumaColumnas(array):
    for i in range(5):
        suma = 0
        for j in range(4):
            suma += array[j][i]
    print(suma, end="\t")


# Muestro el array
def mostrarArray(array):
    for i in range(4):
        for j in range(5):
            print(array[i][j], end="\t")
        sumaFilas(array)
        print()


# Muestro las sumas de las columnas
def mostrarSumaColumnas(array):
    suma = 0
    for i in range(5):
        total_columnas = 0
        for j in range(4):
            total_columnas += array[j][i]
            suma += array[j][i]

        print(total_columnas, end="\t")
    print(suma, end="\t")
    print()


# Muestro la suma de todos los números
def sumaTotal():
    suma_total = 0
    for j in range(5):
        for i in range(4):
            suma_total += array[i][j]
            return suma_total


# Creo un array de 4 filas y 5 columnas
array = [[0 for x in range(5)] for y in range(4)]
# Creo un array de 4 filas y 1 columna para guardar las sumas de las filas
suma_filas = [[0] for x in range(4)]
# Creo un array de 1 fila y 5 columnas para guardar las sumas de las columnas
suma_columnas = [[0 for x in range(5)]]


def main():
    pedirNumeros()
    mostrarArray(array)
    mostrarSumaColumnas(array)
    sumaTotal()


# Llamo a la función main
if __name__ == '__main__':
    main()
