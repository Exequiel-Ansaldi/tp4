from abc import ABC, abstractmethod
from typing import Any
from data_structures import ArrayHeap
class ArrayHeapExtAbstract(ABC):
    @abstractmethod
    def fusionar(self, otro: ArrayHeap) -> None:
        """Combina los elementos de otro heap en este dejándolos perfectamente ordenados.

        Args:
        otro (ArrayHeap): ArrayHeap pasado por parámetro.
        """
        pass
    @abstractmethod
    def vaciar(self) -> None:
        """ Una vez invocado el Heap queda sin elementos. """
        pass
    @abstractmethod
    def eliminar_por_prioridad(self, k: Any) -> None:
        """ Elimina el elemento con prioridad igual al parámetro k.
        Luego de ser invocado la estructura debe preservar la condición de orden
        Args:
        k (Any): prioridad del elemento a eliminar.
        """
    @abstractmethod
    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        """ Cambia la prioridad de los nodos con prioridad igual k_actual y establece como nueva prioridad k_nueva.
        Args:
        k_actual (Any): prioridad actual del elemento a modificar
        k_nueva (Any): nueva prioridad que debe ser asignada.
        """
        pass
        
