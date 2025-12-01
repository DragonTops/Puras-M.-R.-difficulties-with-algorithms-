"""
Модуль с решением практических задач с использованием рекурсии.
"""

from typing import List, Optional


def hanoi_towers(n: int, source: str = "A", destination: str = "C", auxiliary: str = "B") -> List[tuple]:
    """
    Решение задачи о Ханойских башнях.
    
    Args:
        n: Количество дисков
        source: Исходный стержень
        destination: Целевой стержень
        auxiliary: Вспомогательный стержень
        
    Returns:
        Список ходов в формате (диск, откуда, куда)
        
    Сложность: O(2^n)
    """
    moves = []
    
    def hanoi_recursive(n_disks: int, src: str, dest: str, aux: str) -> None:
        if n_disks == 1:
            moves.append((1, src, dest))
        else:
            hanoi_recursive(n_disks - 1, src, aux, dest)
            moves.append((n_disks, src, dest))
            hanoi_recursive(n_disks - 1, aux, dest, src)
    
    if n > 0:
        hanoi_recursive(n, source, destination, auxiliary)
    
    return moves


def is_palindrome_recursive(s: str, left: int = 0, right: Optional[int] = None) -> bool:
    """
    Проверка, является ли строка палиндромом (рекурсивно).
    
    Args:
        s: Строка для проверки
        left: Левая граница
        right: Правая граница
        
    Returns:
        True, если строка является палиндромом
        
    Сложность: O(n)
    """
    if right is None:
        right = len(s) - 1
    
    if left >= right:
        return True
    
    if s[left].lower() != s[right].lower():
        return False
    
    return is_palindrome_recursive(s, left + 1, right - 1)


def is_palindrome_iterative(s: str) -> bool:
    """
    Проверка, является ли строка палиндромом (итеративно).
    
    Args:
        s: Строка для проверки
        
    Returns:
        True, если строка является палиндромом
        
    Сложность: O(n)
    """
    s = s.lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


class TreeNode:
    """Узел бинарного дерева."""
    
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def tree_traversal_preorder(root: Optional[TreeNode]) -> List[int]:
    """
    Прямой обход дерева (preorder): корень -> левое поддерево -> правое поддерево.
    
    Args:
        root: Корень дерева
        
    Returns:
        Список значений узлов в порядке обхода
        
    Сложность: O(n)
    """
    result = []
    
    def traverse(node: Optional[TreeNode]) -> None:
        if node is not None:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    
    traverse(root)
    return result


def tree_traversal_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Симметричный обход дерева (inorder): левое поддерево -> корень -> правое поддерево.
    
    Args:
        root: Корень дерева
        
    Returns:
        Список значений узлов в порядке обхода
        
    Сложность: O(n)
    """
    result = []
    
    def traverse(node: Optional[TreeNode]) -> None:
        if node is not None:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    
    traverse(root)
    return result


def tree_traversal_postorder(root: Optional[TreeNode]) -> List[int]:
    """
    Обратный обход дерева (postorder): левое поддерево -> правое поддерево -> корень.
    
    Args:
        root: Корень дерева
        
    Returns:
        Список значений узлов в порядке обхода
        
    Сложность: O(n)
    """
    result = []
    
    def traverse(node: Optional[TreeNode]) -> None:
        if node is not None:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    
    traverse(root)
    return result


def tree_height(root: Optional[TreeNode]) -> int:
    """
    Вычисление высоты бинарного дерева.
    
    Args:
        root: Корень дерева
        
    Returns:
        Высота дерева (0 для пустого дерева)
        
    Сложность: O(n)
    """
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)


def count_nodes(root: Optional[TreeNode]) -> int:
    """
    Подсчет количества узлов в бинарном дереве.
    
    Args:
        root: Корень дерева
        
    Returns:
        Количество узлов
        
    Сложность: O(n)
    """
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def sum_tree_values(root: Optional[TreeNode]) -> int:
    """
    Вычисление суммы всех значений в бинарном дереве.
    
    Args:
        root: Корень дерева
        
    Returns:
        Сумма всех значений
        
    Сложность: O(n)
    """
    if root is None:
        return 0
    
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)

