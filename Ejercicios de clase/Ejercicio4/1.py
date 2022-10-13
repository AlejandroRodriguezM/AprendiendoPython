# EJERCICIO 1) Escribe una función que devuelva True si el número introducido como parámetro
# es múltiplo de 3 y False en caso contrario. Luego pruébala.
# Por Alejandro Rodriguez Mena

def multiplo(numero):
    if (numero % 3) == 0:
        return True
    else:
        return False


def comprobarNumero():
    while True:
        numero = int(input("Dime un numero: "))
        if multiplo(numero):
            print("El numero", numero, "es multiplo de 3")
            break
        else:
            print("El numero ", numero, "no es multiple de 3 \n")


comprobarNumero()
