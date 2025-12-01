from typing import List, Tuple, Dict, Any
import heapq
from collections import defaultdict

def interval_scheduling(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Выбор максимального количества непересекающихся интервалов.
    
    Args:
        intervals: Список интервалов в формате (начало, конец)
    
    Returns:
        Список выбранных интервалов
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[1])
    selected = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] >= selected[-1][1]:
            selected.append(interval)
    
    return selected

def fractional_knapsack(capacity: int, items: List[Tuple[int, int]]) -> float:
    """
    Решение задачи о непрерывном рюкзаке.
    
    Args:
        capacity: Вместимость рюкзака
        items: Список предметов в формате (вес, стоимость)
    
    Returns:
        Максимальная стоимость содержимого рюкзака
    """
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    current_capacity = capacity
    
    for weight, value in items:
        if current_capacity >= weight:
            total_value += value
            current_capacity -= weight
        else:
            total_value += value * (current_capacity / weight)
            break
    
    return total_value

class HuffmanNode:
    """Узел дерева Хаффмана."""
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(frequencies: Dict[str, int]) -> Dict[str, str]:
    """
    Построение кодов Хаффмана для заданных частот.
    
    Args:
        frequencies: Словарь частот символов
    
    Returns:
        Словарь кодов Хаффмана
    """
    heap = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, (freq, HuffmanNode(char, freq)))
    
    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)
        
        merged = HuffmanNode(None, freq1 + freq2)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, (freq1 + freq2, merged))
    
    codes = {}
    
    def generate_codes(node: HuffmanNode, code: str):
        if node is None:
            return
        
        if node.char is not None:
            codes[node.char] = code
            return
        
        generate_codes(node.left, code + '0')
        generate_codes(node.right, code + '1')
    
    if heap:
        generate_codes(heap[0][1], "")
    
    return codes

def coin_change(amount: int, coins: List[int]) -> List[int]:
    """
    Задача о минимальном количестве монет.
    
    Args:
        amount: Сумма для выдачи
        coins: Доступные номиналы монет
    
    Returns:
        Список монет для выдачи сдачи
    """
    coins.sort(reverse=True)
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return result

def kruskal_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Алгоритм Краскала для построения минимального остовного дерева.
    
    Args:
        vertices: Количество вершин
        edges: Список рёбер в формате (вершина1, вершина2, вес)
    
    Returns:
        Список рёбер минимального остовного дерева
    """
    parent = list(range(vertices))
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    edges.sort(key=lambda x: x[2])
    mst = []
    
    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
        if len(mst) == vertices - 1:
            break
    
    return mst

if __name__ == "__main__":
    # Тестирование алгоритмов
    print("Тестирование жадных алгоритмов:")
    
    # Задача о выборе заявок
    intervals = [(1, 3), (2, 4), (3, 5), (0, 6)]
    result = interval_scheduling(intervals)
    print(f"Выбранные интервалы: {result}")
    
    # Непрерывный рюкзак
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    result = fractional_knapsack(capacity, items)
    print(f"Максимальная стоимость рюкзака: {result}")
    
    # Алгоритм Хаффмана
    frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    codes = huffman_coding(frequencies)
    print(f"Коды Хаффмана: {codes}")
    
    # Задача о монетах
    coins = [1, 5, 10, 25]
    amount = 63
    result = coin_change(amount, coins)
    print(f"Монеты для сдачи: {result}")