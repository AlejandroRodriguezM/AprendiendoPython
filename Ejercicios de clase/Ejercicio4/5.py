# EJERCICIO 5) Escribe dos funciones. Una que dado un número en decimal devuelva este número
# en binario y otra que haga justo lo contrario.
# Por Alejandro Rodriguez Mena

def decimalBinario(numeroIntroducido):
    try:
        if numeroIntroducido >= 0:
            numeroBinario = bin(numeroIntroducido)
            print(numeroBinario)
            binarioDecimal(numeroBinario)
        else:
            raise ValueError("ERROR. El numero introducido es negativo")
    except ValueError as e:
        print(e)
        raise decimalBinario()


def binarioDecimal(numeroBinario):
    try:
        if int(numeroBinario, 2) >= 0:
            numeroDecimal = int(numeroBinario, 2)
            print(numeroDecimal)
        else:
            raise ValueError("ERROR. El numero introducido es negativo")
    except ValueError as e:
        print(e)
        raise binarioDecimal()


def numero():
    try:
        numeroIntroducido = int(input("Dime un numero: "))
        decimalBinario(numeroIntroducido)

    except ValueError as e:
        print(e)
        raise numero()


numero()
