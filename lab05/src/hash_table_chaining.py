"""
Реализация хеш-таблицы с методом цепочек для разрешения коллизий.
"""

from typing import Any, List, Tuple, Optional
from hash_functions import djb2_hash

class HashTableChaining:
    """
    Хеш-таблица с методом цепочек.
    """
    
    def __init__(self, initial_size: int = 16, load_factor: float = 0.75):
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0
        self.table: List[List[Tuple[str, Any]]] = [[] for _ in range(self.size)]
        self.hash_function = djb2_hash

    def _resize(self) -> None:
        """Увеличение размера таблицы при достижении коэффициента заполнения."""
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        
        for bucket in self.table:
            for key, value in bucket:
                index = self.hash_function(key, new_size)
                new_table[index].append((key, value))
        
        self.table = new_table
        self.size = new_size

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка элемента в хеш-таблицу.
        Сложность: O(1) в среднем случае, O(n) в худшем случае.
        """
        if self.count / self.size > self.load_factor:
            self._resize()
            
        index = self.hash_function(key, self.size)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1

    def search(self, key: str) -> Optional[Any]:
        """
        Поиск элемента в хеш-таблице.
        Сложность: O(1) в среднем случае, O(n) в худшем случае.
        """
        index = self.hash_function(key, self.size)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        """
        Удаление элемента из хеш-таблицы.
        Сложность: O(1) в среднем случае, O(n) в худшем случае.
        """
        index = self.hash_function(key, self.size)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False