"""
Сравнительный анализ алгоритмов ДП
"""

import time
import matplotlib.pyplot as plt
from typing import List, Tuple
from dynamic_programming import fibonacci_memo, fibonacci_tabular, knapsack_01

def compare_fibonacci() -> Tuple[List[float], List[float]]:
    """Сравнение времени выполнения нисходящего и восходящего подходов для Фибоначчи."""
    sizes = list(range(1, 101, 5))
    times_memo = []
    times_tabular = []
    
    for n in sizes:
        # Нисходящий подход
        start = time.time()
        fibonacci_memo(n)
        times_memo.append(time.time() - start)
        
        # Восходящий подход  
        start = time.time()
        fibonacci_tabular(n)
        times_tabular.append(time.time() - start)
    
    return times_memo, times_tabular, sizes

def plot_fibonacci_comparison() -> None:
    """Построение графика сравнения времени выполнения для Фибоначчи."""
    times_memo, times_tabular, sizes = compare_fibonacci()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_memo, label='Нисходящий (мемоизация)', marker='o')
    plt.plot(sizes, times_tabular, label='Восходящий (табличный)', marker='s')
    plt.xlabel('n')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение времени выполнения для чисел Фибоначчи')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/fibonacci_comparison.png')
    plt.close()

def scalability_analysis() -> None:
    """Анализ масштабируемости алгоритмов ДП."""
    capacities = [10, 20, 50, 100, 200]
    times_knapsack = []
    
    for capacity in capacities:
        weights = list(range(1, capacity // 2 + 1))
        values = [w * 2 for w in weights]
        
        start = time.time()
        knapsack_01(weights, values, capacity)
        times_knapsack.append(time.time() - start)
    
    plt.figure(figsize=(10, 6))
    plt.plot(capacities, times_knapsack, label='Задача о рюкзаке', marker='o')
    plt.xlabel('Вместимость рюкзака')
    plt.ylabel('Время (секунды)')
    plt.title('Масштабируемость алгоритма рюкзака')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/scalability_analysis.png')
    plt.close()

if __name__ == "__main__":
    plot_fibonacci_comparison()
    scalability_analysis()
    print("Графики сохранены в папке pics/")