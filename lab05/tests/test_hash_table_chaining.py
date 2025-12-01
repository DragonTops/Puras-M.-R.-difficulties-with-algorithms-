"""
Тесты для хеш-таблицы с методом цепочек.
"""

import pytest
from src.hash_table_chaining import HashTableChaining

def test_insert_and_search():
    """Тест вставки и поиска."""
    ht = HashTableChaining()
    ht.insert("key1", "value1")
    assert ht.search("key1") == "value1"

def test_delete():
    """Тест удаления."""
    ht = HashTableChaining()
    ht.insert("key1", "value1")
    assert ht.delete("key1") == True
    assert ht.search("key1") is None

def test_collision_handling():
    """Тест обработки коллизий."""
    ht = HashTableChaining(size=1)  # Принудительно создаем коллизии
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    assert ht.search("key1") == "value1"
    assert ht.search("key2") == "value2"