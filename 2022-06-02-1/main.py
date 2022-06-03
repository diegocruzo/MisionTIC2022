from os import system
system("cls")

particiones = 1

for i in range(10):
    try:
        particiones = particiones / i
    except Exception as e:
        print("No es posible dividir entre cero (0). El programa ignorará esta operación.")
        print("Error:",e,sep="\n")
    print("\nResultado parcial de la división:",particiones)

print("\nResultado final:",particiones)


""" 
a = input('Digite un número: ')
try:
    print(a + 15)
except TypeError as e:
    print("La variable no se almacenó como número.")
    print("Error: ",e,sep="\n")

 """

