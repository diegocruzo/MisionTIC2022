# Creación de la clase "Auto"
class Auto():
    
    # Constructor: Crear una instancia (copia) del objeto (clase) vacía
    def __init__(self, marca, color = None, placa = None):
        # Características, propiedades o atributos del objeto
        self.marca = marca # Asigno un atributo o propiedad al objeto "Auto" llamado marca y no le doy valor
        self.color = color
        self.placa = placa
    
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)    
        
        