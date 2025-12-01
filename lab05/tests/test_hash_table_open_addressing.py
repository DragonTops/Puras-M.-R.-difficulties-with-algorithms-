"""
Тесты для хеш-таблицы с открытой адресацией.
"""

import pytest
from src.hash_table_open_addressing import HashTableOpenAddressing

def test_linear_probing():
    """Тест линейного пробирования."""
    ht = HashTableOpenAddressing(probing_method='linear')
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    assert ht.search("key1") == "value1"
    assert ht.search("key2") == "value2"

def test_double_hashing():
    """Тест двойного хеширования."""
    ht = HashTableOpenAddressing(probing_method='double')
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    assert ht.search("key1") == "value1"
    assert ht.search("key2") == "value2"

def test_delete_open_addressing():
    """Тест удаления в открытой адресации."""
    ht = HashTableOpenAddressing()
    ht.insert("key1", "value1")
    assert ht.delete("key1") == True
    assert ht.search("key1") is None