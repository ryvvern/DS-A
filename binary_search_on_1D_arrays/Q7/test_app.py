import pytest
from binary_search.Q7.app import Solution


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_peak_at_end(sol):
    assert sol.findPeakElement([1, 2, 3, 1]) == 2

def test_peak_in_middle(sol):
    result = sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    assert result in [1, 5]  # both are valid peaks

def test_peak_at_start(sol):
    assert sol.findPeakElement([5, 4, 3, 2, 1]) == 0

def test_peak_at_last(sol):
    assert sol.findPeakElement([1, 2, 3, 4, 5]) == 4

def test_single_element(sol):
    assert sol.findPeakElement([1]) == 0

def test_two_elements_peak_left(sol):
    assert sol.findPeakElement([2, 1]) == 0

def test_two_elements_peak_right(sol):
    assert sol.findPeakElement([1, 2]) == 1

def test_multiple_peaks(sol):
    result = sol.findPeakElement([1, 3, 2, 4, 1])
    assert result in [1, 3]  # both are valid peaks

def test_alternating(sol):
    result = sol.findPeakElement([1, 3, 1, 3, 1])
    assert result in [1, 3]

def test_large_array_peak_start(sol):
    arr = list(range(1000, 0, -1))
    assert sol.findPeakElement(arr) == 0

def test_large_array_peak_end(sol):
    arr = list(range(0, 1000))
    assert sol.findPeakElement(arr) == 999

def test_three_elements_peak_middle(sol):
    assert sol.findPeakElement([1, 3, 1]) == 1

def test_three_elements_peak_start(sol):
    assert sol.findPeakElement([3, 2, 1]) == 0

def test_three_elements_peak_end(sol):
    assert sol.findPeakElement([1, 2, 3]) == 2