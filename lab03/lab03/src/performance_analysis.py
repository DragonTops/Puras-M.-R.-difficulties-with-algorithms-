"""
Модуль для анализа производительности рекурсивных и итеративных алгоритмов.
"""

import time
from typing import Callable, Tuple
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.recursive_algorithms import (
    factorial_recursive,
    factorial_iterative,
    fibonacci_recursive,
    fibonacci_iterative,
    binary_search_recursive,
    binary_search_iterative,
    gcd_recursive,
    gcd_iterative
)
from src.task_solutions import (
    is_palindrome_recursive,
    is_palindrome_iterative
)


def measure_time(func: Callable, *args, **kwargs) -> Tuple[float, any]:
    """
    Измерение времени выполнения функции.
    
    Args:
        func: Функция для измерения
        *args: Позиционные аргументы
        **kwargs: Именованные аргументы
        
    Returns:
        Кортеж (время выполнения в секундах, результат функции)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time, result


def compare_factorial(n: int) -> None:
    """Сравнение рекурсивной и итеративной версий факториала."""
    print(f"\nСравнение факториала для n = {n}:")
    
    try:
        time_rec, result_rec = measure_time(factorial_recursive, n)
        print(f"Рекурсивная версия: {time_rec:.6f} секунд, результат: {result_rec}")
    except RecursionError:
        print(f"Рекурсивная версия: Превышена глубина рекурсии для n = {n}")
        time_rec = float('inf')
        result_rec = None
    
    time_iter, result_iter = measure_time(factorial_iterative, n)
    print(f"Итеративная версия: {time_iter:.6f} секунд, результат: {result_iter}")
    
    if result_rec == result_iter:
        print("Результаты совпадают")
    else:
        print("ОШИБКА: Результаты не совпадают!")


def compare_fibonacci(n: int) -> None:
    """Сравнение рекурсивной и итеративной версий чисел Фибоначчи."""
    print(f"\nСравнение чисел Фибоначчи для n = {n}:")
    
    if n > 35:
        print(f"Рекурсивная версия: Пропущена (слишком медленная для n = {n})")
        time_rec = float('inf')
        result_rec = None
    else:
        time_rec, result_rec = measure_time(fibonacci_recursive, n)
        print(f"Рекурсивная версия: {time_rec:.6f} секунд, результат: {result_rec}")
    
    time_iter, result_iter = measure_time(fibonacci_iterative, n)
    print(f"Итеративная версия: {time_iter:.6f} секунд, результат: {result_iter}")
    
    if n <= 35 and result_rec == result_iter:
        print("Результаты совпадают")
    elif n > 35:
        print("Итеративная версия работает для больших значений n")


def compare_binary_search(arr_size: int, target: int) -> None:
    """Сравнение рекурсивной и итеративной версий бинарного поиска."""
    print(f"\nСравнение бинарного поиска (размер массива: {arr_size}, искомое: {target}):")
    
    arr = list(range(arr_size))
    
    time_rec, result_rec = measure_time(binary_search_recursive, arr, target)
    print(f"Рекурсивная версия: {time_rec:.6f} секунд, индекс: {result_rec}")
    
    time_iter, result_iter = measure_time(binary_search_iterative, arr, target)
    print(f"Итеративная версия: {time_iter:.6f} секунд, индекс: {result_iter}")
    
    if result_rec == result_iter:
        print("Результаты совпадают")
    else:
        print("ОШИБКА: Результаты не совпадают!")


def compare_gcd(a: int, b: int) -> None:
    """Сравнение рекурсивной и итеративной версий НОД."""
    print(f"\nСравнение НОД для a = {a}, b = {b}:")
    
    time_rec, result_rec = measure_time(gcd_recursive, a, b)
    print(f"Рекурсивная версия: {time_rec:.6f} секунд, НОД: {result_rec}")
    
    time_iter, result_iter = measure_time(gcd_iterative, a, b)
    print(f"Итеративная версия: {time_iter:.6f} секунд, НОД: {result_iter}")
    
    if result_rec == result_iter:
        print("Результаты совпадают")
    else:
        print("ОШИБКА: Результаты не совпадают!")


def compare_palindrome(s: str) -> None:
    """Сравнение рекурсивной и итеративной версий проверки палиндрома."""
    print(f"\nСравнение проверки палиндрома для строки '{s}':")
    
    time_rec, result_rec = measure_time(is_palindrome_recursive, s)
    print(f"Рекурсивная версия: {time_rec:.6f} секунд, результат: {result_rec}")
    
    time_iter, result_iter = measure_time(is_palindrome_iterative, s)
    print(f"Итеративная версия: {time_iter:.6f} секунд, результат: {result_iter}")
    
    if result_rec == result_iter:
        print("Результаты совпадают")
    else:
        print("ОШИБКА: Результаты не совпадают!")


def analyze_fibonacci_performance() -> None:
    """Анализ производительности чисел Фибоначчи для разных значений n."""
    print("\n" + "="*60)
    print("Анализ производительности чисел Фибоначчи")
    print("="*60)
    
    values = [10, 20, 30, 35, 40]
    
    print("\nИтеративная версия:")
    for n in values:
        time_iter, result = measure_time(fibonacci_iterative, n)
        print(f"  n = {n:2d}: {time_iter:.6f} секунд, результат: {result}")
    
    print("\nРекурсивная версия (только для малых значений):")
    for n in [10, 20, 30, 35]:
        time_rec, result = measure_time(fibonacci_recursive, n)
        print(f"  n = {n:2d}: {time_rec:.6f} секунд, результат: {result}")


def main() -> None:
    """Основная функция для запуска анализа производительности."""
    print("="*60)
    print("Анализ производительности рекурсивных и итеративных алгоритмов")
    print("="*60)
    
    # Сравнение факториала
    compare_factorial(10)
    compare_factorial(100)
    compare_factorial(500)
    
    # Сравнение чисел Фибоначчи
    compare_fibonacci(10)
    compare_fibonacci(30)
    compare_fibonacci(40)
    
    # Анализ производительности Фибоначчи
    analyze_fibonacci_performance()
    
    # Сравнение бинарного поиска
    compare_binary_search(1000, 500)
    compare_binary_search(10000, 5000)
    
    # Сравнение НОД
    compare_gcd(48, 18)
    compare_gcd(1000, 250)
    
    # Сравнение палиндромов
    compare_palindrome("радар")
    compare_palindrome("привет")
    compare_palindrome("А роза упала на лапу Азора")
    
    print("\n" + "="*60)
    print("Анализ завершен")
    print("="*60)


if __name__ == "__main__":
    main()

