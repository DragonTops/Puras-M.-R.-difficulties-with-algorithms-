import pytest
from src.priority_queue import PriorityQueue

def test_priority_queue():
    pq = PriorityQueue()
    pq.enqueue("task1", 3)
    pq.enqueue("task2", 1)
    pq.enqueue("task3", 2)
    
    assert pq.dequeue() == "task2"
    assert pq.dequeue() == "task3"
    assert pq.dequeue() == "task1"

def test_priority_queue_empty():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.dequeue()