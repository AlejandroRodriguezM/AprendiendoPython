# EJERCICIO 4) Escribe programa que vaya pidiendo por pantalla al usuario una palabra en español
# y la misma en inglés. Esto lo irá añadiendo a un diccionario. Una vez introducidas todas las
# palabras le pediremos al usuario que introduzca una frase y deberá devolvernos la traducción
# completa de la frase (si alguna palabra no está en el diccionario la dejará sin traducir)
# Por Alejandro Rodriguez Mena

def traducir(frase, diccionario):
    try:
        if len(frase) != 0:
            frase = frase.split()
            for i in frase:
                if i in diccionario:
                    print(diccionario[i], end=" ")
                else:
                    print(i, end=" ")
        else:
            raise ValueError("ERROR. La frase introducida esta vacia")
    except ValueError as e:
        print(e)
        raise traducir()


def palabras():
    try:
        diccionario = {}
        while True:
            palabra = input("Dime una palabra en español: ")
            if len(palabra) != 0:
                palabraIngles = input("Dime la palabra en ingles: ")
                if len(palabraIngles) != 0:
                    diccionario[palabra] = palabraIngles
                else:
                    raise ValueError("ERROR. La palabra introducida esta vacia")
            else:
                break
        frase = input("Dime una frase: ")
        traducir(frase, diccionario)
    except ValueError as e:
        print(e)
        raise palabras()


palabras()



