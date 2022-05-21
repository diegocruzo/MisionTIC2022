from os import system
system("cls")

""" 
c = int(input("Digite la cantidad de datos: "))
lista = [] # Lista vacía
print("Cantidad de elementos de la lista:",len(lista))
for i in range(c):
   lista.append(input(f"Ingrese el valor {i+1}: "))
lista.append("Diego") # Adiciona un elemento en la lista
print("\nCantidad de elementos de la lista:",len(lista))
print(lista)
lista += [3.14] # Adiciona un elemento en la lista
print(lista)
lista = None # Liberar la memoria utilizada """

# Adicionar todos los datos en una lista de forma dinámica
lista = [2,10,5,6,5,8]
""" 
while True:
    lista.append(input("Ingrese un dato: "))
    c = input("presione cualquier tecla para continuar y 'n' para salir: ")
    if c == "n" or c == "N": break
 """
print(lista)

#lista.pop() # Eliminar el último elemento de la lista
#lista.pop(0) # Eliminar el primer elemento de la lista
#lista.pop(3) # Eliminar el elemento en la posición 3
#var = lista.pop(3) # Almacenar en variable el elemento eliminado
#del lista[1] # Eliminar el elemento en la posición 1
# del lista # Eliminar la lista completa
#variable = int(input("Digite un valor a eliminar: "))
#lista.remove(variable)
#print(lista)
print(f"Elemento mínimo de la lista: {min(lista)}")
print(f"Elemento máximo de la lista: {max(lista)}")
print(f"Suma de los elementos de la lista: {sum(lista)}")
print(f"Promedio de los elementos de la lista: {sum(lista)/len(lista)}")
lista.sort()
print("Lista ordenada de menor a mayor: ",lista)
lista.sort(reverse = True)
print("Lista ordenada de mayor a menor: ",lista)
print(f"Cantidad de veces que aparece el 5: {lista.count(5)}")

#lista.append([1,2,3])
print(lista[::-1])

