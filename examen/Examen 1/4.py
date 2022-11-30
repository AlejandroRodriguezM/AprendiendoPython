# Ejercicio 4 Por Alejandro Rodriguez Mena
import random

numAleatorio = random.randint(1000, 9999)

numUsuario = int(input("Introduce un numero de 4 cifras: "))

while True:
    print("Este es el numero secreto, para tenerlo como referencia: ",numAleatorio) #Servira como referencia para adivinar el numero
    if numUsuario == numAleatorio:
        print("Felicidades, has acertado")
        volverAJugar = input("¿Quieres volver a jugar? (s/n): ")
        if volverAJugar == "s":
            numAleatorio = random.randint(1000, 9999) # Se crea otro numero aleatorio para empezar a jugar de nuevo
            print(numAleatorio)
            numUsuario = int(input("Introduce un numero de 4 cifras: "))
        else:
            print("Gracias por jugar")
            break
    else:
        print("Lo siento, has fallado")
        numAleatorio = str(numAleatorio)
        numUsuario = str(numUsuario)
        for i in range(0, 4):
            #comprueba cuantos numeros si existen en la clave PD: No he logrado que se muestren todos los numeros que si estan, solamente el 1º numeros
            if numUsuario[i] in numAleatorio[i]:
                print("El numero", numUsuario[i], "si existe en la clave")
                break
        numUsuario = int(input("Introduce un numero de 4 cifras: "))

