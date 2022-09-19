# EJERCICIO 7) Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
# un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas
# que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el
# descuento que se le hace por no ser fresca y el coste final total.

precioPanDia = 3.49
precioPanManio = 3.49 * 0.6

panManioVendido = int(input("¿Cuantas barras de pan que no son del dia se han vendido?: "))

precioTotalManio = precioPanManio * panManioVendido

print("El precio habitual de una barra de pan es: ",precioPanDia,"€, el pan que no es del dia se le aplica es del 60%"
                                                                 ", el coste final es: ",precioTotalManio,"€")
