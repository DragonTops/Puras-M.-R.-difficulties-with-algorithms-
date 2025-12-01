from typing import List, Set
from collections import deque
import time
import matplotlib.pyplot as plt
import random
from graph_representation import AdjacencyList, AdjacencyMatrix

def bfs_adjacency_list(graph: AdjacencyList, start: int) -> List[int]:
    """Поиск в ширину для списка смежности. Сложность O(V + E)."""
    visited = [False] * graph.vertices
    distances = [-1] * graph.vertices
    queue = deque([start])
    
    visited[start] = True
    distances[start] = 0
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get_neighbors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances


def dfs_adjacency_list_recursive(graph: AdjacencyList, start: int) -> List[int]:
    """Рекурсивный поиск в глубину для списка смежности. Сложность O(V + E)."""
    visited = [False] * graph.vertices
    result = []
    
    def dfs_util(vertex: int):
        visited[vertex] = True
        result.append(vertex)
        for neighbor in graph.get_neighbors(vertex):
            if not visited[neighbor]:
                dfs_util(neighbor)
    
    dfs_util(start)
    return result


def dfs_adjacency_list_iterative(graph: AdjacencyList, start: int) -> List[int]:
    """Итеративный поиск в глубину для списка смежности. Сложность O(V + E)."""
    visited = [False] * graph.vertices
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            # Добавляем соседей в обратном порядке для сохранения порядка обхода
            neighbors = graph.get_neighbors(vertex)
            for neighbor in reversed(neighbors):
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return result


def bfs_adjacency_matrix(graph: AdjacencyMatrix, start: int) -> List[int]:
    """Поиск в ширину для матрицы смежности. Сложность O(V²)."""
    visited = [False] * graph.vertices
    distances = [-1] * graph.vertices
    queue = deque([start])
    
    visited[start] = True
    distances[start] = 0
    
    while queue:
        vertex = queue.popleft()
        for neighbor in range(graph.vertices):
            if graph.matrix[vertex][neighbor] != 0 and not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return distances


def compare_traversal_performance():
    """Сравнение производительности алгоритмов обхода."""
    sizes = [10, 50, 100, 200, 500]
    bfs_times = []
    dfs_recursive_times = []
    dfs_iterative_times = []
    
    for size in sizes:
        # Создание тестового графа
        graph = AdjacencyList(size)
        for i in range(size):
            for j in range(i + 1, min(i + 5, size)):
                graph.add_edge(i, j)
        
        # Измерение времени BFS
        start_time = time.time()
        bfs_adjacency_list(graph, 0)
        bfs_times.append(time.time() - start_time)
        
        # Измерение времени DFS рекурсивного
        start_time = time.time()
        dfs_adjacency_list_recursive(graph, 0)
        dfs_recursive_times.append(time.time() - start_time)
        
        # Измерение времени DFS итеративного
        start_time = time.time()
        dfs_adjacency_list_iterative(graph, 0)
        dfs_iterative_times.append(time.time() - start_time)
    
    # График BFS
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, bfs_times, 'ro-', label='BFS')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время (секунды)')
    plt.title('Время выполнения BFS')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/bfs_performance.png')
    plt.close()
    
    # График DFS
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, dfs_recursive_times, 'go-', label='DFS Рекурсивный')
    plt.plot(sizes, dfs_iterative_times, 'bo-', label='DFS Итеративный')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время (секунды)')
    plt.title('Время выполнения DFS')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/dfs_performance.png')
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs('pics', exist_ok=True)
    compare_traversal_performance()