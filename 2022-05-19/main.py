from os import system

# Limpiar pantalla
system("cls")

def maximo2(a, b):
    if a > b:
        return a
    else:
        return b

def maximo3(a, b, c):
    return maximo2(maximo2(a, b), c)

def maximo(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    return res    

def maxmin(*a):
    vMax = vMin = a[0]
    # Encontrar los valores máximo y mínimo
    for val in a[1:]:
        if val > vMax:
            vMax = val
        if val < vMin:
            vMin = val
    # Encontrar el valor mínimo
    return vMin, vMax


""" 
# Ejecución del programa principal
print(maximo2(19, 5))
print(maximo3(3, 5, 4))
print(maximo(2, 10, 4, 22, 15, 5, 9, 7))

x, y = maxmin(2, 10, 4, 22, 15, 5, 9, 7)
print(f"El valor mínimo en el último intervalo es {x}")
print(f"El valor máximo en el último intervalo es {y}")
 """

# Número factorial
# 5! = 1 x 2 x 3 x 4 x 5 = 120
# 5! = 120

def factorial(n):
    global f
    res = 1
    for i in range(2,n + 1):
        res *= i
    f = res

# Ejecución del programa principal
#factorial(3))
#print(factorial(5))

factorial(3)
print(f)


"""

# Variables locales y globales

def f():
    global a
    a = 1 # Variable local
    print(a)
        
    

# Ejecución del programa principal
a = 0 # Variable global
print(a)
f()
print(a)
"""

