import pytest
from app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4

def test_single_pile(sol):
    assert sol.minEatingSpeed([30], 5) == 6

def test_speed_equals_max_pile(sol):
    assert sol.minEatingSpeed([3, 6, 7, 11], 4) == 11

def test_plenty_of_hours(sol):
    assert sol.minEatingSpeed([3, 6, 7, 11], 20) == 2


# Edge cases
def test_one_hour_per_pile(sol):
    assert sol.minEatingSpeed([3, 6, 7, 11], 4) == 11

def test_all_same_piles(sol):
    assert sol.minEatingSpeed([5, 5, 5, 5], 4) == 5

def test_single_banana_piles(sol):
    assert sol.minEatingSpeed([1, 1, 1, 1], 4) == 1

def test_h_equals_piles_length(sol):
    assert sol.minEatingSpeed([3, 6, 7, 11], 4) == 11

def test_large_piles(sol):
    assert sol.minEatingSpeed([1000000000], 2) == 500000000

def test_two_piles(sol):
    assert sol.minEatingSpeed([10, 10], 4) == 5

def test_already_minimum(sol):
    assert sol.minEatingSpeed([1, 1, 1, 1, 1], 5) == 1

def test_large_array(sol):
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

def test_large_array_more_hours(sol):
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23