from prefix_function import prefix_function


def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Поиск всех вхождений pattern в text с помощью алгоритма Кнута-Морриса-Пратта.
    
    Args:
        text: Текст для поиска
        pattern: Искомый паттерн
        
    Returns:
        Список индексов начала вхождений pattern в text
        
    Сложность: O(n+m) по времени, O(m) по памяти
    """
    if not pattern:
        return []
    
    n, m = len(text), len(pattern)
    pi = prefix_function(pattern)
    result = []
    j = 0  # Длина текущего совпавшего префикса pattern
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
            
        if text[i] == pattern[j]:
            j += 1
            
        if j == m:
            result.append(i - m + 1)
            j = pi[j - 1]
    
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
        result = kmp_search(text, pattern)
        print(f"Текст: '{text}', паттерн: '{pattern}'")
        print(f"Результат: {result}")
        print()