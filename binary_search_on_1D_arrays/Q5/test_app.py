import pytest
from binary_search.Q5.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_rotated_three_times(sol):
    assert sol.countRotations([3, 4, 5, 1, 2]) == 3

def test_rotated_four_times(sol):
    assert sol.countRotations([4, 5, 6, 7, 0, 1, 2]) == 4

def test_rotated_once(sol):
    assert sol.countRotations([2, 1]) == 1

def test_not_rotated(sol):
    assert sol.countRotations([1, 2, 3, 4, 5]) == 0


# Edge cases
def test_single_element(sol):
    assert sol.countRotations([1]) == 0

def test_two_elements_not_rotated(sol):
    assert sol.countRotations([1, 2]) == 0

def test_two_elements_rotated(sol):
    assert sol.countRotations([2, 1]) == 1

def test_min_at_start(sol):
    assert sol.countRotations([1, 2, 3, 4, 5]) == 0

def test_min_at_end(sol):
    assert sol.countRotations([2, 3, 4, 5, 1]) == 4

def test_min_in_middle(sol):
    assert sol.countRotations([4, 5, 1, 2, 3]) == 2

def test_large_rotation(sol):
    assert sol.countRotations([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5

def test_large_array(sol):
    arr = list(range(500, 1000)) + list(range(0, 500))
    assert sol.countRotations(arr) == 500