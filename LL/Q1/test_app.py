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
def test_target_in_middle(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    assert sol.search(head, 3) == True

def test_target_at_head(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    assert sol.search(head, 1) == True

def test_target_at_tail(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    assert sol.search(head, 5) == True

def test_target_not_found(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    assert sol.search(head, 7) == False


# Edge cases
def test_empty_list(sol):
    head = build_linked_list([])
    assert sol.search(head, 1) == False

def test_single_element_found(sol):
    head = build_linked_list([5])
    assert sol.search(head, 5) == True

def test_single_element_not_found(sol):
    head = build_linked_list([5])
    assert sol.search(head, 3) == False

def test_duplicate_values(sol):
    head = build_linked_list([1, 2, 2, 3])
    assert sol.search(head, 2) == True

def test_negative_values(sol):
    head = build_linked_list([-3, -2, -1, 0])
    assert sol.search(head, -2) == True

def test_large_list(sol):
    head = build_linked_list(list(range(1000)))
    assert sol.search(head, 999) == True

def test_large_list_not_found(sol):
    head = build_linked_list(list(range(1000)))
    assert sol.search(head, 1001) == False