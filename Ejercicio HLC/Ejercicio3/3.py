# EJERCICIO 3) Pide al usuario por pantalla una contraseña que hayamos inventado. No debe
# dejarlo continuar mientras no acierte la contraseña.

realPass = "test"

tryPass = input("Dime la contraseña: ")

while realPass != tryPass:
    tryPass = input("Dime la contraseña: ")
    if realPass == tryPass:
        print("Has acertado la contraseña")


