# EJERCICIO 2) Pide por pantalla a un usuario su nombre y la nota que ha sacado, si la nota es
# menor que 5 debe devolver “Estas suspenso”, si está entre 5 y 6 debe devolver “Estás aprobado”, si
# está entre 7 y 8 debe devolver “Tienes notable” y si está entre 9 y 10 debe devolver “Tienes
# sobresaliente”
# Por Alejandro Rodriguez Mena
nombre = input("Dime tu nombre: ")
nota = int(input("¿Que nota has sacado?: "))
print("Hola,",nombre, "has sacado un",nota,":")
if nota < 5:
    print("Estas suspenso.")
elif 5 < nota < 7:
    print("Estas aprobado")
elif 6 < nota < 9:
    print("Tienes un notable")
elif 8 < nota < 11:
    print("Tienes un sobresaliente")
