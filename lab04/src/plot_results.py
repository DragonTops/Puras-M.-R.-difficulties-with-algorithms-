import matplotlib.pyplot as plt
import numpy as np
from performance_test import run_performance_tests

def plot_results(results: dict):
    sizes = [100, 1000, 5000, 10000]
    algorithms = list(results.keys())
    
    # График для случайных данных
    plt.figure(figsize=(12, 8))
    
    for algo in algorithms:
        times = [results[algo][f'random_{size}'] for size in sizes]
        plt.plot(sizes, times, marker='o', label=algo)
    
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение алгоритмов сортировки (случайные данные)')
    plt.legend()
    plt.grid(True)
    plt.savefig('random_comparison.png')
    plt.show()

def plot_data_type_comparison(results: dict, size: int = 5000):
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    algorithms = list(results.keys())
    
    plt.figure(figsize=(12, 8))
    
    x = np.arange(len(data_types))
    width = 0.15
    
    for i, algo in enumerate(algorithms):
        times = [results[algo][f'{data_type}_{size}'] for data_type in data_types]
        plt.bar(x + i * width, times, width, label=algo)
    
    plt.xlabel('Тип данных')
    plt.ylabel('Время (секунды)')
    plt.title(f'Сравнение алгоритмов на разных типах данных (n={size})')
    plt.xticks(x + width * 2, data_types)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('data_type_comparison.png')
    plt.show()

if __name__ == "__main__":
    results = run_performance_tests()
    plot_results(results)
    plot_data_type_comparison(results)