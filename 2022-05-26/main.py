from os import system

clear = lambda: system("cls")

# Limpiar pantalla
clear()

""" 
# Abrir un archivo y entregar el contenido al contenedor "file"
lineas = open("D:/files/prueba.txt", "r+")
#print(file, type(file))

# sacar e imprimir en consola las líneas del archivo
#print(lineas.read())

# Extraer la información del archivo línea por línea
contenedorLineas = lineas.readlines()
print(type(contenedorLineas), contenedorLineas)

print()

for linea in contenedorLineas:
    print(linea.split())

# Cerrar el archivo
lineas.close()
# Abrir el archivo en modo escritura borrando el contenido existente
lineas = open("D:/files/prueba.txt", "w")

# Escribir en el archivo borrando todo su contenido anterior
lineas.write("Cuadrados y cubos de los números del 1 al 15\n")
for i in range(1,16):
    lineas.write(f"{i}^2 = {i**2}, {i}^3 = {i**3}\n")

# Cerrar el archivo
lineas.close()
# Abrir el archivo en modo lectura
lineas = open("D:/files/prueba.txt", "r")

# Leer el archivo resultante
for linea in lineas.readlines():
    print(linea)


# Liberar memoria utilizada
lineas.close() 
"""

""" with open("D:/files/prueba.txt", "r") as lineas:
    for linea in lineas.readlines():
        print(linea)
"""

# Abrir el archivo en modo escritura borrando el contenido existente
with open("D:/files/prueba3.txt", "r+") as lineas:

    # Escribir en el archivo borrando todo su contenido anterior
    """ lineas.write("Cuadrados y cubos de los números del 1 al 5\n")
    for i in range(1,6):
        lineas.write(f"{i}^2 = {i**2}, {i}^3 = {i**3}\n")
    """
    for linea in lineas:
        print(linea,end =" - \n")
    