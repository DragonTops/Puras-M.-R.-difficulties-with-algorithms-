import time
import random
import matplotlib.pyplot as plt
import numpy as np
from prefix_function import prefix_function
from kmp_search import kmp_search
from z_function import z_function
from z_function import z_search
from rabin_karp import rabin_karp_search


def generate_test_strings(length: int, pattern_length: int) -> tuple[str, str]:
    """Генерация тестовых строк."""
    alphabet = "abc"
    
    # Генерируем текст
    text = ''.join(random.choice(alphabet) for _ in range(length))
    
    # Генерируем паттерн
    if pattern_length > 0:
        pattern = ''.join(random.choice(alphabet) for _ in range(pattern_length))
    else:
        pattern = ""
    
    return text, pattern


def measure_time(func, *args, repetitions: int = 10) -> float:
    """Измерение среднего времени выполнения функции."""
    times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    
    return sum(times) / len(times)


def compare_algorithms():
    """Сравнительный анализ алгоритмов поиска подстрок."""
    text_lengths = [1000, 5000, 10000, 50000]
    pattern_length = 10
    algorithms = [
        ("KMP", kmp_search),
        ("Z-функция", z_search),
        ("Рабин-Карп", rabin_karp_search)
    ]
    
    results = {name: [] for name, _ in algorithms}
    
    for length in text_lengths:
        text, pattern = generate_test_strings(length, pattern_length)
        
        for name, algorithm in algorithms:
            time_taken = measure_time(algorithm, text, pattern)
            results[name].append(time_taken)
            print(f"{name}: длина текста {length}, время {time_taken:.6f} сек")
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(text_lengths, times, marker='o', label=name)
    
    plt.xlabel('Длина текста')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение алгоритмов поиска подстрок')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/performance_comparison.png')
    plt.close()


def analyze_text_length_impact():
    """Анализ влияния длины текста на производительность."""
    text_lengths = range(1000, 10001, 1000)
    pattern = "abc"
    
    algorithms = [
        ("KMP", kmp_search),
        ("Z-функция", z_search),
        ("Рабин-Карп", rabin_karp_search)
    ]
    
    results = {name: [] for name, _ in algorithms}
    
    for length in text_lengths:
        text = 'a' * length + pattern
        
        for name, algorithm in algorithms:
            time_taken = measure_time(algorithm, text, pattern)
            results[name].append(time_taken)
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(text_lengths, times, marker='o', label=name)
    
    plt.xlabel('Длина текста')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Влияние длины текста на производительность')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/text_length_impact.png')
    plt.close()


def analyze_pattern_length_impact():
    """Анализ влияния длины паттерна на производительность."""
    text_length = 10000
    pattern_lengths = range(1, 101, 10)
    
    algorithms = [
        ("KMP", kmp_search),
        ("Z-функция", z_search),
        ("Рабин-Карп", rabin_karp_search)
    ]
    
    results = {name: [] for name, _ in algorithms}
    
    for p_length in pattern_lengths:
        text, pattern = generate_test_strings(text_length, p_length)
        
        for name, algorithm in algorithms:
            time_taken = measure_time(algorithm, text, pattern)
            results[name].append(time_taken)
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(pattern_lengths, times, marker='o', label=name)
    
    plt.xlabel('Длина паттерна')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Влияние длины паттерна на производительность')
    plt.legend()
    plt.grid(True)
    plt.savefig('pics/pattern_length_impact.png')
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs('pics', exist_ok=True)
    
    print("Запуск сравнительного анализа алгоритмов...")
    compare_algorithms()
    
    print("Анализ влияния длины текста...")
    analyze_text_length_impact()
    
    print("Анализ влияния длины паттерна...")
    analyze_pattern_length_impact()
    
    print("Графики сохранены в папку pics/")