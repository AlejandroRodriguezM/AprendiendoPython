# Ejercicio 6 Por Alejandro Rodriguez Mena

import random

# Rellenar la matriz
matriz = []
for i in range(0, 6):
    matriz.append([])
    for j in range(0, 7):
        matriz[i].append(random.randint(0, 100))

# Mostrar la matriz
for i in range(0, 6):
    for j in range(0, 7):
        print(matriz[i][j], end=" ")
    print()

# Buscar el numero maximo y el minimo
numMax = matriz[0][0]
numMin = matriz[0][0]
for i in range(0, 6):
    for j in range(0, 7):
        if matriz[i][j] > numMax:
            numMax = matriz[i][j]
        if matriz[i][j] < numMin:
            numMin = matriz[i][j]

# Mostrar el numero maximo y el minimo
print("El numero maximo es", numMax, "y el minimo es", numMin)