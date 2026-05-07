import pytest
from binary_search.Q4.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_rotated(sol):
    assert sol.findMin([3, 4, 5, 1, 2]) == 1

def test_rotated_at_start(sol):
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0

def test_rotated_once(sol):
    assert sol.findMin([2, 1]) == 1

def test_not_rotated(sol):
    assert sol.findMin([1, 2, 3, 4, 5]) == 1


# Edge cases
def test_single_element(sol):
    assert sol.findMin([1]) == 1

def test_two_elements_rotated(sol):
    assert sol.findMin([3, 1]) == 1

def test_two_elements_not_rotated(sol):
    assert sol.findMin([1, 2]) == 1

def test_min_at_start(sol):
    assert sol.findMin([1, 2, 3, 4, 5]) == 1

def test_min_at_end(sol):
    assert sol.findMin([2, 3, 4, 5, 1]) == 1

def test_min_in_middle(sol):
    assert sol.findMin([4, 5, 1, 2, 3]) == 1

def test_large_rotation(sol):
    assert sol.findMin([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1

def test_fully_rotated(sol):
    assert sol.findMin([2, 3, 4, 5, 1]) == 1

def test_negative_numbers(sol):
    assert sol.findMin([0, 1, 2, -3, -2, -1]) == -3

def test_large_array(sol):
    arr = list(range(500, 1000)) + list(range(0, 500))
    assert sol.findMin(arr) == 0