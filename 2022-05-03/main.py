from os import system
system("cls")

""" # Ciclo condicional If - else if
if (a >= 0 and a <= 5) or (a >= 15 and a <=20): # and => && or => ||
    # Sentencia(s) por verdadero
    print("El valor ingresado está entre 0 y 5 o entre 15 y 20")
elif (a < 0 or a > 10): # else if
    # Sentencia(s) por verdadero en la siguiente condición
    print("El valor ingresado no está entre 0 y 10")
else:
    # Sentencia(s) por falso
    print("El valor ingresado no está en los intervalos deseados") """

# Imprimir los cinco números siguientes al número ingresado
a = int(input("Por favor ingrese un valor numérico entero: "))

contador = 0
# Ciclo repetitivo mientras (while)
while contador < 5:
    # system("cls") # Limpiar pantalla
    a += 1
    print(a)
    contador += 1



print("Fin del programa")
'''
# Descomponer cualquier número entero en sus factores primos

8 = 2 x 2 x 2
15 = 3 x 5
12 = 2 x 2 x 3

'''