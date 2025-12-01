"""
Реализация алгоритмов динамического программирования
"""

from typing import List, Dict, Any

def fibonacci_naive(n: int) -> int:
    """Наивная рекурсивная реализация Фибоначчи. Сложность O(2^n)."""
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """Фибоначчи с мемоизацией. Сложность O(n)."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_tabular(n: int) -> int:
    """Табличная реализация Фибоначчи. Сложность O(n)."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Задача о рюкзаке 0-1. 
    Сложность: O(n×W), где n - количество предметов, W - вместимость.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def lcs(str1: str, str2: str) -> int:
    """
    Наибольшая общая подпоследовательность.
    Сложность: O(m×n), где m, n - длины строк.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Расстояние Левенштейна.
    Сложность: O(m×n), где m, n - длины строк.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
            
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # удаление
                    dp[i][j-1],    # вставка  
                    dp[i-1][j-1]   # замена
                )
    
    return dp[m][n]

if __name__ == "__main__":
    # Демонстрация работы алгоритмов
    print("Фибоначчи (n=10):")
    print(f"Наивный: {fibonacci_naive(10)}")
    print(f"Мемоизация: {fibonacci_memo(10)}")
    print(f"Табличный: {fibonacci_tabular(10)}")
    
    print("\nРюкзак 0-1:")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print(f"Максимальная стоимость: {knapsack_01(weights, values, capacity)}")
    
    print("\nLCS:")
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    print(f"Длина LCS: {lcs(str1, str2)}")
    
    print("\nРасстояние Левенштейна:")
    print(f"Дистанция: {levenshtein_distance('kitten', 'sitting')}")