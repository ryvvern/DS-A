import pytest
from app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_perfect_square(sol):
    assert sol.mySqrt(4) == 2

def test_perfect_square_large(sol):
    assert sol.mySqrt(16) == 4

def test_non_perfect_square(sol):
    assert sol.mySqrt(8) == 2

def test_non_perfect_square_large(sol):
    assert sol.mySqrt(15) == 3


# Edge cases
def test_zero(sol):
    assert sol.mySqrt(0) == 0

def test_one(sol):
    assert sol.mySqrt(1) == 1

def test_two(sol):
    assert sol.mySqrt(2) == 1

def test_three(sol):
    assert sol.mySqrt(3) == 1

def test_large_perfect_square(sol):
    assert sol.mySqrt(10000) == 100

def test_large_non_perfect_square(sol):
    assert sol.mySqrt(9999) == 99

def test_nine(sol):
    assert sol.mySqrt(9) == 3

def test_twenty_five(sol):
    assert sol.mySqrt(25) == 5

def test_just_below_perfect_square(sol):
    assert sol.mySqrt(24) == 4

def test_just_above_perfect_square(sol):
    assert sol.mySqrt(26) == 5

def test_very_large(sol):
    assert sol.mySqrt(2147483647) == 46340