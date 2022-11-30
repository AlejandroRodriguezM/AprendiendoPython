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
def sumaFilas(suma_filas):
    global sumaFilaColumna
    suma = 0
    for i in range(5):
        suma += suma_filas[i]
        sumaFilaColumna += suma_filas[i]
    return suma


# Funcion que suma las columnas
def sumaColumnas(array,suma_filas):
    global sumaFilaColumna
    for i in range(5):
        suma = 0
        for j in range(4):
            suma += array[j][i]
            sumaFilaColumna += array[j][i]
    return sumaFilas(suma_filas + suma)


# Muestro el array
def mostrarArray(array):
    for i in range(4):
        for j in range(5):
            print(array[i][j], end="\t")
        print("|",sumaFilas(array[i]), end="\t")
        print()
    print("-----------------------")



# Muestro las sumas de las columnas
def mostrarSumaColumnas(array):
    suma = 0
    for i in range(5):
        total_columnas = 0
        for j in range(4):
            total_columnas += array[j][i]
            suma += array[j][i]

        print(total_columnas, end="\t")
    sumaTotal()
    print()


# Muestro la suma de todos los resultados de las sumas de las columnas y filas
def sumaTotal():
    suma = 0
    for i in range(4):
        for j in range(5):
            suma += array[i][j]  + array[i][j]
    print("|",suma, end="\t")


# Creo un array de 4 filas y 5 columnas
array = [[0 for x in range(5)] for y in range(4)]
# Creo un array de 4 filas y 1 columna para guardar las sumas de las filas
suma_filas = [[0] for x in range(4)]

sumaFilaColumna = 0


def main():
    pedirNumeros()
    mostrarArray(array)
    mostrarSumaColumnas(array)


# Llamo a la función main
if __name__ == '__main__':
    main()
