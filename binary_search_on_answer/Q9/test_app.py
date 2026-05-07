import pytest
from app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_square_root(sol):
    assert sol.nthRoot(2, 9) == 3

def test_cube_root(sol):
    assert sol.nthRoot(3, 27) == 3

def test_fourth_root(sol):
    assert sol.nthRoot(4, 16) == 2

def test_fifth_root(sol):
    assert sol.nthRoot(5, 32) == 2


# Edge cases
def test_zero(sol):
    assert sol.nthRoot(2, 0) == 0

def test_one(sol):
    assert sol.nthRoot(2, 1) == 1

def test_first_root(sol):
    assert sol.nthRoot(1, 5) == 5

def test_large_perfect(sol):
    assert sol.nthRoot(3, 1000) == 10

def test_large_square(sol):
    assert sol.nthRoot(2, 10000) == 100

def test_cube_root_large(sol):
    assert sol.nthRoot(3, 125) == 5

def test_fourth_root_large(sol):
    assert sol.nthRoot(4, 625) == 5

def test_square_root_small(sol):
    assert sol.nthRoot(2, 4) == 2