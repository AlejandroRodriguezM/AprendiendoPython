# EJERCICIO 3) Eliminar de la lista la asignatura Química y mostrar por pantalla sólo las tres
# últimas asignaturas de la lista
# Por Alejandro Rodriguez Mena
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

asignaturas.pop(2)  # Elimina la asignatura Química

print(asignaturas[-3:]) # Muestra las tres ultimas asignaturas de la lista

