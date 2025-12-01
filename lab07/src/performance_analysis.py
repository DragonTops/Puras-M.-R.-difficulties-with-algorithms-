import time
import random
import matplotlib.pyplot as plt
from typing import List, Callable
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace

def measure_time(func: Callable, *args) -> float:
    """Измерение времени выполнения функции"""
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def analyze_heap_operations() -> None:
    """Анализ производительности операций кучи"""
    sizes = [100, 500, 1000, 2000, 5000]
    insert_times = []
    extract_times = []
    
    for size in sizes:
        heap = MinHeap()
        
        # Измерение времени вставки
        start = time.perf_counter()
        for i in range(size):
            heap.insert(random.randint(1, 10000))
        insert_times.append(time.perf_counter() - start)
        
        # Измерение времени извлечения
        start = time.perf_counter()
        while len(heap) > 0:
            heap.extract_min()
        extract_times.append(time.perf_counter() - start)
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insert_times, marker='o', label='Вставка')
    plt.plot(sizes, extract_times, marker='s', label='Извлечение')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время (секунды)')
    plt.title('Производительность операций кучи')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/heap_operations.png')
    plt.close()

def compare_heap_build_methods() -> None:
    """Сравнение методов построения кучи"""
    sizes = [1000, 2000, 5000, 10000]
    sequential_times = []
    build_heap_times = []
    
    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        
        # Последовательная вставка
        heap = MinHeap()
        sequential_times.append(measure_time(lambda: [heap.insert(x) for x in data]))
        
        # Построение кучи из массива
        heap = MinHeap()
        build_heap_times.append(measure_time(heap.build_heap, data))
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, sequential_times, marker='o', label='Последовательная вставка')
    plt.plot(sizes, build_heap_times, marker='s', label='Build Heap')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение методов построения кучи')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/heap_build_comparison.png')
    plt.close()

def compare_sorting_algorithms() -> None:
    """Сравнение алгоритмов сортировки"""
    sizes = [100, 500, 1000, 2000, 5000]
    heapsort_times = []
    heapsort_inplace_times = []
    builtin_sort_times = []
    
    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        
        # Heapsort
        heapsort_times.append(measure_time(heapsort, data.copy()))
        
        # In-place Heapsort
        data_copy = data.copy()
        heapsort_inplace_times.append(measure_time(heapsort_inplace, data_copy))
        
        # Built-in sort
        builtin_sort_times.append(measure_time(sorted, data.copy()))
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, heapsort_times, marker='o', label='Heapsort')
    plt.plot(sizes, heapsort_inplace_times, marker='s', label='In-place Heapsort')
    plt.plot(sizes, builtin_sort_times, marker='^', label='Built-in Sort')
    plt.xlabel('Количество элементов')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение алгоритмов сортировки')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/sorting_comparison.png')
    plt.close()

if __name__ == "__main__":
    import os
    os.makedirs('pics', exist_ok=True)
    
    analyze_heap_operations()
    compare_heap_build_methods()
    compare_sorting_algorithms()
    print("Графики сохранены в папке pics/")