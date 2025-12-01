from typing import Optional, List
from binary_search_tree import TreeNode

def recursive_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Рекурсивный in-order обход.
    Сложность: O(n)
    """
    result = []
    def traverse(node: Optional[TreeNode]):
        if node:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    traverse(root)
    return result

def recursive_preorder(root: Optional[TreeNode]) -> List[int]:
    """
    Рекурсивный pre-order обход.
    Сложность: O(n)
    """
    result = []
    def traverse(node: Optional[TreeNode]):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result

def recursive_postorder(root: Optional[TreeNode]) -> List[int]:
    """
    Рекурсивный post-order обход.
    Сложность: O(n)
    """
    result = []
    def traverse(node: Optional[TreeNode]):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
    traverse(root)
    return result

def iterative_inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный in-order обход с использованием стека.
    Сложность: O(n)
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result

def iterative_preorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный pre-order обход.
    Сложность: O(n)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        result.append(current.value)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result

def iterative_postorder(root: Optional[TreeNode]) -> List[int]:
    """
    Итеративный post-order обход.
    Сложность: O(n)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    visited = set()
    
    while stack:
        current = stack[-1]
        
        if current.left and current.left not in visited:
            stack.append(current.left)
        elif current.right and current.right not in visited:
            stack.append(current.right)
        else:
            result.append(current.value)
            visited.add(current)
            stack.pop()
    
    return result