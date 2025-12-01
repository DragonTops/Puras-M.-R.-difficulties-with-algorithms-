def z_function(s: str) -> list[int]:
    """
    Вычисление Z-функции для строки s.
    
    Args:
        s: Входная строка
        
    Returns:
        Список значений Z-функции
        
    Сложность: O(n) по времени, O(n) по памяти
    """
    n = len(s)
    z = [0] * n
    
    # Границы самого правого сегмента [l, r]
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
            
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
            
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z


def z_search(text: str, pattern: str) -> list[int]:
    """
    Поиск всех вхождений pattern в text с использованием Z-функции.
    
    Args:
        text: Текст для поиска
        pattern: Искомый паттерн
        
    Returns:
        Список индексов начала вхождений pattern в text
    """
    if not pattern:
        return []
    
    # Создаем строку pattern + '$' + text
    combined = pattern + '$' + text
    z = z_function(combined)
    
    result = []
    m = len(pattern)
    
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            result.append(i - m - 1)
    
    return result


if __name__ == "__main__":
    # Пример использования
    test_strings = ["abacaba", "aaa", "abcabc"]
    
    for s in test_strings:
        result = z_function(s)
        print(f"Строка: '{s}'")
        print(f"Z-функция: {result}")
        print()
    
    # Пример поиска
    text, pattern = "abacabaab", "aba"
    result = z_search(text, pattern)
    print(f"Поиск '{pattern}' в '{text}': {result}")