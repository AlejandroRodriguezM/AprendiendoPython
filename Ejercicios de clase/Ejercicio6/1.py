# Este programa pedirá al usuario que introduzca veinte números enteros por
# pantalla. Estos números serán guardados en un array de 4 filas y 5 columnas. El resultado del
# programa será mostrar las sumas parciales de las filas y las columnas, como si fuera una hoja de
# cálculo. La suma de todos los números aparecerá en la esquina inferior derecha.


# Funcion que sirve para pedir los numeros
def pedirNumeros():
    try:
        for i in range(4):
            for j in range(5):
                print("Columna:", i+1, "Fila:", j+1)
                array[i][j] = int(input("Introduce un numero: "))
        return array
    except ValueError:
        print("Error. El caracter introducido no es valido.\nDebe de introduce un numero")
        raise SystemExit


# Funcion que suma las filas
def sumaFilas(array):
    for i in range(4):
        for j in range(5):
            suma_filas[i][0] += array[i][j]
    return suma_filas


# Funcion que suma las columnas
def sumaColumnas(array):
    for i in range(5):
        for j in range(4):
            suma_columnas[0][i] += array[j][i]
    return suma_columnas


# Muestro el array
def mostrarArray(array):
    for i in range(4):
        for j in range(6):
            if j == 5:
                suma_filas[i][0] = sumaFilas(array)[i][0]
                print(suma_filas[i][0], end="\t")
            else:
                array[i][j] = pedirNumeros()[i][j]
                print(array[i][j], end="\t")
        print()


# Muestro las sumas de las columnas
def mostrarSumaColumnas():
    for i in range(6):
        if i == 5:
            print(sumaTotal(), end="\t")
        else:
            suma_columnas[0][i] = sumaColumnas(array)[0][i]
            print(suma_columnas[0][i], end="\t")
    print()


# Muestro la suma de todos los números
def sumaTotal():
    suma_total = 0
    for j in range(5):
        for i in range(4):
            suma_total += array[i][j]
            return suma_total


# Creo un array de 4 filas y 5 columnas
array = [[0 for x in range(6)] for y in range(4)]
# Creo un array de 4 filas y 1 columna para guardar las sumas de las filas
suma_filas = [[0] for x in range(4)]
# Creo un array de 1 fila y 5 columnas para guardar las sumas de las columnas
suma_columnas = [[0 for x in range(5)]]


def main():
    mostrarArray(array)
    mostrarSumaColumnas()
    sumaTotal()


# Llamo a la función main
if __name__ == '__main__':
    main()
