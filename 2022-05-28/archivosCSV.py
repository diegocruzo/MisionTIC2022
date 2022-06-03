from os import system
# Importar la bibloteca csv
import csv

# Crear función para limpiar pantalla
clear = lambda: system("cls")
# Limpiar pantalla
clear()

# Crear listas vacías para almacenar el contenido
encabezados = []
registros = []

with open('2022-05-28/starwars_characters.csv', 'r') as csvFile:
    # El contenido del archivo tipo CSV se entrega a un contenedor tipo CSV en Python 
    lectorCSV = csv.reader(csvFile)
    
    # Obtener los encabezados del archivo CSV. Para una línea del contenedor se utiliza el método "next"
    encabezados = next(lectorCSV)
    
    # Obtener los registros del arhivo CSV.
    for registro in lectorCSV:
        registros.append(registro)
    
    # Obtener la cantidad de registros
    #print("Cantidad total de registros:", lectorCSV.line_num) 

#print("Encabezados:",encabezados)
#print("Registros:")

#for linea in registros:
#    print(linea)

top5 = []
for i in range(5):
    top5.append(registros[i])

with open('CincoPrimerosCaracteresStarwars.csv', 'w') as csvFile:
    # En "documento" se almacena la información del archivo con el alias "csvFile" haciendo uso de los métodos CSV
    documento = csv.writer(csvFile)
    # Escribir una sola fila (encabezados en el archivo)
    documento.writerow(encabezados)
    # Escribir varias filas (registros en el archivo)
    documento.writerows(top5)
    
with open('CincoPrimerosCaracteresStarwars.csv', 'r') as salida:
    print(salida.read())