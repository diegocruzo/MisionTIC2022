from os import system

system("cls")

""" # Conjuntos (set)

# Conjunto vacío
conjunto = {}
print(conjunto)

# Conjunto con elementos
conjunto = {2022, "Diego", 3.14}
print(type(conjunto), conjunto)

conjunto ={1, 2, "Ana", (1, 2, 3)}
print(conjunto)

# Conjunto vacío
conjunto = set()
print(conjunto)

# Adicionar elementos al conjunto
conjunto.add(12)
conjunto.add(5)
conjunto.add((1, 2, 3))
print(conjunto)

 
# Agregar elementos al conjunto mediante ciclos
for i in range(3):
    valor = input(f"\nIngrese el valor {i + 1} del conjunto: ")
    conjunto.add(valor)
print(conjunto)


conjunto.update([51,"6:28", 123])
print(conjunto)

# Retirar elementos del conjunto
conjunto.remove(123)
print(conjunto)

conjunto.discard(515)
print(conjunto)

# Acceder a todos los elementos del conjunto
for elemento in conjunto:
    print(elemento,end = " - ")
print()

# Utilizar el operador "in" para verificar si un elemento se encuentra en un conjunto
print("¿515 está en el conjunto?",515 in conjunto)
print("¿12 está en el conjunto?",12 in conjunto)
 """

# Diccionarios: Se diferencia del conjunto ya que se definen pares de elementos (clave:valor)
directorio = {
    "Alfredo": 3001234578,
    "Diego": 3112225588,
    "Ana": [6047777777, 3208889977],
    12: "Día de hoy",
    (1, 2): "La clave es una tupla",
    "dias": {
        1: "Lunes",
        2: "Martes"
    } 
}

print(directorio.get("Ana"))

if directorio.get("ana") != None:
    print(directorio.get("ana"))
else:
    print("\n'ana' no existe como clave en directorio\n")
    # sentencias

# Adicionar elemento al diccionario nombreDiccionario[clave] = valor
directorio['Cacho'] = 3456742

for clave, valor in directorio.items():
    print(clave,"->",valor)

print("\nClaves en el diccionario:")
for elemento in directorio.keys():
    print(elemento)

print("\nValores en el diccionario:")
for elemento in directorio.values():
    print(elemento)


print("\nDiccionario antes:",directorio)
datoBorrado = directorio.pop("Ana")
print("\nDiccionario después:",directorio)
print(f"Elemento eliminado = {datoBorrado}")
