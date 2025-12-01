from typing import Any, List
from heap import MinHeap

def heapsort(array: List[Any]) -> List[Any]:
    """Сортировка кучей с использованием дополнительной памяти. Сложность: O(n log n)"""
    heap = MinHeap()
    heap.build_heap(array)
    
    sorted_array = []
    while len(heap) > 0:
        sorted_array.append(heap.extract_min())
    
    return sorted_array

def _sift_down_max(arr: List[Any], n: int, i: int) -> None:
    """Вспомогательная функция для in-place heapsort (max-heap)"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _sift_down_max(arr, n, largest)

def heapsort_inplace(arr: List[Any]) -> None:
    """In-place сортировка кучей. Сложность: O(n log n)"""
    n = len(arr)
    
    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down_max(arr, n, i)
    
    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _sift_down_max(arr, i, 0)