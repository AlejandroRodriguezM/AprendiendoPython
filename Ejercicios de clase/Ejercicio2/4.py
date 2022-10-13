# EJERCICIO 4) Preguntar por pantalla al usuario su nombre y las asignaturas en las que está
# matriculado, una a una. Introducir todas las asignaturas en una lista y luego mostrar por pantalla “El
# alumno X está matriculado en ….” listando todas las asignaturas en las que está matriculado.
# Por Alejandro Rodriguez Mena
asignaturas = []  # Array de asignaturas de los alumnos
nombreAlumno = input("Dime tu nombre: ")  # Nombre del alumno

# Usando un bucle for, preguntaremos 5 veces la asignatura del alumno y lo guardaremos en un array
for i in range(5):
    asignatura = input("Dime tu asignatura: ")
    asignaturas.append(asignatura)

print("El alumno ", nombreAlumno, "esta matriculado en: ", asignaturas)
