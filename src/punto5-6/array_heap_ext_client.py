from array_heap_ext import ArrayHeapExt
class ArrayHeapExtClient(ArrayHeapExt):
    def probar_array_heap_ext():
        heap = ArrayHeapExt()
        heap.add(2, 'B')
        heap.add(5, 'A')
        heap.add(15, 'K')
        heap.add(16, 'X')
        heap.add(25, 'J')
        heap.add(9, 'F')
        heap.add(14, 'E')
        heap.add(12, 'H')
        heap.add(4, 'C')
        heap.add(7, 'Q')
        heap.add(11, 'S')
        heap.add(8, 'W')
        heap.add(6, 'Z')
        heap.add(20, 'B')
        heap.add(10, 'L')

        print("Heap inicial:")
        print(heap)
        
        
        print("\nProbando vaciar:")
        heap.vaciar()
        print(f"Heap después de vaciar: {heap}")  

        
        heap.add(10, 'A')
        heap.add(20, 'B')
        heap.add(5, 'C')
        heap.add(15, 'D')
        heap.add(7, 'E')

        print("\nHeap después de volver a agregar elementos:")
        print(heap)

        
        print("\nProbando eliminar_por_prioridad (eliminar con prioridad 7):")
        heap.eliminar_por_prioridad(7)
        print(f"Heap después de eliminar la prioridad 7: {heap}")

        
        print("\nProbando cambiar_prioridad (cambiar prioridad 10 a 12):")
        heap.cambiar_prioridad(10, 12)
        print(f"Heap después de cambiar la prioridad 10 a 12: {heap}")

       
        otro_heap = ArrayHeapExt()
        otro_heap.add(3, 'H')
        otro_heap.add(18, 'I')

        print("\nHeap a fusionar:")
        print(otro_heap)

        print("\nProbando fusionar:")
        heap.fusionar(otro_heap)
        print(f"Heap después de fusionar: {heap}")

    if __name__ == "__main__":
        probar_array_heap_ext()
        