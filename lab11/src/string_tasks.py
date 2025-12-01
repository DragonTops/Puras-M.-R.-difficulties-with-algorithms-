from prefix_function import prefix_function
from z_function import z_function
from kmp_search import kmp_search


def find_string_period(s: str) -> int:
    """
    Нахождение минимального периода строки с помощью префикс-функции.
    
    Args:
        s: Входная строка
        
    Returns:
        Длина минимального периода строки
    """
    n = len(s)
    pi = prefix_function(s)
    
    # Период равен n - pi[n-1], если n делится на период
    period = n - pi[n - 1]
    
    if n % period == 0:
        return period
    else:
        return n  # Строка непериодическая


def are_cyclic_shifts(s1: str, s2: str) -> bool:
    """
    Проверка, является ли s2 циклическим сдвигом s1 с помощью Z-функции.
    
    Args:
        s1: Первая строка
        s2: Вторая строка
        
    Returns:
        True если s2 является циклическим сдвигом s1
    """
    if len(s1) != len(s2):
        return False
    
    # Создаем строку s1 + s1 и ищем s2
    combined = s1 + s1
    return len(kmp_search(combined, s2)) > 0


def find_all_occurrences(text: str, pattern: str) -> dict:
    """
    Поиск всех вхождений паттерна разными алгоритмами.
    
    Args:
        text: Текст для поиска
        pattern: Искомый паттерн
        
    Returns:
        Словарь с результатами разных алгоритмов
    """
    from kmp_search import kmp_search
    from z_search import z_search
    from rabin_karp import rabin_karp_search
    
    return {
        "KMP": kmp_search(text, pattern),
        "Z-функция": z_search(text, pattern),
        "Рабин-Карп": rabin_karp_search(text, pattern)
    }


if __name__ == "__main__":
    # Примеры решения практических задач
    
    print("=== Поиск периода строки ===")
    test_strings = ["abcabcabc", "aaa", "ababab", "abcde"]
    for s in test_strings:
        period = find_string_period(s)
        print(f"Строка: '{s}', период: {period}")
    print()
    
    print("=== Проверка циклического сдвига ===")
    test_pairs = [
        ("abcde", "cdeab"),
        ("abcde", "edcba"),
        ("hello", "llohe"),
        ("abc", "abc")
    ]
    for s1, s2 in test_pairs:
        result = are_cyclic_shifts(s1, s2)
        print(f"'{s1}' и '{s2}': {result}")
    print()
    
    print("=== Поиск всех вхождений разными алгоритмами ===")
    text = "ababcababacabababa"
    pattern = "aba"
    results = find_all_occurrences(text, pattern)
    
    print(f"Текст: '{text}'")
    print(f"Паттерн: '{pattern}'")
    for algorithm, occurrences in results.items():
        print(f"{algorithm}: {occurrences}")