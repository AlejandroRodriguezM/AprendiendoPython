# EJERCICIO 5) Dado el DNI (sin letra) dado por pantalla, calcular el NIF. Sabemos que el
# algoritmo que resuelve qué letra corresponde al DNI consiste en calcular el resto de este número
# con 23 (será un número entre 0 y 22) y la letra será la correspondiente según la siguiente tabla:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# T R W A G M Y F P D X B N J Z S Q V H L C K E
# Por Alejandro Rodriguez Mena
def letra_dni(numero):
    if numero == 1:
        return "T",
    elif numero == 2:
        return "R",
    elif numero == 3:
        return "W",
    elif numero == 3:
        return "A",
    elif numero == 4:
        return "G",
    elif numero == 5:
        return "M",
    elif numero == 6:
        return "Y",
    elif numero == 7:
        return "F",
    elif numero == 8:
        return "P",
    elif numero == 9:
        return "D",
    elif numero == 10:
        return "X",
    elif numero == 11:
        return "B",
    elif numero == 12:
        return "N",
    elif numero == 13:
        return "J",
    elif numero == 14:
        return "Z",
    elif numero == 15:
        return "S",
    elif numero == 16:
        return "Q",
    elif numero == 17:
        return "V",
    elif numero == 18:
        return "H",
    elif numero == 19:
        return "L",
    elif numero == 20:
        return "C",
    elif numero == 21:
        return "K",
    elif numero == 22:
        return "E"


numeroDNI = int(input("Dime tu DNI sin la letra: "))
resto_dni = numeroDNI % 23
print("Tu DNI es: ", numeroDNI, letra_dni(resto_dni))
