"""
Модуль с реализацией рекурсивных алгоритмов.
Содержит рекурсивные и итеративные версии базовых алгоритмов.
"""

from typing import Any, List, Optional


def factorial_recursive(n: int) -> int:
    """
    Вычисление факториала рекурсивным способом.
    
    Args:
        n: Неотрицательное целое число
        
    Returns:
        Факториал числа n
        
    Сложность: O(n)
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Вычисление факториала итеративным способом.
    
    Args:
        n: Неотрицательное целое число
        
    Returns:
        Факториал числа n
        
    Сложность: O(n)
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_recursive(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи рекурсивным способом.
    
    Args:
        n: Номер числа Фибоначчи (n >= 0)
        
    Returns:
        n-е число Фибоначчи
        
    Сложность: O(2^n) - экспоненциальная
    """
    if n < 0:
        raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Вычисление n-го числа Фибоначчи итеративным способом.
    
    Args:
        n: Номер числа Фибоначчи (n >= 0)
        
    Returns:
        n-е число Фибоначчи
        
    Сложность: O(n)
    """
    if n < 0:
        raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> Optional[int]:
    """
    Бинарный поиск рекурсивным способом.
    
    Args:
        arr: Отсортированный список целых чисел
        target: Искомое значение
        left: Левая граница поиска
        right: Правая граница поиска
        
    Returns:
        Индекс элемента или None, если элемент не найден
        
    Сложность: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    """
    Бинарный поиск итеративным способом.
    
    Args:
        arr: Отсортированный список целых чисел
        target: Искомое значение
        
    Returns:
        Индекс элемента или None, если элемент не найден
        
    Сложность: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return None


def power_recursive(base: float, exponent: int) -> float:
    """
    Возведение в степень рекурсивным способом.
    
    Args:
        base: Основание
        exponent: Показатель степени (целое число)
        
    Returns:
        base^exponent
        
    Сложность: O(log n) при использовании оптимизации
    """
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power_recursive(base, -exponent)
    
    if exponent % 2 == 0:
        half_power = power_recursive(base, exponent // 2)
        return half_power * half_power
    else:
        return base * power_recursive(base, exponent - 1)


def gcd_recursive(a: int, b: int) -> int:
    """
    Нахождение наибольшего общего делителя (НОД) рекурсивным способом (алгоритм Евклида).
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        НОД(a, b)
        
    Сложность: O(log min(a, b))
    """
    if b == 0:
        return abs(a)
    return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """
    Нахождение наибольшего общего делителя (НОД) итеративным способом.
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        НОД(a, b)
        
    Сложность: O(log min(a, b))
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

