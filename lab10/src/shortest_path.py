import heapq
from typing import List, Tuple
import random
import time
import matplotlib.pyplot as plt
from graph_representation import AdjacencyList

def dijkstra(graph: AdjacencyList, start: int) -> List[float]:
    """Алгоритм Дейкстры для поиска кратчайших путей. Сложность O((V + E) log V)."""
    distances = [float('inf')] * graph.vertices
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph.get_neighbors_with_weights(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def connected_components(graph: AdjacencyList) -> List[List[int]]:
    """Поиск компонент связности с помощью BFS. Сложность O(V + E)."""
    visited = [False] * graph.vertices
    components = []
    
    for vertex in range(graph.vertices):
        if not visited[vertex]:
            component = []
            queue = [vertex]
            visited[vertex] = True
            
            while queue:
                current = queue.pop(0)
                component.append(current)
                for neighbor in graph.get_neighbors(current):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            components.append(component)
    
    return components


def topological_sort(graph: AdjacencyList) -> List[int]:
    """Топологическая сортировка для DAG. Сложность O(V + E)."""
    in_degree = [0] * graph.vertices
    for vertex in range(graph.vertices):
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] += 1
    
    queue = [i for i in range(graph.vertices) if in_degree[i] == 0]
    result = []
    
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == graph.vertices else []


def analyze_dijkstra_performance():
    """Анализ производительности алгоритма Дейкстры."""
    sizes = [10, 50, 100, 200, 500]
    times = []
    
    for size in sizes:
        graph = AdjacencyList(size)
        # Создание связного графа
        for i in range(size - 1):
            graph.add_edge(i, i + 1, random.randint(1, 10))
        
        # Добавление случайных ребер
        for _ in range(size * 2):
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)
            if u != v:
                graph.add_edge(u, v, random.randint(1, 10))
        
        start_time = time.time()
        dijkstra(graph, 0)
        times.append(time.time() - start_time)
    
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, times, 'ro-')
    plt.xlabel('Количество вершин')
    plt.ylabel('Время (секунды)')
    plt.title('Производительность алгоритма Дейкстры')
    plt.grid(True)
    plt.savefig('pics/dijkstra_performance.png')
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs('pics', exist_ok=True)
    analyze_dijkstra_performance()