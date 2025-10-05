"""
Тесты для алгоритмов поиска
"""
import pytest
from src.search_algorithms import linear_search, binary_search


class TestSearchAlgorithms:
    """Тестовый класс для алгоритмов поиска"""

    def test_linear_search_found(self):
        """Тест линейного поиска - элемент найден"""
        arr = [1, 3, 5, 7, 9]
        assert linear_search(arr, 5) == 2
        assert linear_search(arr, 1) == 0
        assert linear_search(arr, 9) == 4

    def test_linear_search_not_found(self):
        """Тест линейного поиска - элемент не найден"""
        arr = [1, 3, 5, 7, 9]
        assert linear_search(arr, 2) == -1
        assert linear_search(arr, 10) == -1

    def test_binary_search_found(self):
        """Тест бинарного поиска - элемент найден"""
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(arr, 5) == 2
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 13) == 6
        assert binary_search(arr, 7) == 3

    def test_binary_search_not_found(self):
        """Тест бинарного поиска - элемент не найден"""
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(arr, 2) == -1
        assert binary_search(arr, 15) == -1

    def test_empty_array(self):
        """Тест поиска в пустом массиве"""
        arr = []
        assert linear_search(arr, 1) == -1
        assert binary_search(arr, 1) == -1