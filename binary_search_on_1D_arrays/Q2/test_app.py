import pytest
from codex.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    assert sol.countOccurrences([1, 1, 1, 2, 2, 3, 3], 3) == 2

def test_target_appears_once(sol):
    assert sol.countOccurrences([1, 2, 3, 4, 5], 3) == 1

def test_target_appears_multiple(sol):
    assert sol.countOccurrences([1, 1, 1, 1, 1], 1) == 5

def test_target_not_in_array(sol):
    assert sol.countOccurrences([1, 2, 3, 4, 5], 6) == 0

# Edge cases
def test_empty_array(sol):
    assert sol.countOccurrences([], 3) == 0

def test_single_element_found(sol):
    assert sol.countOccurrences([3], 3) == 1

def test_single_element_not_found(sol):
    assert sol.countOccurrences([1], 3) == 0

def test_target_at_very_start(sol):
    assert sol.countOccurrences([2, 2, 2, 3, 4, 5], 2) == 3

def test_target_at_very_end(sol):
    assert sol.countOccurrences([1, 2, 3, 4, 5, 5, 5], 5) == 3

def test_all_same_elements(sol):
    assert sol.countOccurrences([7, 7, 7, 7, 7, 7], 7) == 6

def test_target_smaller_than_all(sol):
    assert sol.countOccurrences([2, 3, 4, 5], 1) == 0

def test_target_larger_than_all(sol):
    assert sol.countOccurrences([1, 2, 3, 4], 9) == 0

def test_two_elements_both_match(sol):
    assert sol.countOccurrences([4, 4], 4) == 2

def test_two_elements_no_match(sol):
    assert sol.countOccurrences([1, 2], 5) == 0

def test_large_array(sol):
    assert sol.countOccurrences(list(range(10000)), 5000) == 1

def test_large_array_all_same(sol):
    assert sol.countOccurrences([3] * 10000, 3) == 10000