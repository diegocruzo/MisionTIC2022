from os import system
system("cls")


'''
# Imprimir los cinco números siguientes al número ingresado
a = int(input("Por favor ingrese un valor numérico entero: "))

contador = 0
# Ciclo repetitivo mientras (while)
while contador < 5:
    # system("cls") # Limpiar pantalla
    a += 1
    print(a)
    contador += 1

120 = 2 * 2 * 2 * 3 * 5
res = 120 / 2
res = 60 / 2
res = 30 / 2
res = 15 / 3
res = 5 / 5
res = 1

# Imprimir los cinco números siguientes al número ingresado
num = int(input("Por favor ingrese un valor numérico entero: "))
 
resultado = str(num) + " = "
while num != 1:
    valor = 2
    while valor <= num:
        if num % valor == 0:
            if num / valor == 1:
                resultado += str(valor)
            else:    
                resultado += str(valor) + " x "
            num /= valor # num = num / valor
            break
        valor += 1
print(resultado)  
'''  



'''i = 0
# Ciclo repetitivo mientras (while)
while i < 5:
    # system("cls") # Limpiar pantalla
    a += 1
    print(a)
    i += 1
'''

# Ciclo repetitivo para
""" for (int i = 2; i < num; i++){
    # Sentencias
} """

""" 
# Imprimir los cinco números siguientes al número ingresado
num = int(input("Por favor ingrese un valor numérico entero: "))

# python

for i in range(2, 7):
    num /= i
    print(num)
else:
    print(f"Valor de num dentro del else: {num}")    
 """

palabra = input("Digite una palabra: ")

# foreach letra in palabra:

cont = 0
for i in range(len(palabra)):
    print(f"En el índice {i} se encuentra la letra",palabra[i])


















