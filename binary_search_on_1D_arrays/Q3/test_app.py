import pytest
from binary_search.Q3.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_target_in_left_half(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 5) == 1

def test_target_in_right_half(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_target_at_mid(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 7) == 3

def test_duplicates(sol):
    assert sol.search([3, 1, 3, 3, 3], 1) == 1

def test_target_not_found(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1


# Edge cases
def test_single_element_found(sol):
    assert sol.search([1], 1) == 0

def test_single_element_not_found(sol):
    assert sol.search([1], 0) == -1

def test_two_elements_found_left(sol):
    assert sol.search([3, 1], 3) == 0

def test_two_elements_found_right(sol):
    assert sol.search([3, 1], 1) == 1

def test_not_rotated(sol):
    assert sol.search([1, 2, 3, 4, 5], 3) == 2

def test_target_at_start(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 4) == 0

def test_target_at_end(sol):
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 2) == 6

def test_target_at_pivot(sol):
    assert sol.search([6, 7, 0, 1, 2, 4, 5], 0) == 2

def test_fully_rotated(sol):
    assert sol.search([2, 1], 1) == 1

def test_target_not_found_small(sol):
    assert sol.search([3, 1], 2) == -1

def test_large_array_found(sol):
    arr = list(range(500, 1000)) + list(range(0, 500))
    assert sol.search(arr, 0) == 500

def test_large_array_not_found(sol):
    arr = list(range(500, 1000)) + list(range(0, 500))
    assert sol.search(arr, 1001) == -1