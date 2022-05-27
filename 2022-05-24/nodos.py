class Nodo():
    
    # Constructor
    def __init__(self, dato, siguiente = None):
        self._dato = dato # dato que tiene el nodo
        self._siguiente = siguiente # Puntero o apuntador al siguiente nodo
    
    # Formato de salida de los datos
    def __str__(self):
        return str(self._dato)

class NodoFactura():
    
    # Constructor
    def __init__(self, descProducto, cantidad, valorUnitario, siguiente = None):
        self._descProducto = descProducto # dato 1 que tiene el nodo
        self._cantidad = cantidad # dato 2 que tiene el nodo
        self._valorUnitario = valorUnitario # dato 3 que tiene el nodo
        self._subtotal = 0 # dato 4 que tiene el nodo
        self._siguiente = siguiente # Puntero o apuntador al siguiente nodo
    
    # Formato de salida de los datos
    def __str__(self):
        salida = str(self._descProducto) + " -> " + str(self._valorUnitario)
        return salida