import pytest
from binary_search_on_answer.Q13.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    assert sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15

def test_standard_case_2(sol):
    assert sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6

def test_single_day(sol):
    assert sol.shipWithinDays([1, 2, 3, 4, 5], 1) == 15

def test_days_equal_packages(sol):
    assert sol.shipWithinDays([1, 2, 3, 4, 5], 5) == 5


# Edge cases
def test_single_package(sol):
    assert sol.shipWithinDays([10], 1) == 10

def test_all_same_weights(sol):
    assert sol.shipWithinDays([5, 5, 5, 5], 2) == 10

def test_two_packages_two_days(sol):
    assert sol.shipWithinDays([1, 2], 2) == 2

def test_two_packages_one_day(sol):
    assert sol.shipWithinDays([1, 2], 1) == 3

def test_large_weights(sol):
    assert sol.shipWithinDays([100, 200, 300, 400, 500], 3) == 600

def test_capacity_equals_max(sol):
    assert sol.shipWithinDays([10, 10, 10, 10], 4) == 10

def test_already_minimum(sol):
    assert sol.shipWithinDays([1, 2, 3, 1, 1], 4) == 3

def test_large_array(sol):
    assert sol.shipWithinDays(list(range(1, 11)), 10) == 10