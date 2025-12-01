def prefix_function(s: str) -> list[int]:
    """
    Вычисление префикс-функции для строки s.
    
    Args:
        s: Входная строка
        
    Returns:
        Список значений префикс-функции
        
    Сложность: O(n) по времени, O(n) по памяти
    """
    n = len(s)
    pi = [0] * n
    
    for i in range(1, n):
        j = pi[i - 1]
        
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
            
        if s[i] == s[j]:
            j += 1
            
        pi[i] = j
    
    return pi


if __name__ == "__main__":
    # Пример использования
    test_strings = ["ababaca", "abcabcd", "aabaaab"]
    
    for s in test_strings:
        result = prefix_function(s)
        print(f"Строка: '{s}'")
        print(f"Префикс-функция: {result}")
        print()