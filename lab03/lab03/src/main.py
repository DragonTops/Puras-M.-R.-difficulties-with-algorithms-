"""
Основной модуль для демонстрации работы рекурсивных алгоритмов.
"""

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
    hanoi_towers,
    is_palindrome_recursive,
    is_palindrome_iterative,
    TreeNode,
    tree_traversal_preorder,
    tree_traversal_inorder,
    tree_traversal_postorder,
    tree_height,
    count_nodes,
    sum_tree_values
)


def demonstrate_factorial() -> None:
    """Демонстрация вычисления факториала."""
    print("="*60)
    print("Демонстрация вычисления факториала")
    print("="*60)
    
    values = [5, 10, 15]
    for n in values:
        fact_rec = factorial_recursive(n)
        fact_iter = factorial_iterative(n)
        print(f"Факториал {n}:")
        print(f"  Рекурсивно: {fact_rec}")
        print(f"  Итеративно: {fact_iter}")
        print()


def demonstrate_fibonacci() -> None:
    """Демонстрация вычисления чисел Фибоначчи."""
    print("="*60)
    print("Демонстрация вычисления чисел Фибоначчи")
    print("="*60)
    
    values = [5, 10, 20, 30]
    for n in values:
        if n <= 30:
            fib_rec = fibonacci_recursive(n)
        else:
            fib_rec = "слишком медленно"
        fib_iter = fibonacci_iterative(n)
        print(f"Число Фибоначчи F({n}):")
        if n <= 30:
            print(f"  Рекурсивно: {fib_rec}")
        else:
            print(f"  Рекурсивно: {fib_rec}")
        print(f"  Итеративно: {fib_iter}")
        print()


def demonstrate_binary_search() -> None:
    """Демонстрация бинарного поиска."""
    print("="*60)
    print("Демонстрация бинарного поиска")
    print("="*60)
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    targets = [7, 1, 19, 10]
    
    print(f"Массив: {arr}")
    for target in targets:
        idx_rec = binary_search_recursive(arr, target)
        idx_iter = binary_search_iterative(arr, target)
        print(f"Поиск {target}:")
        print(f"  Рекурсивно: индекс {idx_rec}")
        print(f"  Итеративно: индекс {idx_iter}")
        print()


def demonstrate_gcd() -> None:
    """Демонстрация вычисления НОД."""
    print("="*60)
    print("Демонстрация вычисления НОД")
    print("="*60)
    
    pairs = [(48, 18), (100, 25), (17, 13), (1000, 250)]
    for a, b in pairs:
        gcd_rec = gcd_recursive(a, b)
        gcd_iter = gcd_iterative(a, b)
        print(f"НОД({a}, {b}):")
        print(f"  Рекурсивно: {gcd_rec}")
        print(f"  Итеративно: {gcd_iter}")
        print()


def demonstrate_hanoi_towers() -> None:
    """Демонстрация решения задачи о Ханойских башнях."""
    print("="*60)
    print("Демонстрация задачи о Ханойских башнях")
    print("="*60)
    
    for n in [1, 2, 3]:
        moves = hanoi_towers(n)
        print(f"\nХанойские башни для {n} дисков:")
        print(f"Количество ходов: {len(moves)}")
        print("Ходы:")
        for move in moves:
            disk, source, dest = move
            print(f"  Диск {disk}: {source} -> {dest}")


def demonstrate_palindrome() -> None:
    """Демонстрация проверки палиндромов."""
    print("="*60)
    print("Демонстрация проверки палиндромов")
    print("="*60)
    
    test_strings = ["радар", "привет", "А роза упала на лапу Азора", "level", "hello"]
    
    for s in test_strings:
        is_pal_rec = is_palindrome_recursive(s)
        is_pal_iter = is_palindrome_iterative(s)
        print(f"Строка '{s}':")
        print(f"  Рекурсивно: {'палиндром' if is_pal_rec else 'не палиндром'}")
        print(f"  Итеративно: {'палиндром' if is_pal_iter else 'не палиндром'}")
        print()


def demonstrate_tree_traversal() -> None:
    """Демонстрация обхода бинарного дерева."""
    print("="*60)
    print("Демонстрация обхода бинарного дерева")
    print("="*60)
    
    # Создание тестового дерева
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Структура дерева:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\")
    print("   4   5")
    print()
    
    preorder = tree_traversal_preorder(root)
    inorder = tree_traversal_inorder(root)
    postorder = tree_traversal_postorder(root)
    height = tree_height(root)
    nodes_count = count_nodes(root)
    sum_values = sum_tree_values(root)
    
    print(f"Прямой обход (preorder): {preorder}")
    print(f"Симметричный обход (inorder): {inorder}")
    print(f"Обратный обход (postorder): {postorder}")
    print(f"Высота дерева: {height}")
    print(f"Количество узлов: {nodes_count}")
    print(f"Сумма значений: {sum_values}")


def main() -> None:
    """Основная функция для демонстрации всех алгоритмов."""
    demonstrate_factorial()
    print()
    
    demonstrate_fibonacci()
    print()
    
    demonstrate_binary_search()
    print()
    
    demonstrate_gcd()
    print()
    
    demonstrate_hanoi_towers()
    print()
    
    demonstrate_palindrome()
    print()
    
    demonstrate_tree_traversal()
    print()
    
    print("="*60)
    print("Все демонстрации завершены")
    print("="*60)


if __name__ == "__main__":
    main()

