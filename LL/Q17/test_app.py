import pytest
from LL.Q17.app import LRUCache


@pytest.fixture
def cache():
    return LRUCache(2)


# Basic cases
def test_get_existing(cache):
    cache.put(1, 1)
    assert cache.get(1) == 1

def test_get_missing(cache):
    assert cache.get(1) == -1

def test_put_and_get(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

def test_eviction(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    assert cache.get(2) == -1

def test_update_existing(cache):
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10


# Edge cases
def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

def test_evict_least_recent(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == -1

def test_get_updates_recency(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    assert cache.get(1) == 1
    assert cache.get(2) == -1
    assert cache.get(3) == 3

def test_large_capacity():
    cache = LRUCache(100)
    for i in range(100):
        cache.put(i, i)
    assert cache.get(0) == 0
    assert cache.get(99) == 99