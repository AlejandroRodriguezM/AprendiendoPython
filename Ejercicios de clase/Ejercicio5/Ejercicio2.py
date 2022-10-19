# Escribir una función que pida un número entero entre 1 y 10 y guarde en un
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número
# introducido.
# Por Alejandro Rodriguez Mena

# Funcion que pide un número entero entre 1 y 10
def tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    if numero > 0 and numero < 11:
        with open("tabla-" + str(numero) + ".txt", "w") as tabla:
            for i in range(1, 11):
                tabla.write(str(numero) + " x " + str(i) + " = " + str(numero * i) + " \n")
    else:
        print("El número introducido no está entre 1 y 10")


tabla_multiplicar()

