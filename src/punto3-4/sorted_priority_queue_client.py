from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from sorted_priority_queue import SortedPriorityQueue
class SortedPriorityQueueClient(SortedPriorityQueue, SortedPriorityQueueAbstract):
   cola_prioridad = SortedPriorityQueue()
   cola_prioridad.add(5, 'tarea 5')   
   cola_prioridad.add(1, 'tarea 1')  
   cola_prioridad.add(3, 'tarea 3')   
   cola_prioridad.add(2, 'tarea 2')   
   cola_prioridad.add(4, 'tarea 4')   
   print(f'Total de elementos: {len(cola_prioridad)}')
   min_item = cola_prioridad.min()
   print(f'Ítem mínimo: {min_item}') 
   removed_item = cola_prioridad.remove_min()
   print(f'Ítem removido: {removed_item}')  
   nuevo_min = cola_prioridad.min()
   print(f'Ítem mínimo después de la eliminación: {nuevo_min}')  
   cola_prioridad.add(0, 'tarea 0')  
   cola_prioridad.add(6, 'tarea 6')
   print(f'Total de elementos después de agregar: {len(cola_prioridad)}')
   print(cola_prioridad.__str__())

if __name__ == "__main__":
    SortedPriorityQueueClient()