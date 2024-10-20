from typing import Any
from data_structures import ArrayHeap
from array_heap_ext_abstract import ArrayHeapExtAbstract

class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):
    def fusionar(self, otro : ArrayHeap):
         while len(otro) > 0:
            key, value = otro.remove_min()  
            self.add(key, value)
    
    def vaciar(self) -> None:
        self._data.clear()
    

    def eliminar_por_prioridad(self, k: Any) -> None:

        index = None
        for i in range(len(self._data)):
            if self._data[i]._key == k:
                index = i
                break
        
        if index is None:
            raise ValueError(f"No se encontró ningún elemento con prioridad {k}.")
        
        self._data[index], self._data[-1] = self._data[-1], self._data[index]
        self._data.pop()

        
        if index < len(self._data):
            self._downheap(index)
            self._upheap(index)


    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
       
        for i in range(len(self._data)):
            if self._data[i]._key == k_actual:
                self._data[i]._key = k_nueva
                self._downheap(i)
                self._upheap(i)


    