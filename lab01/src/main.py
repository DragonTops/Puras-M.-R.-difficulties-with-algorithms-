"""
Основной модуль для сравнения производительности алгоритмов поиска
"""
import time
import random
from search_algorithms import linear_search, binary_search
import matplotlib.pyplot as plt


def generate_sorted_array(size: int) -> list:
    """Генерация отсортированного массива"""
    return sorted(random.sample(range(size * 10), size))


def measure_time(search_func, arr: list, target: int) -> float:
    """Измерение времени выполнения поиска"""
    start_time = time.perf_counter()
    search_func(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time


def main():
    """Основная функция сравнения производительности"""
    # Параметры тестирования
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    test_cases = 100  # Количество тестов для усреднения

    linear_times = []
    binary_times = []

    print("Запуск сравнения производительности...")

    for size in sizes:
        arr = generate_sorted_array(size)
        linear_time_total = 0
        binary_time_total = 0

        for _ in range(test_cases):
            # Тестирование на случайном элементе
            target = random.choice(arr)

            linear_time_total += measure_time(linear_search, arr, target)
            binary_time_total += measure_time(binary_search, arr, target)

        avg_linear = linear_time_total / test_cases
        avg_binary = binary_time_total / test_cases

        linear_times.append(avg_linear)
        binary_times.append(avg_binary)

        print(f"Размер: {size:6d} | Линейный: {avg_linear:.6f}с | Бинарный: {avg_binary:.6f}с")

    # Построение графиков
    plt.figure(figsize=(12, 5))

    # График в линейном масштабе
    plt.subplot(1, 2, 1)
    plt.plot(sizes, linear_times, 'o-', label='Линейный поиск O(n)')
    plt.plot(sizes, binary_times, 's-', label='Бинарный поиск O(log n)')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение производительности')
    plt.legend()
    plt.grid(True)

    # График в логарифмическом масштабе
    plt.subplot(1, 2, 2)
    plt.semilogy(sizes, linear_times, 'o-', label='Линейный поиск O(n)')
    plt.semilogy(sizes, binary_times, 's-', label='Бинарный поиск O(log n)')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды) - log scale')
    plt.title('Логарифмическая шкала')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('comparison_plot.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()