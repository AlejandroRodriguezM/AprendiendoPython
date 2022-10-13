# EJERCICIO 6) Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que
# deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
# payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

nPayasos = int(input("¿Cuantos numeros de muñecos payaso fueron vendidos en el ultimo pedido? "))
nMuñecas = int(input("¿Cuantos numeros de muñecas fueron vendidos en el ultimo pedido? "))

pPayaso = 112  # peso de 1 muñeco payaso
pMuñeca = 75  # peso de 1 muñeco muñeca

pesoTotalPayaso = 112 * nPayasos  # Peso total del numero de payasos
pesoTotalMuñecas = 75 * nMuñecas  # Peso total del numero de muñecas
pesoPedido = (pesoTotalPayaso + pesoTotalMuñecas) * 0.001  # Sumo el peso total y lo convierto en Kilos

print("El proximo pedido pesara: ", pesoPedido, "kg")
