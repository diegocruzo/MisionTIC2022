from os import system 
from listas import Stack

clear = lambda: system("cls")

# Limpiar pantalla
clear()

# Crear la instancia de la pila
pila = Stack()

print(f"¿La pila está vacía?: {pila.Empty()}")

# Ingresar elementos en la pila
pila.Push("Juan")
pila.Push(21)
pila.Push(2022)

print(f"\n¿La pila está vacía?: {pila.Empty()}")

print("\nElementos en la pila:")
pila.Show()

# Retirar un elemento en la pila
pila.Pop()

print("\n\nElementos en la pila:")
pila.Show()


# Ejercicio:
# Elaborar un sistema que almacene elementos como la descripción, valor unitario, cantidad
# y subtotal de cada producto en una factura y mostrar el valor total al final.
# Presentar opciones para ingresar un nuevo elemento y para modificar únicamente el último elemento
# ingresado. La modificación se hace eliminando el último elemento e ingresando un elemento nuevo
# con los datos actualizados.



