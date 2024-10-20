from abc import ABC, abstractmethod
from typing import Any, List, Union
from data_structures import BinaryTreeNode
class LinkedBinaryTreeExtAbstract(ABC):
    """Conjunto de métodos adicionales a LinkedBinaryTree"""
    @abstractmethod
    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> BinaryTreeNode:
        """Devuelve el ancetro común entre nodo1 y nodo2 de mayor profundidad.
        Args:
        nodo1 (BinaryTreeNode): debe no ser None y pertenecer al árbol.
        nodo2 (BinaryTreeNode): debe no ser None y pertencer al árbol.
        Returns:
        BinaryTreeNode: devuelve el ancestro común de nodo1 y nodo2.
        """
    @abstractmethod
    # def hojas(self) -> List[Any]:
    #     """Devuelve los elementos de los nodos que no tienen ningún hijo.
    #     Returns:
    #     List[Any]: lista formada por los elementos de los nodos hoja.
    #     """
    #     pass
    @abstractmethod
    def nivel(self, nodo: BinaryTreeNode) -> int:
        """Busca el nodo pasado por parámetro en el árbol y si lo encuentra
        Retorna su nivel. El nivel del nodo raíz es 0 el nivel de los hijos
        de la raíz es 1 y así sucesivamente.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer su nivel.
        Returns:
        List[Any]: lista formada por los elementos de los nodos hoja.
        """
        pass
    @abstractmethod
    def diametro(self) -> int:
        """Indica el diámetro o ancho máximo de un árbol.
        El ancho máximo es la cantidad máxima de nodos que hay en un mismo nivel del árbol.
        Returns:
        int: devuelve la máxima cantidad de nodos entre todos los niveles que conforman el árbol.
        """
        pass
    @abstractmethod
    def es_balanceado(self) -> bool:
        """Comprueba si el árbol está balanceado
        Página 2 de 5
        Estructuras de Datos - 2024 Trabajo Práctico N.º 4
        Un árbol está balanceado si para cada uno de sus nodos se cumple que la diferencia de altura
        entre el subárbol izquierdo y el derecho no difiere en más de una unidad.
        Returns:
        bool: True en caso que el árbol esté balanceado. False en caso contrario.
        """
        pass