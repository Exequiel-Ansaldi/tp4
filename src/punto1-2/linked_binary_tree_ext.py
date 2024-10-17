from data_structures import LinkedBinaryTree
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode
class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hojas(self):
        lista = []
        for nodo in self.__iter__():
            if nodo.children_count() == 0:
                lista.append(nodo.element)
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
