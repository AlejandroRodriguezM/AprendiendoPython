# EJERCICIO 2) Escribe una función que, tomando los dos catetos de un triángulo rectángulo,
# devuelva la hipotenusa del mismo. Luego pruébala.
# Por Alejandro Rodriguez Mena

def checkTriangulo():
    try:
        cateto1 = int(input("Cateto 1: "))
        cateto2 = int(input("Cateto 2: "))
        hipotenusa = pow(cateto1, 2) + pow(cateto2, 2)
        print("La hipotenusa de ", cateto1, "y", cateto2, "es: ", hipotenusa)
    except ValueError:
        print("ERROR. Introduce un numero.")
        raise checkTriangulo()  # Raise se utiliza para poder volver a llamar a la funcion, este bucle se seguira
        # efectuando mientras no se introduzcan numeros.


checkTriangulo()
