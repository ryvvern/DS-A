import pytest
from binary_search_on_answer.Q12.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    assert sol.smallestDivisor([1, 2, 5, 9], 6) == 5

def test_standard_case_2(sol):
    assert sol.smallestDivisor([44, 22, 33, 11, 1], 5) == 44

def test_single_element(sol):
    assert sol.smallestDivisor([1], 1) == 1

def test_all_same(sol):
    assert sol.smallestDivisor([5, 5, 5, 5], 4) == 5


# Edge cases
def test_threshold_equals_length(sol):
    assert sol.smallestDivisor([1, 2, 3, 4, 5], 5) == 5

def test_large_threshold(sol):
    assert sol.smallestDivisor([1, 2, 3, 4, 5], 100) == 1

def test_divisor_is_one(sol):
    assert sol.smallestDivisor([1, 1, 1, 1], 4) == 1

def test_large_numbers(sol):
    assert sol.smallestDivisor([1000000, 1000000], 2) == 1000000

def test_two_elements(sol):
    assert sol.smallestDivisor([1, 2], 2) == 2

def test_threshold_is_one(sol):
    assert sol.smallestDivisor([1, 2, 3], 3) == 3

def test_already_minimum(sol):
    assert sol.smallestDivisor([2, 3, 4, 5], 4) == 5

def test_large_array(sol):
    assert sol.smallestDivisor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10