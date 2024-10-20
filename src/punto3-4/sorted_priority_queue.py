from typing import Any, List
from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from data_structures import PriorityQueueBase
class SortedPriorityQueue(SortedPriorityQueueAbstract, PriorityQueueBase):
    def __init__(self):
        self._elements: List[self._Item] = []  

    def __len__(self):
        return len(self._elements) 
    
    def is_empty(self):
        return len(self) == 0
    
    def remove_min(self):
        if self.is_empty():
            raise Exception("La cola está vacía.")
        item = self._elements.pop(0)  
        return item._key, item._value
    
    def __str__(self) -> str:
        return f"SortedPriorityQueue([{', '.join(str(item) for item in self._elements)}])"
    
    def add(self, k: Any, v: Any):
        item = self._Item(k, v) 
        self._elements.append(item)  
        self._elements.sort() 

    def min(self):
        if self.is_empty(): 
            raise Exception("La cola está vacía.")
        item = self._elements[0]
        return (item._key, item._value)