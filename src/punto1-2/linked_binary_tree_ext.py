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

                # Encolar hijos
                if actual.left_child:
                    queue.enqueue(actual.left_child)
                if actual.right_child:
                    queue.enqueue(actual.right_child)

                queue.dequeue()

            nivel_actual += 1
    
    def diametro(self) -> int:
        if self.root is None:
            return 0  

        ancho_maximo = 0  
        cola = LinkedQueue()  
        cola.enqueue(self.root)

        while not cola.is_empty():
            tamaño_nivel = cola._size 
            ancho_maximo = max(ancho_maximo, tamaño_nivel)  

            for _ in range(tamaño_nivel):  
                actual = cola.dequeue()  
                if actual.left_child:  
                    cola.enqueue(actual.left_child)  
                if actual.right_child:  
                    cola.enqueue(actual.right_child)   

        return ancho_maximo  


       



