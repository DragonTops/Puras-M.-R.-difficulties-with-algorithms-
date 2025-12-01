import pytest
from src.heap import MinHeap, MaxHeap

def test_min_heap_insert_extract():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() == 8

def test_min_heap_build():
    heap = MinHeap()
    heap.build_heap([5, 3, 8, 1, 2])
    
    assert heap.extract_min() == 1
    assert heap.extract_min() == 2
    assert heap.extract_min() == 3

def test_max_heap_insert_extract():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    
    assert heap.extract_max() == 8
    assert heap.extract_max() == 5
    assert heap.extract_max() == 3

def test_empty_heap():
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.extract_min()