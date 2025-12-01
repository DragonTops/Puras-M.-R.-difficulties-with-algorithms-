from typing import List, Dict, Set, Any
import time
import matplotlib.pyplot as plt
import numpy as np
import sys

class AdjacencyMatrix:
    """Класс для представления графа матрицей смежности."""
    
    def __init__(self, vertices: int):
        self.matrix = [[0] * vertices for _ in range(vertices)]
        self.vertices = vertices
        self.edge_count = 0
    
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Добавление ребра между вершинами u и v. Сложность O(1)."""
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.matrix[u][v] = weight
            self.matrix[v][u] = weight
            self.edge_count += 1
    
    def remove_edge(self, u: int, v: int) -> None:
        """Удаление ребра между вершинами u и v. Сложность O(1)."""
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.matrix[u][v] = 0
            self.matrix[v][u] = 0
            self.edge_count -= 1
    
    def has_edge(self, u: int, v: int) -> bool:
        """Проверка наличия ребра между u и v. Сложность O(1)."""
        return 0 <= u < self.vertices and 0 <= v < self.vertices and self.matrix[u][v] != 0
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """Получение списка соседей вершины. Сложность O(V)."""
        if 0 <= vertex < self.vertices:
            return [i for i in range(self.vertices) if self.matrix[vertex][i] != 0]
        return []
    
    def get_memory_usage(self) -> int:
        """Оценка использования памяти в байтах."""
        return sys.getsizeof(self.matrix) + sum(sys.getsizeof(row) for row in self.matrix)


class AdjacencyList:
    """Класс для представления графа списком смежности."""
    
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adj_list: List[Dict[int, int]] = [{} for _ in range(vertices)]
        self.edge_count = 0
    
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Добавление ребра между вершинами u и v. Сложность O(1)."""
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u][v] = weight
            self.adj_list[v][u] = weight
            self.edge_count += 1
    
    def remove_edge(self, u: int, v: int) -> None:
        """Удаление ребра между вершинами u и v. Сложность O(1)."""
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            if v in self.adj_list[u]:
                del self.adj_list[u][v]
                del self.adj_list[v][u]
                self.edge_count -= 1
    
    def has_edge(self, u: int, v: int) -> bool:
        """Проверка наличия ребра между u и v. Сложность O(deg(u))."""
        return 0 <= u < self.vertices and v in self.adj_list[u]
    
    def get_neighbors(self, vertex: int) -> List[int]:
        """Получение списка соседей вершины. Сложность O(deg(v))."""
        if 0 <= vertex < self.vertices:
            return list(self.adj_list[vertex].keys())
        return []
    
    def get_neighbors_with_weights(self, vertex: int) -> List[tuple[int, int]]:
        """Получение списка соседей с весами."""
        if 0 <= vertex < self.vertices:
            return list(self.adj_list[vertex].items())
        return []
    
    def get_memory_usage(self) -> int:
        """Оценка использования памяти в байтах."""
        total = sys.getsizeof(self.adj_list)
        for item in self.adj_list:
            total += sys.getsizeof(item)
        return total


def compare_representations():
    """Сравнение производительности представлений графов."""
    sizes = [10, 50, 100, 200, 500]
    matrix_times = []
    list_times = []
    matrix_memory = []
    list_memory = []
    
    for size in sizes:
        # Тест времени добавления ребер
        matrix_graph = AdjacencyMatrix(size)
        list_graph = AdjacencyList(size)
        
        start_time = time.time()
        for i in range(size):
            for j in range(i + 1, min(i + 10, size)):
                matrix_graph.add_edge(i, j)
        matrix_times.append(time.time() - start_time)
        
        start_time = time.time()
        for i in range(size):
            for j in range(i + 1, min(i + 10, size)):
                list_graph.add_edge(i, j)
        list_times.append(time.time() - start_time)
        
        # Тест использования памяти
        matrix_memory.append(matrix_graph.get_memory_usage())
        list_memory.append(list_graph.get_memory_usage())
    
    # График времени добавления ребер
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, matrix_times, 'ro-', label='Матрица смежности')
    plt.plot(sizes, list_times, 'bo-', label='Список смежности')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение времени добавления ребер')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/edge_addition_comparison.png')
    plt.close()
    
    # График использования памяти
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, matrix_memory, 'ro-', label='Матрица смежности')
    plt.plot(sizes, list_memory, 'bo-', label='Список смежности')
    plt.xlabel('Количество вершин')
    plt.ylabel('Память (байты)')
    plt.title('Сравнение памяти')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/memory_comparison.png')
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs('pics', exist_ok=True)
    compare_representations()