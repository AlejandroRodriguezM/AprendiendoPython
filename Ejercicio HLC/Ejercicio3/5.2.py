# EJERCICIO 5) Dado el DNI (sin letra) dado por pantalla, calcular el NIF. Sabemos que el
# algoritmo que resuelve qué letra corresponde al DNI consiste en calcular el resto de este número
# con 23 (será un número entre 0 y 22) y la letra será la correspondiente según la siguiente tabla:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# T R W A G M Y F P D X B N J Z S Q V H L C K E

lista_letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]


def letra_calculo(dni):
    resto = dni % 23
    letra = lista_letras[resto]
    return letra


numeroDNI = int(input("Escribe tu DNI sin la letra: "))
print("La letra del DNI: ", numeroDNI, "ES: ", letra_calculo(numeroDNI))
