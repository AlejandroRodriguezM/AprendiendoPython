# EJERCICIO 3) Escribe una función que reciba como parámetros una palabra y un carácter y
# devuelva el número de estos que se encuentra en la palabra. Luego pruébala.
# Por Alejandro Rodriguez Mena

def contarPalabras(palabra, caracter):
    try:
        if len(palabra) != 0:
            contadorCaracter = 0
            for i in palabra:
                if i == caracter:
                    contadorCaracter += 1
                    print("Existe ", contadorCaracter, "en la palabra", palabra)
        else:
            raise Exception("ERROR. La palabra introducido esta vacia")
    except Exception as e:
        print(e)
        raise palabras()


def palabras():
    try:
        palabra = input("Dime una palabra: ")
        if len(palabra) != 0:
            caracter = input("Dime un caracter: ")
            if len(caracter) == 1:
                contarPalabras(palabra, caracter)
            else:
                raise Exception("ERROR. Solamente puedes introducir un caracter")
        else:
            raise Exception("ERROR. La palabra introducido esta vacia")
    except Exception as e:
        print(e)
        raise palabras()


palabras()
