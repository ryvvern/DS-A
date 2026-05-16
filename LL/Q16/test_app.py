import pytest
from app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case_1(sol):
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2

def test_standard_case_2(sol):
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3

def test_duplicate_at_start(sol):
    assert sol.findDuplicate([1, 1, 2, 3, 4]) == 1

def test_duplicate_at_end(sol):
    assert sol.findDuplicate([1, 2, 3, 4, 4]) == 4


# Edge cases
def test_two_elements(sol):
    assert sol.findDuplicate([1, 1]) == 1

def test_duplicate_is_one(sol):
    assert sol.findDuplicate([1, 1, 2, 3]) == 1

def test_duplicate_is_last(sol):
    assert sol.findDuplicate([2, 1, 3, 3]) == 3

def test_large_array(sol):
    arr = list(range(1, 1001)) + [500]
    import random
    random.shuffle(arr)
    assert sol.findDuplicate(arr) == 500

def test_all_same(sol):
    assert sol.findDuplicate([2, 2, 2, 2, 2]) == 2

def test_duplicate_in_middle(sol):
    assert sol.findDuplicate([1, 4, 3, 2, 3]) == 3