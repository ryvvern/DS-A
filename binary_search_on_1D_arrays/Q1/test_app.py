import pytest
from binary_search.Q1.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_target_in_middle(sol):
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_target_appears_twice(sol):
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]

def test_target_fills_array(sol):
    assert sol.searchRange([8, 8, 8, 8, 8], 8) == [0, 4]

def test_target_not_in_array(sol):
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


# Edge cases
def test_empty_array(sol):
    assert sol.searchRange([], 0) == [-1, -1]

def test_single_element_found(sol):
    assert sol.searchRange([1], 1) == [0, 0]

def test_single_element_not_found(sol):
    assert sol.searchRange([1], 0) == [-1, -1]

def test_target_at_very_start(sol):
    assert sol.searchRange([2, 2, 3, 4, 5], 2) == [0, 1]

def test_target_at_very_end(sol):
    assert sol.searchRange([1, 2, 3, 4, 5, 5], 5) == [4, 5]

def test_target_appears_once(sol):
    assert sol.searchRange([1, 2, 3, 4, 5], 3) == [2, 2]

def test_all_elements_are_target(sol):
    assert sol.searchRange([3, 3, 3, 3], 3) == [0, 3]

def test_two_elements_both_match(sol):
    assert sol.searchRange([1, 1], 1) == [0, 1]

def test_two_elements_no_match(sol):
    assert sol.searchRange([1, 2], 3) == [-1, -1]

def test_target_on_left_side(sol):
    assert sol.searchRange([1, 1, 1, 2, 3, 4], 1) == [0, 2]

def test_target_on_right_side(sol):
    assert sol.searchRange([1, 2, 3, 4, 4, 4], 4) == [3, 5]

def test_large_array(sol):
    assert sol.searchRange(list(range(10000)), 5000) == [5000, 5000]

def test_target_smaller_than_all(sol):
    assert sol.searchRange([2, 3, 4, 5], 1) == [-1, -1]

def test_target_larger_than_all(sol):
    assert sol.searchRange([1, 2, 3, 4], 5) == [-1, -1]