import pytest
from binary_search.Q6.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_single_in_middle(sol):
    assert sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2

def test_single_at_start(sol):
    assert sol.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4]) == 1

def test_single_at_end(sol):
    assert sol.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4]) == 4

def test_single_element(sol):
    assert sol.singleNonDuplicate([1]) == 1

def test_three_elements_start(sol):
    assert sol.singleNonDuplicate([1, 2, 2]) == 1

def test_three_elements_end(sol):
    assert sol.singleNonDuplicate([1, 1, 2]) == 2

def test_larger_array(sol):
    assert sol.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]) == 5

def test_single_between_pairs(sol):
    assert sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10

def test_two_pairs_single_start(sol):
    assert sol.singleNonDuplicate([1, 2, 2, 3, 3]) == 1

def test_two_pairs_single_end(sol):
    assert sol.singleNonDuplicate([1, 1, 2, 2, 3]) == 3

def test_large_array_single_middle(sol):
    assert sol.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]) == 7

def test_large_array_single_start(sol):
    assert sol.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 1