"""
Решение практических задач с использованием ДП
"""

from typing import List, Tuple
from dynamic_programming import lcs, knapsack_01

def coin_change(coins: List[int], amount: int) -> int:
    """
    Размен монет - минимальное количество монет для суммы.
    Сложность: O(n×amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def lis(sequence: List[int]) -> int:
    """
    Наибольшая возрастающая подпоследовательность.
    Сложность: O(n²)
    """
    if not sequence:
        return 0
        
    n = len(sequence)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lcs_with_reconstruction(str1: str, str2: str) -> Tuple[int, str]:
    """LCS с восстановлением подпоследовательности."""
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Заполнение таблицы
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Восстановление решения
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str = str1[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], lcs_str

def knapsack_with_reconstruction(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    """Задача о рюкзаке с восстановлением выбранных предметов."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Восстановление решения
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected

if __name__ == "__main__":
    # Демонстрация решения задач
    print("Размен монет:")
    coins = [1, 3, 4]
    amount = 6
    result = coin_change(coins, amount)
    print(f"Минимальное количество монет для {amount}: {result}")
    
    print("\nНаибольшая возрастающая подпоследовательность:")
    sequence = [10, 9, 2, 5, 3, 7, 101, 18]
    result = lis(sequence)
    print(f"Длина LIS: {result}")
    
    print("\nLCS с восстановлением:")
    str1 = "ABCDGH" 
    str2 = "AEDFHR"
    length, subsequence = lcs_with_reconstruction(str1, str2)
    print(f"Длина: {length}, Подпоследовательность: {subsequence}")
    
    print("\nРюкзак с восстановлением:")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_value, items = knapsack_with_reconstruction(weights, values, capacity)
    print(f"Макс. стоимость: {max_value}, Выбранные предметы: {items}")