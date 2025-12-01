from typing import List
import random
from graph_representation import AdjacencyList
from graph_traversal import bfs_adjacency_list
from shortest_path import dijkstra, connected_components, topological_sort

def maze_shortest_path(maze_size: int = 5) -> List[int]:
    """Поиск кратчайшего пути в лабиринте."""
    # Создание простого лабиринта (графа)
    graph = AdjacencyList(maze_size * maze_size)
    
    # Добавление ребер между соседними клетками
    for i in range(maze_size):
        for j in range(maze_size):
            current = i * maze_size + j
            if j < maze_size - 1:
                graph.add_edge(current, current + 1)  # право
            if i < maze_size - 1:
                graph.add_edge(current, current + maze_size)  # низ
    
    # Поиск кратчайшего пути от начала до конца
    distances = bfs_adjacency_list(graph, 0)
    return distances

def network_connectivity() -> int:
    """Определение связности сети."""
    graph = AdjacencyList(10)
    # Создание случайной сети
    for _ in range(15):
        u = random.randint(0, 9)
        v = random.randint(0, 9)
        if u != v:
            graph.add_edge(u, v)
    
    components = connected_components(graph)
    return len(components)

def task_dependencies() -> List[int]:
    """Топологическая сортировка для задач с зависимостями."""
    graph = AdjacencyList(6)  # 6 задач
    
    # Зависимости: задача 0 -> задача 1, задача 1 -> задача 2, и т.д.
    dependencies = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    for dep in dependencies:
        graph.add_edge(dep[0], dep[1])
    
    return topological_sort(graph)

def solve_practical_tasks():
    """Решение практических задач."""
    print("=== Решение практических задач ===")
    
    # Задача 1: Кратчайший путь в лабиринте
    print("\n1. Кратчайший путь в лабиринте 5x5:")
    maze_distances = maze_shortest_path()
    print(f"Расстояния от начальной точки: {maze_distances}")
    
    # Задача 2: Связность сети
    print("\n2. Анализ связности сети:")
    component_count = network_connectivity()
    print(f"Количество компонент связности: {component_count}")
    
    # Задача 3: Топологическая сортировка
    print("\n3. Топологическая сортировка задач:")
    task_order = task_dependencies()
    print(f"Порядок выполнения задач: {task_order}")
    
    # Задача 4: Алгоритм Дейкстры
    print("\n4. Алгоритм Дейкстры:")
    graph = AdjacencyList(5)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 3)
    
    distances = dijkstra(graph, 0)
    print(f"Кратчайшие расстояния от вершины 0: {distances}")

if __name__ == "__main__":
    solve_practical_tasks()