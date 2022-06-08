from os import system
from listas import SinglyLinkedList

system("cls")

# Crear la instancia (objeto) de la clase SinglyLinkedList
lista = SinglyLinkedList()

# Ingresar elementos al inicio de la lista
lista.InsertFirst(2022)
lista.InsertFirst(3)

print("Tipo de lista:",type(lista))

print("\nMostrar elementos de la lista:")
lista.Show()

lista.InsertLast("Diego")
lista.InsertLast(6)

print("Mostrar elementos de la lista:")
lista.Show()

lista.Insert(80, 2022)

print("Mostrar elementos de la lista:")
lista.Show()

print("\nÚltimo elemento:",lista._last)

lista.RemoveFirst()

print("Mostrar elementos de la lista después de eliminar el primero:")
lista.Show()

print("Cantidad de elementos en la lista:",lista.Size())

lista.RemoveLast()

print("Mostrar elementos de la lista después de eliminar el último:")
lista.Show()

print("\nÚltimo elemento:",lista._last)


