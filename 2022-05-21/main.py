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
pila.Pop()
pila.Pop()
pila.Pop()

print("\n\nElementos en la pila:")
pila.Show()




