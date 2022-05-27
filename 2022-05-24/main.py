from email.errors import FirstHeaderLineIsContinuationDefect
from math import factorial
from os import system 
from listas import Factura

clear = lambda: system("cls")

# Crear la instancia de la factura
factura = Factura()

while True:
    # Limpiar pantalla
    clear()

    factura.Show()
    
    print("\n\nMenú:")
    print("1. Ingresar producto(s)")
    print("2. Modificar el último producto ingresado")
    print("3. Finalizar factura")
    op = input("\nDigite la opción deseada: ")
    if op == "1":
        # Solicitar la información del producto
        descProducto = input("Ingrese la descripción del producto: ")
        cant = int(input("Ingrese la cantidad: "))
        vlrUnit = int(input("Ingrese el valor unitario: "))
        # Almacenar la información en la factura
        factura.Push(descProducto, cant, vlrUnit)
    elif op == "2":
        # Eliminar el último producto ingresado
        factura.Pop()
        # Ingresar el producto con la información actualizada
        descProducto = input("Ingrese la descripción del producto: ")
        cant = int(input("Ingrese la cantidad: "))
        vlrUnit = int(input("Ingrese el valor unitario: "))
        factura.Push(descProducto, cant, vlrUnit)
    elif op == "3":
        break
    else:
        print("\nError: Ingresó una opción que no es válida")
        var = input("\nDigite cualquier tecla para continuar...")

clear()
factura.Show()
print("Gracias por su compra. ¡Vuelva pronto!")
    
    
    



# Ejercicio:
# Elaborar un sistema que almacene elementos como la descripción, valor unitario, cantidad
# y subtotal de cada producto en una factura y mostrar el valor total al final.
# Presentar opciones para ingresar un nuevo elemento y para modificar únicamente el último elemento
# ingresado. La modificación se hace eliminando el último elemento e ingresando un elemento nuevo
# con los datos actualizados.



