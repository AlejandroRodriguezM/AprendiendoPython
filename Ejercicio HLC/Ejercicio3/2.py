# EJERCICIO 2) Pide por pantalla a un usuario su nombre y la nota que ha sacado, si la nota es
# menor que 5 debe devolver “Estas suspenso”, si está entre 5 y 6 debe devolver “Estás aprobado”, si
# está entre 7 y 8 debe devolver “Tienes notable” y si está entre 9 y 10 debe devolver “Tienes
# sobresaliente”

nombre = input("Dime tu nombre: ")
nota = int(input("¿Que nota has sacado?: "))
print("Hola,",nombre, "has sacado un",nota,":")
if nota < 5:
    print("Estas suspenso.")
elif nota > 5 and nota < 7:
    print("Estas aprobado")
elif nota > 6 and nota < 9:
    print("Tienes un notable")
elif nota > 8 and nota < 11:
    print("Tienes un sobresaliente")
