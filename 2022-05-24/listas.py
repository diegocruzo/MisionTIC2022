from nodos import Nodo, NodoFactura

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
    
    # Mostrar la cima (top o peek) de la pila
    def Top(self):
        return self.top
    
    # Mostrar la pila
    def Show(self):
        aux = self.first
        while aux:
            print(aux._dato,end=" ")
            aux = aux._siguiente

# Factura
class Factura():
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
    def Push(self, descProducto, cantidad, valorUnitario):
        # Verificar que la información ingresada sea correcta
        if descProducto is None:
            print("Error: Se debe ingresar un dato válido.")
        else:
            # Paso 1: Asignar memoria
            # Paso 2: Rellenar el campo de datos
            # Paso 3: Dirigir el puntero siguiente del nodo a null (None)
            newNode = NodoFactura(descProducto, cantidad, valorUnitario)
            newNode._subtotal = cantidad * valorUnitario
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
            # Verificar si queda un solo elemento en la pila
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
    
    # Mostrar la cima (top o peek) de la pila
    def Top(self):
        return self.top
    
    # Mostrar la pila
    def Show(self):
        print(" Descripción | Cantidad | Valor Unitario | Subtotal ")
        print("-" * 30)
        total = 0
        aux = self.first
        while aux:
            print(f" {aux._descProducto} | {aux._cantidad} | ${aux._valorUnitario} | {aux._subtotal} ")
            total += aux._subtotal
            aux = aux._siguiente
        print(f"\n\nTotal a pagar: ${total}")


# Clase cola 
class Queue():
    
    # Constructor
    def __init__(self):
        self.front = None # Primer elemento de la cola
        self.rear = None # Último elemento de la cola
        self.size = 0 # Cantidad de elementos que tiene la cola
    
    # Cantidad de elementos de la cola (get)
    def Size(self):
        return self.size

    # Cola vacía
    def Empty(self):
        return self.rear == None
    
    # Operación para apilar (insertar) elementos
    def Enqueue(self, dato = None):
        # Verificar si se ingresó un dato
        if dato is None:
            print("Error: Se debe ingresar un dato válido.")
        else:
            # Paso 1: Asignar memoria
            # Paso 2: Rellenar el campo de datos
            # Paso 3: Dirigir el puntero siguiente del nodo a null (None)
            newNode = Nodo(dato)
            # Verificar si la cola está vacía
            if self.Empty():
                # Operación insertar un elemento en una cola vacía
                # Los punteros inicio (fitst) y fin (rear) apuntan (se asignan)
                # hacia el nuevo elemento
                self.front = self.rear = newNode
            else:
                # Operación Push
                # El puntero siguiente del último elemento apunta hacia
                # el nuevo elemento
                self.rear._siguiente = newNode
                # El puntero fin (rear) apunta hacia el nuevo elemento
                self.rear = newNode
                # El puntero inicio no cambia
            # Actualizar el tamaño de la cola
            self.size += 1    

    # Retirar el último elemento de la cola
    def Dequeue(self):
        # Validar si la cola está vacía
        if self.Empty():
            print("\n\nError: No se puede eliminar elementos de una cola vacía.")
        else:
            # Eliminar el único elemento de la cola
            if self.front == self.rear:
                # El primer y el último elemento de la cola apuntan a null
                self.front = self.rear = None
            # Operación Dequeue
            else:
                # El nuevo primer elemento es el elemento que se encuentra
                # después del anterior primer elemento en la cola 
                self.front = self.front._siguiente
            # Actualizar el tamaño
            self.size -= 1
    
    # Mostrar la cima (rear o peek) de la cola
    def Front(self):
        return self.front
    
    # Mostrar la cola
    def Show(self):
        aux = self.front
        while aux:
            print(aux._dato,end=" ")
            aux = aux._siguiente


