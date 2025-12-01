"""
Тесты для хеш-функций.
"""

import pytest
from src.hash_functions import simple_hash, polynomial_hash, djb2_hash

def test_simple_hash():
    """Тест простой хеш-функции."""
    assert simple_hash("test", 100) == simple_hash("test", 100)
    assert simple_hash("test", 100) != simple_hash("test2", 100)

def test_polynomial_hash():
    """Тест полиномиальной хеш-функции."""
    assert polynomial_hash("test", 100) == polynomial_hash("test", 100)
    assert polynomial_hash("test", 100) != polynomial_hash("test2", 100)

def test_djb2_hash():
    """Тест хеш-функции DJB2."""
    assert djb2_hash("test", 100) == djb2_hash("test", 100)
    assert djb2_hash("test", 100) != djb2_hash("test2", 100)