# Ejercicio 3 Por Alejandro Rodriguez Mena

cadena = input("Introduce una cadena de caracteres: ")
cadena = cadena.split() # Se divide la cadena por los espacios que hay
diccionario = {} # Se crea el diccionario
for i in cadena:
    diccionario[i] = cadena.count(i) #Comprueba cuantas veces una palabra se repetite en el diccionario
print(diccionario)

