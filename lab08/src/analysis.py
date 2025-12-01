import time
import matplotlib.pyplot as plt
from typing import List, Tuple
import itertools
import os

def exact_knapsack_01(capacity: int, items: List[Tuple[int, int]]) -> int:
    """
    Точное решение задачи о рюкзаке 0-1 полным перебором.
    
    Args:
        capacity: Вместимость рюкзака
        items: Список предметов в формате (вес, стоимость)
    
    Returns:
        Максимальная стоимость
    """
    n = len(items)
    max_value = 0
    
    for i in range(1, n + 1):
        for combination in itertools.combinations(items, i):
            total_weight = sum(item[0] for item in combination)
            total_value = sum(item[1] for item in combination)
            
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
    
    return max_value

def fractional_knapsack(capacity: int, items: List[Tuple[int, int]]) -> float:
    """
    Решение задачи о непрерывном рюкзаке.
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

def compare_knapsack_algorithms():
    """
    Сравнительный анализ жадного и точного алгоритмов для задачи о рюкзаке.
    """
    # Тестовые данные
    test_cases = [
        (50, [(10, 60), (20, 100), (30, 120)]),
        (10, [(5, 10), (4, 40), (6, 30), (3, 50)]),
        (15, [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]),
    ]
    
    results = []
    
    for capacity, items in test_cases:
        # Жадный алгоритм (непрерывный рюкзак)
        greedy_result = fractional_knapsack(capacity, items)
        
        # Точный алгоритм (0-1 рюкзак)
        exact_result = exact_knapsack_01(capacity, items)
        
        results.append({
            'capacity': capacity,
            'items': items,
            'greedy': greedy_result,
            'exact': exact_result,
            'difference': abs(greedy_result - exact_result)
        })
    
    return results

def plot_comparison(results: List[dict]):
    """
    Построение графика сравнения алгоритмов.
    """
    if not os.path.exists('pics'):
        os.makedirs('pics')
    
    cases = range(len(results))
    greedy_values = [r['greedy'] for r in results]
    exact_values = [r['exact'] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.bar([x - 0.2 for x in cases], greedy_values, width=0.4, label='Жадный алгоритм', alpha=0.7)
    plt.bar([x + 0.2 for x in cases], exact_values, width=0.4, label='Точный алгоритм', alpha=0.7)
    
    plt.xlabel('Тестовые случаи')
    plt.ylabel('Максимальная стоимость')
    plt.title('Сравнение жадного и точного алгоритмов для задачи о рюкзаке')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('pics/knapsack_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def performance_analysis():
    """
    Анализ производительности алгоритмов.
    """
    sizes = [5, 10, 15, 20]
    greedy_times = []
    exact_times = []
    
    for size in sizes:
        # Генерация тестовых данных
        items = [(i + 1, (i + 1) * 10) for i in range(size)]
        capacity = sum(item[0] for item in items) // 2
        
        # Замер времени для жадного алгоритма
        start_time = time.time()
        fractional_knapsack(capacity, items)
        greedy_time = time.time() - start_time
        greedy_times.append(greedy_time)
        
        # Замер времени для точного алгоритма (только для небольших размеров)
        if size <= 15:
            start_time = time.time()
            exact_knapsack_01(capacity, items)
            exact_time = time.time() - start_time
            exact_times.append(exact_time)
        else:
            exact_times.append(float('nan'))
    
    # Построение графика производительности
    plt.figure(figsize=(10, 6))
    plt.plot(sizes[:len(exact_times)], exact_times, marker='o', label='Точный алгоритм', linewidth=2)
    plt.plot(sizes, greedy_times, marker='s', label='Жадный алгоритм', linewidth=2)
    
    plt.xlabel('Количество предметов')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение производительности алгоритмов')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    
    plt.savefig('pics/performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Сравнительный анализ алгоритмов:")
    
    # Сравнение результатов
    results = compare_knapsack_algorithms()
    for i, result in enumerate(results):
        print(f"Случай {i + 1}:")
        print(f"  Вместимость: {result['capacity']}")
        print(f"  Предметы: {result['items']}")
        print(f"  Жадный алгоритм: {result['greedy']:.2f}")
        print(f"  Точный алгоритм: {result['exact']}")
        print(f"  Разница: {result['difference']:.2f}")
        print()
    
    # Построение графиков
    plot_comparison(results)
    performance_analysis()
    print("Графики сохранены в папке pics/")