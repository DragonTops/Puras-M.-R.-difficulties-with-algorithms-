"""Модуль для анализа производительности различных структур данных."""

import timeit
from collections import deque
from linked_list import LinkedList


def compare_list_and_linked_list() -> None:
    """Сравнение list и LinkedList для вставки в начало."""
    print("Сравнение вставки в начало (1000 элементов):")

    # Для list
    def list_insert_start():
        lst = []
        for i in range(1000):
            lst.insert(0, i)
        return lst

    # Для LinkedList
    def linked_list_insert_start():
        ll = LinkedList()
        for i in range(1000):
            ll.insert_at_start(i)
        return ll

    time_list = timeit.timeit(list_insert_start, number=100)
    time_linked_list = timeit.timeit(linked_list_insert_start, number=100)

    print(f"List: {time_list:.5f} секунд")
    print(f"LinkedList: {time_linked_list:.5f} секунд")


def compare_list_and_deque() -> None:
    """Сравнение list и deque для операций очереди."""
    print("\nСравнение операций очереди (1000 операций dequeue):")

    # Для list
    def list_queue():
        lst = list(range(1000))
        for _ in range(1000):
            lst.pop(0)
        return lst

    # Для deque
    def deque_queue():
        dq = deque(range(1000))
        for _ in range(1000):
            dq.popleft()
        return dq

    time_list = timeit.timeit(list_queue, number=100)
    time_deque = timeit.timeit(deque_queue, number=100)

    print(f"List (pop(0)): {time_list:.5f} секунд")
    print(f"Deque (popleft()): {time_deque:.5f} секунд")


if __name__ == '__main__':
    compare_list_and_linked_list()
    compare_list_and_deque()