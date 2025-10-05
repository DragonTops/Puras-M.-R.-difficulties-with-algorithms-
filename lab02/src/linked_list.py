"""Модуль реализует связный список (LinkedList)."""

from typing import Optional, Any


class Node:
    """Узел связного списка."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:
    """Связный список."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insert_at_start(self, data: Any) -> None:
        """Вставка элемента в начало списка. Сложность O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data: Any) -> None:
        """Вставка элемента в конец списка. Сложность O(1) с хвостом."""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self) -> Optional[Any]:
        """Удаление элемента из начала списка. Сложность O(1)."""
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def traversal(self) -> None:
        """Печать всех элементов списка. Сложность O(n)."""
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()