# Realiza el juego de PIEDRA/PAPEL/TIJERA donde el usuario podrá jugar contra
# el ordenador, el cual realizará sus tiradas de forma aleatoria. Tras cada jugada el ordenador pregunta
# al usuario si desea continuar. En caso de que la respuesta sea negativa se mostrará por pantalla el
# número de jugadas que ha ganado cada uno.
import random

jugadas = ["piedra", "papel", "tijera"]
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0


# Funcion que pide al usuario que introduzca piedra, papel o tijera
def pedirJugada():
    try:
        jugada = input("Introduce piedra, papel o tijera: ")
        if jugada == "piedra" or jugada == "papel" or jugada == "tijera":
            return jugada
        else:
            raise ValueError
    except ValueError:
        print("Error. El caracter introducido no es valido.\nDebe de introducir piedra, papel o tijera")
        raise SystemExit


# Funcion que genera una jugada aleatoria
def jugadaAleatoria():
    jugada = random.choice(jugadas)
    return jugada


# Funcion que compara las jugadas
def compararJugadas(jugada1, jugada2):
    global partidas_ganadas
    global partidas_perdidas
    global partidas_empatadas
    if jugada1 == jugada2:
        print("Empate")
        partidas_empatadas += 1
    elif jugada1 == "piedra" and jugada2 == "tijera":
        print("Has ganado!")
        partidas_ganadas += 1
    elif jugada1 == "papel" and jugada2 == "piedra":
        print("Has ganado!")
        partidas_ganadas += 1
    elif jugada1 == "tijera" and jugada2 == "papel":
        print("Has ganado!")
        partidas_ganadas += 1
    else:
        print("Ha ganado la maquina!")
        partidas_perdidas += 1


# Funcion que pregunta al usuario si desea continuar
def continuar():
    respuesta = input("¿Desea continuar? (s/n): ")
    return respuesta


def main():
    while True:
        jugador = pedirJugada()
        maquina = jugadaAleatoria()
        compararJugadas(jugador, maquina)
        respuesta = continuar()
        if respuesta == "n":
            print("Ganadas:", partidas_ganadas, "\nPerdidas:", partidas_perdidas, "\nEmpatadas:", partidas_empatadas)

            break


main()
