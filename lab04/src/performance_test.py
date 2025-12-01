import time
import copy
from typing import List, Dict, Any
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from generate_data import generate_all_datasets

def test_sorting_algorithm(algorithm, data: List[int]) -> float:
    arr_copy = copy.deepcopy(data)
    start_time = time.time()
    algorithm(arr_copy)
    end_time = time.time()
    return end_time - start_time

def verify_sorting_correctness():
    test_data = [64, 34, 25, 12, 22, 11, 90]
    algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]
    
    for algo in algorithms:
        result = algo(copy.deepcopy(test_data))
        assert result == sorted(test_data), f"Алгоритм {algo.__name__} работает некорректно"
    print("Все алгоритмы сортируют корректно")

def run_performance_tests():
    datasets = generate_all_datasets()
    algorithms = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort, 
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'quick_sort': quick_sort
    }
    
    results = {}
    
    for algo_name, algorithm in algorithms.items():
        results[algo_name] = {}
        for data_name, data in datasets.items():
            time_taken = test_sorting_algorithm(algorithm, data)
            results[algo_name][data_name] = time_taken
            print(f"{algo_name} на {data_name}: {time_taken:.4f} сек")
    
    return results

if __name__ == "__main__":
    verify_sorting_correctness()
    results = run_performance_tests()