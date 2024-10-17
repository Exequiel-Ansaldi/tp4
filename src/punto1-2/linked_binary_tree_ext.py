from data_structures import LinkedBinaryTree
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
class LinkedBinaryTreeExt( LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hojas(self):
        lista = []
        for nodo in self.__iter__():
            if nodo.children_count() == 0:
                lista.append(nodo.element)
        return lista