# Realiza un programa que tome como argumento el nombre de un fichero de texto
# donde tendremos escritas las rutas de 4 imágenes que tendremos en nuestro ordenador, una ruta por
# fila del fichero. Una vez leídas estas rutas deberá guardarlas en una lista, y con ella generar un
# archivo index.html donde se muestre una cabecera que ponga IMÁGENES, y a continuación cada
# una de las imágenes con un título que ponga IMAGEN X, donde la x será el número de la imagen

#Funcion que lee el contenido del fichero y lo guarda en una lista
def leerFichero():
    try:
        fichero = open("fichero.txt", "r")
        lista = []
        for linea in fichero:
            lista.append(linea)
        fichero.close()
        print(lista)
        return lista
    except FileNotFoundError:
        print("Error. El fichero no existe")
        raise SystemExit

# Funcion que genera el archivo HTML
def generarHTML(lista):
    fichero = open("index.html", "w")
    fichero.write("<html><head><title>IMÁGENES</title></head><body>")
    for i in range(len(lista)):
        fichero.write("<h1>IMAGEN " + str(i + 1) + "</h1><img src='" + lista[i] + "'/>")
    fichero.write("</body></html>")
    fichero.close()

# Funcion principal
def main():
    generarHTML(leerFichero())

main()