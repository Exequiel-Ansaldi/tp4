from data_structures import LinkedBinaryTree
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode
from data_structures import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hojas(self):
        lista = []
        stack = [self._root]

        while stack:
            nodo = stack.pop()
            
            # Si el nodo es hoja, lo agregamos a la lista.
            if nodo is not None and nodo.children_count == 0:
                lista.append(nodo.element)
            
            # Agregamos los hijos al stack si existen.
            if nodo is not None:
                if nodo.right_child:
                    stack.append(nodo.right_child)
                if nodo.left_child:
                    stack.append(nodo.left_child)

        return lista

    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode):
        camino_nodo1 = []
        actual = nodo1
        while actual:
            camino_nodo1.append(actual)
            actual = self._search_parent(actual)
        camino_nodo1.reverse()

        camino_nodo2 = []
        actual = nodo2
        while actual:
            camino_nodo2.append(actual)
            actual = self._search_parent(actual)
        camino_nodo2.reverse()
        
        ancestro_comun = None
        for ancestro1, ancestro2 in zip(camino_nodo1, camino_nodo2):
            if ancestro1 == ancestro2:
                ancestro_comun = ancestro1
            else:
                break
        
        return ancestro_comun
    
    def nivel(self, nodo: BinaryTreeNode) -> int:
        if self.is_empty():
            raise Exception("El árbol está vacío.")
        
        queue = LinkedQueue()
        queue.enqueue(self._root)

        nivel_actual = 0

        while not queue.is_empty():
            size = len(queue)

            for _ in range(size):
                actual = queue.first()

                if actual == nodo: 
                    return nivel_actual

                
                if actual.left_child:
                    queue.enqueue(actual.left_child)
                if actual.right_child:
                    queue.enqueue(actual.right_child)

                queue.dequeue()

            nivel_actual += 1
    
    def diametro(self) -> int:
        if self._root is None:
            return 0  

        ancho_maximo = 0  
        cola = LinkedQueue()  
        cola.enqueue(self._root)

        while not cola.is_empty():
            tamaño_nivel = len(cola)
            print(f"Tamaño del nivel: {tamaño_nivel}")
            ancho_maximo = max(ancho_maximo, tamaño_nivel)  

            for _ in range(tamaño_nivel): 
                print(f"Nodo actual: {actual.element}")
                if isinstance(actual, BinaryTreeNode): 
                    actual = cola.dequeue()
                    if actual.left_child:  
                        cola.enqueue(actual.left_child)  
                    if actual.right_child:  
                        cola.enqueue(actual.right_child)   

        return ancho_maximo

    def _altura(self, nodo) -> int:
        return 0 # mirar que hacer acá 
        # if nodo is None:
        #     retu


    def _es_balanceado(self, nodo) -> bool:

        if nodo.children_count == 0:
            return True

        return not abs(self._altura(nodo.right_child) - self._altura(nodo.left_child)) > 0
    
    def es_balanceado(self) -> bool:
    # Si el árbol está vacío, se considera balanceado.
        if self.root is None:
            return True

        queue = LinkedQueue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            nodo = queue.first()

            actual = self._es_balanceado(nodo)
            print(f"{nodo}: {actual}")
            if not actual:
                return False

            if nodo.left_child:
                queue.enqueue(nodo.left_child)

            if nodo.right_child:
                queue.enqueue(nodo.right_child)

            queue.dequeue()

        return True

        # # Stack para almacenar nodos y sus respectivas alturas.
        # stack = [(self.root, 0)]
        # alturas = {None: 0}

        # while stack:
        #     nodo, estado = stack.pop()

        #     if estado == 0:
        #         # Almacenar el nodo con estado 'visitado'
        #         stack.append((nodo, 1))
        #         # Añadir los hijos del nodo actual.
        #         if nodo.left_child:
        #             stack.append((nodo.left_child, 0))
        #         if nodo.right_child:
        #             stack.append((nodo.right_child, 0))
        #     else:
        #         # Calcular la altura de los hijos.
        #         altura_izq = alturas.get(nodo.left_child, 0)
        #         altura_der = alturas.get(nodo.right_child, 0)

        #         # Verificar si el nodo está balanceado.
        #         if abs(altura_izq - altura_der) > 1:
        #             return False

        #         # Almacenar la altura del nodo.
        #         alturas[nodo] = max(altura_izq, altura_der) + 1

        # # Si hemos recorrido todo sin encontrar problemas, el árbol está balanceado.
        # return True
