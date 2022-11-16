# Realiza un programa que realice la función de un cajero automático, preguntando
# al usuario cuanto dinero desea retirar, y una vez recogida la cantidad debe mostrar por pantalla en
# número de billetes de cada clase que le va a devolver. Esta cantidad deberá ser “ideal”, es decir,
# deberá devolver la cantidad solicitada con el menor número de billetes posible. Los billetes podrán
# ser de 100, 50, 20, 10 ó 5 euros, no siendo posible la devolución de monedas

# Funcion que pide dinero
def pedirDinero():
    try:
        dinero = int(input("Introduce la cantidad de dinero a retirar: "))
        return dinero
    except ValueError:
        print("Error. El caracter introducido no es valido.\nDebe de introduce un numero")
        raise SystemExit

# Funcion que calcula segun el dinero reitaro, devolvera de forma optima el numero de billetes
def calcularBilletes(dinero):
    billetes = [100, 50, 20, 10, 5]
    for i in range(len(billetes)):
        if dinero >= billetes[i]:
            print("Billetes de", billetes[i], ":", dinero // billetes[i])
            dinero = dinero % billetes[i]

def main():
    calcularBilletes(pedirDinero())

main()




