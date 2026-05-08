import pytest
from app import Node, Solution


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_list(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    assert sol.length(head) == 5

def test_single_element(sol):
    head = build_linked_list([1])
    assert sol.length(head) == 1

def test_two_elements(sol):
    head = build_linked_list([1, 2])
    assert sol.length(head) == 2


# Edge cases
def test_empty_list(sol):
    assert sol.length(None) == 0

def test_large_list(sol):
    head = build_linked_list(list(range(1000)))
    assert sol.length(head) == 1000

def test_single_element_zero(sol):
    head = build_linked_list([0])
    assert sol.length(head) == 1

def test_negative_values(sol):
    head = build_linked_list([-1, -2, -3])
    assert sol.length(head) == 3