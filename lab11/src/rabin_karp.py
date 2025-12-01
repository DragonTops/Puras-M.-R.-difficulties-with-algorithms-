def rabin_karp_search(text: str, pattern: str, base: int = 256, prime: int = 101) -> list[int]:
    """
    Поиск всех вхождений pattern в text с помощью алгоритма Рабина-Карпа.
    
    Args:
        text: Текст для поиска
        pattern: Искомый паттерн
        base: Основание системы счисления для хеширования
        prime: Простое число для модуля
        
    Returns:
        Список индексов начала вхождений pattern в text
        
    Сложность: O(n+m) в среднем, O(nm) в худшем случае по времени, O(1) по памяти
    """
    n, m = len(text), len(pattern)
    if n < m:
        return []
    
    result = []
    pattern_hash = 0
    text_hash = 0
    h = 1  # base^(m-1) % prime
    
    # Вычисление h = base^(m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime
    
    # Вычисление хеша pattern и первого окна text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Скольжение по тексту
    for i in range(n - m + 1):
        # Проверка хешей и при совпадении - проверка символов
        if pattern_hash == text_hash:
            # Проверка на коллизию - сравниваем символы
            if text[i:i + m] == pattern:
                result.append(i)
        
        # Вычисление хеша для следующего окна
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # Обеспечиваем неотрицательность
            if text_hash < 0:
                text_hash += prime
    
    return result


if __name__ == "__main__":
    # Пример использования
    test_cases = [
        ("ababcababacab", "ababa"),
        ("hello world", "world"),
        ("aaaaa", "aa"),
        ("abc", "d")
    ]
    
    for text, pattern in test_cases:
        result = rabin_karp_search(text, pattern)
        print(f"Текст: '{text}', паттерн: '{pattern}'")
        print(f"Результат: {result}")
        print()