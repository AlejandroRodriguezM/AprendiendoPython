# EJERCICIO 4) Dado un número máximo que se pedirá al usuario, devolver por pantalla todos los
# números primos hasta este número máximo, en una lista.
# Por Alejandro Rodriguez Mena

# Funcion que devuelve true en caso de que el numero como parametro sea primo del numero introducido por pantalla
def numprimo(num):
    for i in range(2, num):
        if num % i != 0:
            return True
        return False


# Funcion que devuelve un array con el contenido de los numeros primos de 2 hasta el numero escrito por pantalla
def listaprimo(num):
    listanum = []
    for i in range(2, num):
        if numprimo(i):
            listanum.append(i)
    return listanum


# Funcion principal donde se pedira un numero y devolvera como mensaje, un array con los numeros primos
def main():
    numero = int(input("Dime un numero: "))
    print(listaprimo(numero))


# Llamada al metodo main
if __name__ == '__main__':
    main()
