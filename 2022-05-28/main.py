from os import system
# Importar la bibloteca json
import json 

# Crear función para limpiar pantalla
clear = lambda: system("cls")
# Limpiar pantalla
clear()
# Entregar al contenedor "marvel" en Python el contenido del archivo "marvel-cinematic-universe.json"
with open("2022-05-28/marvel-cinematic-universe.json") as marvel:
    #print(marvel.read())
    #print(type(marvel))
    data = json.load(marvel)
"""
print(type(data))
print()
print(f"Título: {data['Marvel Cinematic Universe']['Iron Man']['title']}\n") # Acceder directamente a una clave del diccionario
"""
# Recorrer los elementos de un contenedor
#for elemento in data['Marvel Cinematic Universe']['Iron Man']:
#    print(f"{elemento}: {data['Marvel Cinematic Universe']['Iron Man'][elemento]}")
# Crear un subdirectorio con parte del contenido de otro directorio
hombreIncreible = data['Marvel Cinematic Universe']['The Incredible Hulk']
#print(type(hombreIncreible))
#print(hombreIncreible['release_date'])
contenedor = ['hugo', 'paco', 'luis']
print('lista',json.dumps(contenedor))
contenedor = ('hugo', 'paco', 'luis')
print('tupla',json.dumps(contenedor))
print(json.dumps("Hola"))
print(json.dumps(123))
print(json.dumps(3.14))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convertir un contenedor de Python a un archivo tipo JSON
with open('hombreIncreible.json', 'w') as jsonFile:
    json.dump(hombreIncreible, jsonFile)

print("\nContenido del archivo hombreIncleible.json:")
with open('hombreIncreible.json', 'r') as salida:
    # Leer el contenido
    print(salida.read())


