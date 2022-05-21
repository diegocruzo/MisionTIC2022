# Importar la clase "system" de la biblioteca "os"
from os import system

# Limpiar pantalla
system("cls")


# Obtener información desde consola
#a = int(input("Digite el valor de la primer variable: ")) # La función input() obtiene la línea ingresada 
                                    # por consola como una cadena de caracteres+

#print("Las dos últimas cifras del número ingresado son:",a%100)
'''b = int(input("Digite el valor de la segunda variable: "))
# Imprimir el valor ingresado en pantalla
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"x",b,"=",a*b)
print(a,"/",b,"=",a/b)
print(a,"//",b,"=",a//b)
print(a,"%",b,"=",a%b)
print(a,"^",b,"=",a**b)'''

'''Ejercicios
1) Solicitar día, mes, año e imprimir en consola la fecha en formato año-mes-dia
2) Solicitar un valor de 8 cifras en formato ddmmaaaa e imprimir en consola la fecha en 
    formato año-mes-día
    Ejemplo: entrada: 30042022, salida: 2022-4-30'''

# Expresiones Relacionales
# Se construyen a partir de operadores relacionales:
# <, >, <=, >=, != 
'''a = 30
b = 4
print(2 == 2.0)'''


# Expresiones lógicas
# Se construyen a partir de operadores lógicos:
# and, or, not
# cad = input("Digite un texto: ")
# p = num >= 1
# q = num <= 10
cad = -9
print("El número ingresado es cero:",not cad)


# Estructuras condicionales