class Nodo():
    
    # Constructor
    def __init__(self, dato, siguiente = None):
        self._dato = dato # dato que tiene el nodo
        self._siguiente = siguiente # Puntero o apuntador al siguiente nodo
    
    # Formato de salida de los datos
    def __str__(self):
        return str(self._dato)