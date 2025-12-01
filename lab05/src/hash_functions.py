"""
Модуль с реализацией различных хеш-функций для строковых ключей.
"""

def simple_hash(key: str, table_size: int) -> int:
    """
    Простая хеш-функция - сумма кодов символов.
    Сложность: O(n), где n - длина ключа.
    """
    return sum(ord(char) for char in key) % table_size

def polynomial_hash(key: str, table_size: int, base: int = 31) -> int:
    """
    Полиномиальная хеш-функция.
    Сложность: O(n), где n - длина ключа.
    """
    hash_value = 0
    for char in key:
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value

def djb2_hash(key: str, table_size: int) -> int:
    """
    Хеш-функция DJB2.
    Сложность: O(n), где n - длина ключа.
    """
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % table_size