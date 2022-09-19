# EJERCICIO 4) Escribir un programa que pregunte al usuario por el número de horas trabajadas y
# el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas = int(input("¿Cuantas horas has trabajado?: "))
costeHoras = int(input("¿Cuanto es el coste por hora?: "))
total = horasTrabajadas * costeHoras
print("Te corresponden ", total, "€ de paga")
