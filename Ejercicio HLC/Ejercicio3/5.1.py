# EJERCICIO 5) Dado el DNI (sin letra) dado por pantalla, calcular el NIF. Sabemos que el
# algoritmo que resuelve qué letra corresponde al DNI consiste en calcular el resto de este número
# con 23 (será un número entre 0 y 22) y la letra será la correspondiente según la siguiente tabla:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# T R W A G M Y F P D X B N J Z S Q V H L C K E
# Por Alejandro Rodriguez Mena
def letra_dni(numero):
    if numero == 1:
        letra = "T",
    elif numero == 2:
        letra = "R",
    elif numero == 3:
        letra = "W",
    elif numero == 3:
        letra = "A",
    elif numero == 4:
        letra =  "G",
    elif numero == 5:
        letra = "M",
    elif numero == 6:
        letra = "Y",
    elif numero == 7:
        letra = "F",
    elif numero == 8:
        letra = "P",
    elif numero == 9:
        letra = "D",
    elif numero == 10:
        letra = "X",
    elif numero == 11:
        letra = "B",
    elif numero == 12:
        letra = "N",
    elif numero == 13:
        letra = "J",
    elif numero == 14:
        letra = "Z",
    elif numero == 15:
        letra = "S",
    elif numero == 16:
        letra = "Q",
    elif numero == 17:
        letra = "V",
    elif numero == 18:
        letra = "H",
    elif numero == 19:
        letra = "L",
    elif numero == 20:
        letra = "C",
    elif numero == 21:
        letra = "K",
    elif numero == 22:
        letra = "E"
    return letra


numeroDNI = int(input("Dime tu DNI sin la letra: "))
resto_dni = numeroDNI % 23
print("Tu DNI es: ", numeroDNI, letra_dni(resto_dni))