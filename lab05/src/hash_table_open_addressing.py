"""
Реализация хеш-таблицы с открытой адресацией.
"""

from typing import Any, Optional, Tuple
from hash_functions import djb2_hash, polynomial_hash

class HashTableOpenAddressing:
    """
    Хеш-таблица с открытой адресацией.
    """
    
    def __init__(self, initial_size: int = 16, load_factor: float = 0.75, 
                 probing_method: str = 'linear'):
        self.size = initial_size
        self.load_factor = load_factor
        self.count = 0
        self.table: List[Optional[Tuple[str, Any]]] = [None] * self.size
        self.primary_hash = djb2_hash
        self.secondary_hash = polynomial_hash
        self.probing_method = probing_method

    def _probe_sequence(self, key: str, i: int) -> int:
        """Генерация последовательности проб."""
        if self.probing_method == 'linear':
            return (self.primary_hash(key, self.size) + i) % self.size
        elif self.probing_method == 'double':
            h1 = self.primary_hash(key, self.size)
            h2 = self.secondary_hash(key, self.size)
            return (h1 + i * h2) % self.size
        else:
            raise ValueError("Unknown probing method")

    def _resize(self) -> None:
        """Увеличение размера таблицы."""
        new_size = self.size * 2
        old_table = self.table
        self.table = [None] * new_size
        self.size = new_size
        self.count = 0
        
        for item in old_table:
            if item is not None:
                key, value = item
                self.insert(key, value)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка элемента в хеш-таблицу.
        Сложность: O(1/(1-α)) в среднем случае.
        """
        if self.count / self.size > self.load_factor:
            self._resize()
            
        i = 0
        while i < self.size:
            index = self._probe_sequence(key, i)
            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                if self.table[index] is None:
                    self.count += 1
                return
            i += 1
            
        self._resize()
        self.insert(key, value)

    def search(self, key: str) -> Optional[Any]:
        """
        Поиск элемента в хеш-таблице.
        Сложность: O(1/(1-α)) в среднем случае.
        """
        i = 0
        while i < self.size:
            index = self._probe_sequence(key, i)
            if self.table[index] is None:
                return None
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
        return None

    def delete(self, key: str) -> bool:
        """
        Удаление элемента из хеш-таблицы.
        Сложность: O(1/(1-α)) в среднем случае.
        """
        i = 0
        while i < self.size:
            index = self._probe_sequence(key, i)
            if self.table[index] is None:
                return False
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return True
            i += 1
        return False