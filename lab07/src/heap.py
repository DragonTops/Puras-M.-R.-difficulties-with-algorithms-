from typing import Any, List, Optional

class MinHeap:
    """Реализация min-heap на основе массива"""
    
    def __init__(self) -> None:
        self.heap: List[Any] = []
    
    def insert(self, value: Any) -> None:
        """Вставка элемента в кучу. Сложность: O(log n)"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def extract_min(self) -> Any:
        """Извлечение минимального элемента. Сложность: O(log n)"""
        if not self.heap:
            raise IndexError("Куча пуста")
        
        min_val = self.heap[0]
        last_val = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)
        
        return min_val
    
    def peek(self) -> Any:
        """Просмотр минимального элемента. Сложность: O(1)"""
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def build_heap(self, array: List[Any]) -> None:
        """Построение кучи из массива. Сложность: O(n)"""
        self.heap = array[:]
        n = len(self.heap)
        
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def _sift_up(self, index: int) -> None:
        """Всплытие элемента. Сложность: O(log n)"""
        parent = (index - 1) // 2
        
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
    
    def _sift_down(self, index: int) -> None:
        """Погружение элемента. Сложность: O(log n)"""
        n = len(self.heap)
        
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    
    def __len__(self) -> int:
        return len(self.heap)


class MaxHeap:
    """Реализация max-heap на основе массива"""
    
    def __init__(self) -> None:
        self.heap: List[Any] = []
    
    def insert(self, value: Any) -> None:
        """Вставка элемента в кучу. Сложность: O(log n)"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def extract_max(self) -> Any:
        """Извлечение максимального элемента. Сложность: O(log n)"""
        if not self.heap:
            raise IndexError("Куча пуста")
        
        max_val = self.heap[0]
        last_val = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)
        
        return max_val
    
    def build_heap(self, array: List[Any]) -> None:
        """Построение кучи из массива. Сложность: O(n)"""
        self.heap = array[:]
        n = len(self.heap)
        
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def _sift_up(self, index: int) -> None:
        """Всплытие элемента. Сложность: O(log n)"""
        parent = (index - 1) // 2
        
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
    
    def _sift_down(self, index: int) -> None:
        """Погружение элемента. Сложность: O(log n)"""
        n = len(self.heap)
        
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == index:
                break
            
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
    
    def __len__(self) -> int:
        return len(self.heap)