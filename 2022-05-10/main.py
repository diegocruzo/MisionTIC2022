from os import system
system("cls")

# Entradas
nombres = ["Ana", "Luis", "Pedro"] # Arreglo de 3 posiciones
notas = [[3.1, 4.5, 3.5], [3, 3.2, 5], [2.4, 4.8, 1.2]] # Matriz 3 x 3
definitivas = [] # Lista vacía

# Proceso
# Calcular la definitiva
for i in range(3):
    definitivas.append((notas[i][0] * 0.5) + (notas[i][1] * 0.3) + (notas[i][2] * 0.2))

# Salida
# Mostrar el resultado
print("Nombre | nota1 | nota2 | nota3 | Definitiva")
print("-"*43)

for i in range(len(notas)):
    print(nombres[i],end = " | " )
    for nota in notas[i]: # foreach
        print(nota,end=" | ")
    print(definitivas[i])
    
    
"""     
notas = [[3.1, 4.5, 3.5], [3, 3.2], [2.4]] # Matriz 3 x 3
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(f"notas[{i}][{j}] = {notas[i][j]}")
 """

system("cls")

print("Tuplas")
nombres[1] = "Faruk"
print(type(nombres),nombres)
datos = (1, 2, 10, "Diego", [4, 5, 7], (2, 3)) # Creación de una tupla
print(type(datos),datos)
print(datos[4])
print("Cantidad de elementos en la tupla:",len(datos))

numUnico = 2,
print(type(numUnico),numUnico)

print(type(nombres),nombres)
nombres = tuple(nombres)
print(type(nombres),nombres)

print("-"*50,"\nRecorrido de una tupla:")
for i in range(len(datos)):
    print(type(datos[i]),datos[i])
