from os import system
from re import A

system("cls")


# Función: Porción de código que ejecuta una o varias acción(es) específica(s)

def nombres(apellido = ""):
    """
    La función nombres se encarga de
    imprimir tanto el nombre como el 
    apellido concatenados    
    Entada(s):
        nombre -> str: Nombre de la persona
        [apellido -> str_ Apellido de la persona]
    Salida:
        None. En la función se imprime el nombre y el apellido separados por espacios        
    """

    nombre = input("Por favor digite su nombre: ")
    print(nombre, apellido)
    

def numeroPar(num):
    """ Documentación """
    # if "1023456789".find(str(num)) != -1:
    if num <= -99999 or num >= 99999:
        print("Error: El número entero debe tener máximo cinco (5) cifras")
    elif isinstance(num, int):
        if num == 0:
            print("El valor ingresado es cero")
        elif num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
    else:
        print("Error: el número ingresado debe ser un número entero")    
    
numeroPar(-100000)

# Try catch
# Principios SOLID




# Mostrar la documentación de la función
# print(nombres.__doc__)

# Ejecución del programa principal
# nombres("Diego")

