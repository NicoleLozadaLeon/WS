
class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class ABB:
    def __init__(self):
        self.raiz = None

    def insert(self, data: int):
        self.raiz = self._insert(self.raiz, data)

    def _insert(self, current: Node, data: int) -> Node:
        if current is None:
            return Node(data)

        if data < current.data:
            current.left = self._insert(current.left, data)
        elif data > current.data:
            current.right = self._insert(current.right, data)
        else:
            print(f"Valor duplicado ignorado: {data}")
        return current

    def inorder(self):
        self._inorder(self.raiz)

    def _inorder(self, node: Node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)

    def contar(self):
        contador = 0
        return self._contar(self.raiz, contador)
        

    def _contar(self, nodo:Node, contador:int):
        if nodo:
            contador = self._contar(nodo.left, contador)
            contador = self._contar(nodo.right, contador)
            contador +=1
        return contador

    def menor(self):
        return self._menor(self.raiz)
    
    def _menor(self, nodo:Node):
        if nodo.left:
            return self._menor(nodo.left)
        else:
            return nodo.data
        
    def altura(self):
        return self._altura(self.raiz)
    
    def _altura(self, nodo):
        if nodo:
            al_izq = self._altura(nodo.left)
            al_der = self._altura(nodo.right)
            return max(al_der, al_izq) +1
        else:
            return 0
        
    def hoja(self):
        return self._hoja(self.raiz)
    
    def _hoja(self, nodo):
        if nodo and nodo.left is None and nodo.right is None:
            return 1 
        if nodo is None:
            return 0
        
        return self._hoja(nodo.left) + self._hoja(nodo.right)
    
    def nivel(self, buscando):
        return self._nivel(self.raiz, buscando, 1)

    def _nivel(self, nodo, buscando, nivel_actual):
        if nodo is None:
            return 0
        if nodo.data == buscando:
            return nivel_actual
        # Buscar en el subárbol izquierdo
        nivel_izquierdo = self._nivel(nodo.left, buscando, nivel_actual + 1)
        if nivel_izquierdo != 0:
            return nivel_izquierdo
        # Buscar en el subárbol derecho
        nivel_derecho = self._nivel(nodo.right, buscando, nivel_actual + 1)
        return nivel_derecho


        
    def eliminar(self, value: int):
        self.raiz = self._eliminar(self.raiz, value)

    def _eliminar(self, current: Node, value: int) -> Node:
        if current is None:
            return None

        if value < current.data:
            current.left = self._eliminar(current.left, value)
        elif value > current.data:
            current.right = self._eliminar(current.right, value)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            min_larger_node = self._encontrar_min(current.right)
            current.data = min_larger_node.data
            current.right = self._eliminar(current.right, min_larger_node.data)
        return current

    def _encontrar_min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node
    
abb = ABB()
abb.insert(50)
abb.insert(30)
abb.insert(70)
abb.insert(20)
abb.insert(40)

abb.insert(60)
abb.insert(80)
abb.insert(10)
abb.insert(25)
abb.insert(35)

abb.insert(45)
abb.insert(55)
abb.insert(65)
abb.insert(75)
abb.insert(90)

a = abb.contar()
# print(a)

b = abb.menor()
#print(b)

c = abb.altura()
# print(c)
d = abb.hoja()
print(d)

