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


def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_even_length(sol):
    head = build_linked_list([1, 2, 3, 4])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 4, 2, 3]

def test_odd_length(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 5, 2, 4, 3]

def test_three_elements(sol):
    head = build_linked_list([1, 2, 3])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 3, 2]

def test_two_elements(sol):
    head = build_linked_list([1, 2])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 2]


# Edge cases
def test_single_element(sol):
    head = build_linked_list([1])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1]

def test_empty_list(sol):
    sol.reorderList(None)

def test_six_elements(sol):
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 6, 2, 5, 3, 4]

def test_large_list(sol):
    head = build_linked_list(list(range(1, 7)))
    sol.reorderList(head)
    assert linked_list_to_array(head) == [1, 6, 2, 5, 3, 4]