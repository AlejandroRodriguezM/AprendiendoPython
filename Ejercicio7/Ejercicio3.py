# Define una función recursiva que reciba como argumento una frase y devuelva la
# misma frase con las palabras en orden inverso.

def invertirPalabras(frase):
    if len(frase) == 1:
        return frase[0]
    else:
        return frase[-1] + " " + invertirPalabras(frase[:-1])


def main():
    frase = "Hola mundo, esto es un programa"
    print(invertirPalabras(frase.split(" ")))


main()