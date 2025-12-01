import time
import random
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
from binary_search_tree import BinarySearchTree, TreeNode
import os
import math

def generate_balanced_tree(elements: List[int]) -> TreeNode:
    """Генерация сбалансированного дерева из отсортированного массива"""
    def build_balanced_tree(arr: List[int], start: int, end: int) -> Optional[TreeNode]:
        """Вспомогательная функция для построения сбалансированного дерева"""
        if start > end:
            return None
            
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        root.left = build_balanced_tree(arr, start, mid - 1)
        root.right = build_balanced_tree(arr, mid + 1, end)
        return root
    
    sorted_elements = sorted(elements)
    return build_balanced_tree(sorted_elements, 0, len(sorted_elements) - 1)

def generate_degenerate_tree(elements: List[int]) -> TreeNode:
    """Генерация вырожденного дерева (связный список) с итеративной вставкой"""
    bst = BinarySearchTree()
    root = None
    
    # Сортируем элементы для создания вырожденного дерева
    sorted_elements = sorted(elements)
    
    for elem in sorted_elements:
        root = bst.insert_iterative(root, elem)
    return root

def measure_search_time(root: TreeNode, searches: int) -> float:
    """Измерение времени выполнения операций поиска"""
    bst = BinarySearchTree()
    elements = []
    
    # Собираем все элементы дерева для поиска (итеративно)
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            elements.append(node.value)
            stack.append(node.left)
            stack.append(node.right)
    
    if not elements:
        return 0.0
        
    start_time = time.time()
    for _ in range(searches):
        target = random.choice(elements)
        bst.search_iterative(root, target)
    end_time = time.time()
    
    return end_time - start_time

def analyze_performance():
    """Анализ производительности для разных размеров деревьев"""
    sizes = [100, 500, 1000]  # Уменьшили размеры для избежания рекурсии
    balanced_times = []
    degenerate_times = []
    
    for size in sizes:
        elements = random.sample(range(size * 10), size)
        
        # Сбалансированное дерево
        balanced_root = generate_balanced_tree(elements)
        balanced_time = measure_search_time(balanced_root, 100)
        balanced_times.append(balanced_time)
        
        # Вырожденное дерево
        degenerate_root = generate_degenerate_tree(elements)
        degenerate_time = measure_search_time(degenerate_root, 100)
        degenerate_times.append(degenerate_time)
        
        print(f"Размер: {size}, Сбалансированное: {balanced_time:.4f}s, Вырожденное: {degenerate_time:.4f}s")
    
    return sizes, balanced_times, degenerate_times

def plot_performance_comparison(sizes: List[int], balanced_times: List[float], degenerate_times: List[float]):
    """Построение графика сравнения производительности"""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, balanced_times, 'b-', label='Сбалансированное дерево', marker='o')
    plt.plot(sizes, degenerate_times, 'r-', label='Вырожденное дерево', marker='s')
    plt.xlabel('Количество элементов в дереве')
    plt.ylabel('Время поиска (секунды)')
    plt.title('Сравнение производительности поиска в BST')
    plt.legend()
    plt.grid(True)
    
    # Создаем папку pics если её нет
    os.makedirs('pics', exist_ok=True)
    plt.savefig('pics/performance_comparison.png')
    plt.close()

def plot_time_complexity(sizes: List[int], balanced_times: List[float], degenerate_times: List[float]):
    """Построение графика зависимости времени от количества элементов"""
    plt.figure(figsize=(10, 6))
    
    # Теоретические сложности (нормализованные для визуализации)
    logn = [0.0001 * size * math.log2(size + 1) for size in sizes]  # O(n log n) приближение
    linear = [0.0001 * size for size in sizes]  # O(n) приближение
    
    plt.plot(sizes, balanced_times, 'bo-', label='Сбалансированное (эксперимент)')
    plt.plot(sizes, degenerate_times, 'rs-', label='Вырожденное (эксперимент)')
    plt.plot(sizes, logn, 'g--', label='O(n log n) теоретическая')
    plt.plot(sizes, linear, 'm--', label='O(n) теоретическая')
    
    plt.xlabel('Количество элементов')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Зависимость времени операций от количества элементов')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('pics/time_vs_elements.png')
    plt.close()

def main():
    """Основная функция анализа"""
    print("Анализ производительности BST...")
    
    # Анализ производительности
    sizes, balanced_times, degenerate_times = analyze_performance()
    
    # Построение графиков
    plot_performance_comparison(sizes, balanced_times, degenerate_times)
    plot_time_complexity(sizes, balanced_times, degenerate_times)
    
    print("Графики сохранены в папку pics/")
    
    # Демонстрация текстовой визуализации
    bst = BinarySearchTree()
    demo_elements = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for elem in demo_elements:
        root = bst.insert_iterative(root, elem)
    
    print("\nТекстовая визуализация демонстрационного дерева:")
    tree_lines = bst.print_tree(root)
    for line in tree_lines:
        print(line)
    
    # Демонстрация дополнительных методов
    print(f"\nВысота дерева: {bst.height_iterative(root)}")
    print(f"Минимальный элемент: {bst.find_min_iterative(root).value}")
    print(f"Максимальный элемент: {bst.find_max_iterative(root).value}")
    print(f"Является корректным BST: {bst.is_valid_bst_iterative(root)}")

if __name__ == "__main__":
    main()