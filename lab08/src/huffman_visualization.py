import time
import matplotlib.pyplot as plt
import heapq
import random
import os
import math
from typing import Dict, List, Tuple

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

def generate_random_frequencies(n: int) -> Dict[str, int]:
    """
    Генерация случайных частот для n символов.
    """
    frequencies = {}
    for i in range(n):
        char = chr(ord('a') + i)
        frequencies[char] = random.randint(1, 100)
    return frequencies

def measure_huffman_performance():
    """
    Замер времени работы алгоритма Хаффмана на данных разного размера.
    """
    sizes = [10, 50, 100, 200, 500, 1000, 2000]
    times = []
    
    for size in sizes:
        frequencies = generate_random_frequencies(size)
        
        start_time = time.time()
        huffman_coding(frequencies)
        end_time = time.time()
        
        execution_time = end_time - start_time
        times.append(execution_time)
        
        print(f"Размер: {size}, Время: {execution_time:.6f} сек")
    
    return sizes, times

def plot_huffman_tree(frequencies: Dict[str, int], codes: Dict[str, str]):
    """
    Визуализация дерева Хаффмана (упрощенная версия).
    """
    if not os.path.exists('pics'):
        os.makedirs('pics')
    
    # Создаем текстовое представление дерева
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    tree_text = "Дерево кодов Хаффмана:\n\n"
    for char, code in sorted(codes.items()):
        tree_text += f"'{char}' (частота: {frequencies[char]}): {code}\n"
    
    ax.text(0.1, 0.9, tree_text, fontfamily='monospace', fontsize=10, 
            verticalalignment='top', transform=ax.transAxes)
    
    plt.title('Коды Хаффмана')
    plt.savefig('pics/huffman_tree.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_performance(sizes: List[int], times: List[float]):
    """
    Построение графика зависимости времени работы от размера входных данных.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'b-o', linewidth=2, markersize=6)
    plt.xlabel('Количество символов')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Зависимость времени работы алгоритма Хаффмана от размера данных')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.xscale('log')
    
    plt.savefig('pics/huffman_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

def analyze_compression_ratio():
    """
    Анализ эффективности сжатия алгоритмом Хаффмана.
    """
    test_cases = [
        {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45},
        {'a': 10, 'b': 15, 'c': 20, 'd': 25, 'e': 30},
        generate_random_frequencies(8)
    ]
    
    for i, frequencies in enumerate(test_cases):
        codes = huffman_coding(frequencies)
        
        # Расчет средней длины кода
        total_freq = sum(frequencies.values())
        avg_length = sum(freq * len(codes[char]) for char, freq in frequencies.items()) / total_freq
        
        # Расчет энтропии (исправленная формула)
        entropy = 0.0
        for freq in frequencies.values():
            probability = freq / total_freq
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        print(f"Тестовый случай {i + 1}:")
        print(f"  Средняя длина кода: {avg_length:.3f}")
        print(f"  Энтропия: {entropy:.3f}")
        print(f"  Эффективность: {entropy/avg_length:.3f}")
        print()

if __name__ == "__main__":
    print("Анализ алгоритма Хаффмана:")
    
    # Тестовые данные
    frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    codes = huffman_coding(frequencies)
    
    print("Коды Хаффмана для тестовых данных:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")
    
    # Визуализация дерева
    plot_huffman_tree(frequencies, codes)
    print("Дерево Хаффмана сохранено в pics/huffman_tree.png")
    
    # Анализ производительности
    print("\nИзмерение производительности:")
    sizes, times = measure_huffman_performance()
    plot_performance(sizes, times)
    print("График производительности сохранен в pics/huffman_performance.png")
    
    # Анализ эффективности сжатия
    print("\nАнализ эффективности сжатия:")
    analyze_compression_ratio()