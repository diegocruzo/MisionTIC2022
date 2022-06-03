from nodos import Nodo

# Clase pila 
class Stack():
    
    # Constructor
    def __init__(self):
        self.first = None # Primer elemento de la pila
        self.top = None # Cima o tope (peek), último elemento de la pila
        self.size = 0 # Cantidad de elementos que tiene la pila
    
    # Cantidad de elementos de la pila (get)
    def Size(self):
        return self.size

    # Pila vacía
    def Empty(self):
        return self.top == None
    
    # Operación para apilar (insertar) elementos
    def Push(self, dato = None):
        # Verificar si se ingresó un dato
        if dato is None:
            print("Error: Se debe ingresar un dato válido.")
        else:
            # Paso 1: Asignar memoria
            # Paso 2: Rellenar el campo de datos
            # Paso 3: Dirigir el puntero siguiente del nodo a null (None)
            newNode = Nodo(dato)
            # Verificar si la pila está vacía
            if self.Empty():
                # Operación insertar un elemento en una pila vacía
                # Los punteros inicio (fitst) y fin (top) apuntan (se asignan)
                # hacia el nuevo elemento
                self.first = self.top = newNode
            else:
                # Operación Push
                # El puntero siguiente del último elemento apunta hacia
                # el nuevo elemento
                self.top._siguiente = newNode
                # El puntero fin (top) apunta hacia el nuevo elemento
                self.top = newNode
                # El puntero inicio no cambia
            # Actualizar el tamaño de la pila
            self.size += 1    

    # Retirar el último elemento de la pila
    def Pop(self):
        # Validar si la pila está vacía
        if self.Empty():
            print("\n\nError: No se puede eliminar elementos de una pila vacía.")
        else:
            # Eliminar el último elemento de la pila
            if self.first == self.top:
                # El primer y el último elemento de la pila apuntan a null
                self.first = self.top = None
            # Operación Pop
            else:
                # Encontrar la ubicación del penúltimo elemento de la lista (elemento
                # actual o posición)
                aux = self.first
                while aux._siguiente != self.top:
                    aux = aux._siguiente
                # El puntero siguiente del elemento actual (posición) apuntará hacia la
                # dirección a la que apunta el puntero siguiente del último elemento en 
                # la pila 
                aux._siguiente = self.top._siguiente
                # El elemento actual es ahora el último elemento en la Pila
                self.top = aux
            # Actualizar el tamaño
            self.size -= 1
        
    # Mostrar la pila
    def Show(self):
        aux = self.first
        while aux:
            print(aux._dato,end=" ")
            aux = aux._siguiente

# Clase lista simplemente enlazada
class SinglyLinkedList():
    
    # Constructor
    def __init__(self):
        self._first = None # Puntero al primer elemento
        self._last = None # Puntero al último elemento
        self._size = 0 # Cantidad de elementos de la lista simplemente enlazada
        
    # Método para verificar si la lista está vacía
    def Empty(self):
        return self._first == None
    
    # Método para insertar un elemento al inicio de la lista
    def InsertFirst(self, dato):
        # Asignar memoria y rellenar el campo de datos
        newNode = Nodo(dato)
        # Verificar si la lista está vacía
        if self.Empty():
            # Método para ingresar un elemento en una lista vacía
            # Los punteros inicio y fin apuntan hacia el nuevo elemento
            self._first = self._last = newNode
        else:
            # Mètodo para ingresar un elemento al inicio de la lista
            # El puntero siguiente del nuevo elemento apunta hacia
            # el primer elemento.
            newNode._siguiente = self._first
            # El puntero inicio apunta hacia el nuevo elemento
            self._first = newNode
        # Actualizar el tamaño
        self._size += 1
            

    
    
    # Operación para mostrar los elementos de la lista
    def Show(self):
        aux = self._first
        while aux:
            print(aux.dato,end=" ")
            aux = aux._siguiente
        print("\n")






