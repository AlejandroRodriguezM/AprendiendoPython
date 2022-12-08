#  Define una función que reciba como arguméntos un número (que nos servirá de
# corte) y una lista de números (no se sabe la longitud de la lista a priori, puede ser cualquiera). La
# función debe devolver dos listas, una con todos los números menores al que se dió de corte, y otra
# con todos los números mayores al número de corte. (el número de corte también debe ser mostrado,
# pero aparte).

def cortarLista(corte, lista):
    lista_mayores = []
    lista_menores = []
    for i in range(len(lista)):
        if lista[i] > corte:
            lista_mayores.append(lista[i])
        else:
            lista_menores.append(lista[i])
    return lista_menores, lista_mayores


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    corte = 5
    lista_menores, lista_mayores = cortarLista(corte, lista)
    print("Lista de menores: ", lista_menores)
    print("Lista de mayores: ", lista_mayores)


main()
