from typing import Any, Tuple
from heap import MinHeap

class PriorityQueue:
    """Приоритетная очередь на основе min-heap"""
    
    def __init__(self) -> None:
        self.heap = MinHeap()
    
    def enqueue(self, item: Any, priority: float) -> None:
        """Добавление элемента в очередь. Сложность: O(log n)"""
        self.heap.insert((priority, item))
    
    def dequeue(self) -> Any:
        """Извлечение элемента с наивысшим приоритетом. Сложность: O(log n)"""
        if len(self.heap) == 0:
            raise IndexError("Очередь пуста")
        
        priority, item = self.heap.extract_min()
        return item
    
    def peek(self) -> Any:
        """Просмотр элемента с наивысшим приоритетом. Сложность: O(1)"""
        if len(self.heap) == 0:
            raise IndexError("Очередь пуста")
        
        priority, item = self.heap.peek()
        return item
    
    def __len__(self) -> int:
        return len(self.heap)