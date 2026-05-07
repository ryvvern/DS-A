import pytest
from binary_search_on_answer.Q11.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    assert sol.minDays([1, 10, 3, 10, 2], 3, 1) == 3

def test_standard_case_2(sol):
    assert sol.minDays([1, 10, 3, 10, 2], 3, 2) == -1

def test_single_bouquet(sol):
    assert sol.minDays([1, 2, 3, 4, 5], 1, 2) == 2

def test_all_same_days(sol):
    assert sol.minDays([1, 1, 1, 1, 1], 3, 1) == 1


# Edge cases
def test_impossible(sol):
    assert sol.minDays([1, 10, 3, 10, 2], 3, 2) == -1

def test_single_flower_single_bouquet(sol):
    assert sol.minDays([5], 1, 1) == 5

def test_exact_flowers_needed(sol):
    assert sol.minDays([1, 2, 3], 1, 3) == 3

def test_all_bloom_same_day(sol):
    assert sol.minDays([5, 5, 5, 5, 5], 2, 2) == 5

def test_large_bloom_days(sol):
    assert sol.minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2) == 9

def test_one_bouquet_one_flower(sol):
    assert sol.minDays([1, 2, 3, 4, 5], 1, 1) == 1

def test_need_all_flowers(sol):
    assert sol.minDays([1, 2, 3, 4, 5], 1, 5) == 5

def test_more_bouquets_than_possible(sol):
    assert sol.minDays([1, 2, 3], 4, 1) == -1

def test_large_k(sol):
    assert sol.minDays([1, 2, 3, 4, 5], 2, 3) == -1