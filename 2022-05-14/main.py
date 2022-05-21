import os 
# Importar mi biblioteca
import objetosPropios as op

# Limpiar pantalla
clear = lambda: os.system("cls")

valorExiste = (lambda x: x == None)

clear()
""" 
# Importar la biblioteca numpy y darle una etiqueta
import numpy as np


# Arreglos usando los métodos para listas en Python
a = [1, 2, 3]
b = [[1, 2, 3], [4, 5, 6]]

print(type(a),f"a:\n{a}")
print(type(b),f"b:\n{b}")

# Crear arreglos tipo numpy
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)])

print("\nArreglo 'a' tipo numpy:")
print(a)
print(f"Cantidad de dimensiones de 'a': {a.ndim}")
print(f"La(s) dimensión(es) de 'a': {a.shape}")
print(f"Cantidad de elementos de 'a': {a.size}")
print(f"Tipo de dato de el(los) elemento(s) en 'a': {a.dtype}")
print(f"Tamaño de cada elemento de 'a' en bytes: {a.itemsize}")

print("\nArreglo 'b' tipo numpy:")
print(b)
print(f"Cantidad de dimensiones de 'b': {b.ndim}")
print(f"La(s) dimensión(es) de 'b': {b.shape}")
print(f"Cantidad de elementos de 'b': {b.size}")
print(f"Tipo de dato de el(los) elemento(s) en 'b': {b.dtype}")
print(f"Tamaño de cada elemento de 'b' en bytes: {b.itemsize}")
 """

# Crear una instancia (copia) del objeto (clase) "Auto"
carro1 = op.Auto("Honda", "Azul")
carro1.placa ="ABC-123"
print(f"Marca del carro: {carro1.marca}")
print(f"Color del carro: {carro1.color}")
print(f"Placa del carro: {carro1.placa}")

print(f"5! = {op.factorial(5)}")
print(valorExiste(None))