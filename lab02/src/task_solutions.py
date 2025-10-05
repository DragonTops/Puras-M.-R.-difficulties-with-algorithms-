"""Модуль для решения практических задач."""

from collections import deque
from typing import List


def check_brackets(expression: str) -> bool:
    """Проверка сбалансированности скобок. Используется стек (list)."""
    stack: List[str] = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack


def is_palindrome(sequence: str) -> bool:
    """Проверка, является ли последовательность палиндромом. Используется дек (deque)."""
    dq = deque(sequence)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def simulate_print_queue(tasks: List[str]) -> None:
    """Симуляция обработки задач в очереди печати. Используется deque."""
    queue = deque(tasks)
    while queue:
        current_task = queue.popleft()
        print(f"Печатается: {current_task}")
        # Имитация времени печати
        # time.sleep(0.5)
    print("Все задачи выполнены.")


if __name__ == '__main__':
    # Задача 1: Проверка скобок
    expr1 = "((( )))"
    expr2 = "((( ))]"
    print(f"Выражение '{expr1}' сбалансировано: {check_brackets(expr1)}")
    print(f"Выражение '{expr2}' сбалансировано: {check_brackets(expr2)}")

    # Задача 2: Палиндром
    word1 = "радар"
    word2 = "привет"
    print(f"Слово '{word1}' является палиндромом: {is_palindrome(word1)}")
    print(f"Слово '{word2}' является палиндромом: {is_palindrome(word2)}")

    # Задача 3: Очередь печати
    tasks_list = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
    simulate_print_queue(tasks_list)