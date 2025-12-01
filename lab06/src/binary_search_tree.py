from typing import Optional, List

class TreeNode:
    """Узел бинарного дерева поиска"""
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinarySearchTree:
    """Реализация бинарного дерева поиска"""
    
    def insert_iterative(self, root: Optional[TreeNode], value: int) -> TreeNode:
        """
        Итеративная вставка элемента в BST.
        Сложность: O(h) в худшем случае, O(log n) в среднем для сбалансированного дерева
        """
        new_node = TreeNode(value)
        if root is None:
            return new_node
            
        current = root
        parent = None
        
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
                
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
            
        return root

    def search_iterative(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        """
        Итеративный поиск элемента в BST.
        Сложность: O(h) в худшем случае, O(log n) в среднем для сбалансированного дерева
        """
        current = root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def find_min_iterative(self, root: TreeNode) -> TreeNode:
        """
        Поиск минимального элемента в поддереве (итеративный).
        Сложность: O(h) в худшем случае
        """
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max_iterative(self, root: TreeNode) -> TreeNode:
        """
        Поиск максимального элемента в поддереве (итеративный).
        Сложность: O(h) в худшем случае
        """
        current = root
        while current.right is not None:
            current = current.right
        return current

    def height_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Вычисление высоты дерева/поддерева (итеративное).
        Сложность: O(n)
        """
        if root is None:
            return 0
            
        stack = [(root, 1)]
        max_height = 0
        
        while stack:
            node, height = stack.pop()
            if height > max_height:
                max_height = height
                
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
                
        return max_height

    def is_valid_bst_iterative(self, root: Optional[TreeNode]) -> bool:
        """
        Проверка корректности BST (итеративная).
        Сложность: O(n)
        """
        if root is None:
            return True
            
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, min_val, max_val = stack.pop()
            
            if not (min_val < node.value < max_val):
                return False
                
            if node.left:
                stack.append((node.left, min_val, node.value))
            if node.right:
                stack.append((node.right, node.value, max_val))
                
        return True

    def print_tree(self, root: Optional[TreeNode], level: int = 0, prefix: str = "Root: ") -> List[str]:
        """
        Текстовая визуализация дерева.
        Сложность: O(n)
        """
        lines = []
        if root is not None:
            lines.append(" " * (level * 4) + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                if root.left:
                    lines.extend(self.print_tree(root.left, level + 1, "L--- "))
                else:
                    lines.append(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    lines.extend(self.print_tree(root.right, level + 1, "R--- "))
                else:
                    lines.append(" " * ((level + 1) * 4) + "R--- None")
        return lines