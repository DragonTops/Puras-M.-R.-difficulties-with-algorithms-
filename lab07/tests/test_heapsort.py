import pytest
from src.heapsort import heapsort, heapsort_inplace

def test_heapsort():
    arr = [4, 2, 8, 1, 5]
    sorted_arr = heapsort(arr)
    assert sorted_arr == [1, 2, 4, 5, 8]

def test_heapsort_inplace():
    arr = [4, 2, 8, 1, 5]
    heapsort_inplace(arr)
    assert arr == [1, 2, 4, 5, 8]

def test_heapsort_empty():
    arr = []
    sorted_arr = heapsort(arr)
    assert sorted_arr == []

def test_heapsort_single():
    arr = [1]
    sorted_arr = heapsort(arr)
    assert sorted_arr == [1]