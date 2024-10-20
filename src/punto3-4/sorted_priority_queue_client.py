from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from sorted_priority_queue import SortedPriorityQueue
class SortedPriorityQueueClient(SortedPriorityQueue, SortedPriorityQueueAbstract):
   cola_prioridad = SortedPriorityQueue()
   cola_prioridad.add(5, 'tarea 5')   
   cola_prioridad.add(1, 'tarea 1')  
   cola_prioridad.add(3, 'tarea 3')   
   cola_prioridad.add(2, 'tarea 2')   
   cola_prioridad.add(4, 'tarea 4')   
   print(f'Total de elementos en la cola de prioridad: {len(cola_prioridad)}')
   min_item = cola_prioridad.min()
   print(f'Ítem mínimo: {min_item}') 
   removed_item = cola_prioridad.remove_min()
   print(f'Ítem removido: {removed_item}')  
   nuevo_min = cola_prioridad.min()
   print(f'Nuevo ítem mínimo después de la eliminación: {nuevo_min}')  # Esperado: (2, 'tarea 2')
   cola_prioridad.add(0, 'tarea 0')  # Prioridad 0
   cola_prioridad.add(6, 'tarea 6')  # Prioridad 6
   print(f'Total de elementos después de agregar más: {len(cola_prioridad)}')
   print(cola_prioridad.__str__())

if __name__ == "__main__":
    SortedPriorityQueueClient()