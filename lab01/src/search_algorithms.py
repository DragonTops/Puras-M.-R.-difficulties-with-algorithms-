"""
Модуль с реализацией алгоритмов поиска
"""


def linear_search(arr: list, target: int) -> int:
    """
    Линейный поиск элемента в массиве

    Args:
        arr: Массив для поиска
        target: Искомый элемент

    Returns:
        int: Индекс элемента или -1 если не найден
    """
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)


# Общая сложность: O(n)

def binary_search(arr: list, target: int) -> int:
    """
    Бинарный поиск элемента в отсортированном массиве

    Args:
        arr: Отсортированный массив
        target: Искомый элемент

    Returns:
        int: Индекс элемента или -1 если не найден
    """
    left = 0  # O(1)
    right = len(arr) - 1  # O(1)

    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:  # O(1)
            right = mid - 1  # O(1)
    return -1  # O(1)
# Общая сложность: O(log n)