import random
from typing import List, Dict, Any

def generate_random(size: int) -> List[int]:
    return [random.randint(0, size * 10) for _ in range(size)]

def generate_sorted(size: int) -> List[int]:
    return list(range(size))

def generate_reversed(size: int) -> List[int]:
    return list(range(size, 0, -1))

def generate_almost_sorted(size: int, disorder_percentage: float = 0.05) -> List[int]:
    arr = list(range(size))
    num_disorder = int(size * disorder_percentage)
    
    for _ in range(num_disorder):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def generate_all_datasets(sizes: List[int] = None) -> Dict[str, List[Any]]:
    if sizes is None:
        sizes = [100, 1000, 5000, 10000]
    
    datasets = {}
    
    for size in sizes:
        datasets[f'random_{size}'] = generate_random(size)
        datasets[f'sorted_{size}'] = generate_sorted(size)
        datasets[f'reversed_{size}'] = generate_reversed(size)
        datasets[f'almost_sorted_{size}'] = generate_almost_sorted(size)
    
    return datasets

if __name__ == "__main__":
    datasets = generate_all_datasets()
    print("Сгенерированные наборы данных:")
    for name, data in datasets.items():
        print(f"{name}: первые 10 элементов {data[:10]}")