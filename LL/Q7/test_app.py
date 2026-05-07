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
def test_delete_in_middle(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.deleteAtPosition(head, 2)
    assert linked_list_to_array(new_head) == [1, 2, 4, 5]

def test_delete_at_position_0(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.deleteAtPosition(head, 0)
    assert linked_list_to_array(new_head) == [2, 3]

def test_delete_at_last_position(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.deleteAtPosition(head, 2)
    assert linked_list_to_array(new_head) == [1, 2]

def test_delete_at_position_1(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.deleteAtPosition(head, 1)
    assert linked_list_to_array(new_head) == [1, 3]


# Edge cases
def test_delete_empty_list(sol):
    new_head = sol.deleteAtPosition(None, 0)
    assert linked_list_to_array(new_head) == []

def test_delete_single_element(sol):
    head = build_linked_list([1])
    new_head = sol.deleteAtPosition(head, 0)
    assert linked_list_to_array(new_head) == []

def test_delete_out_of_bounds(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.deleteAtPosition(head, 10)
    assert linked_list_to_array(new_head) == [1, 2, 3]

def test_delete_multiple_times(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    head = sol.deleteAtPosition(head, 1)
    head = sol.deleteAtPosition(head, 2)
    assert linked_list_to_array(head) == [1, 3, 5]

def test_delete_two_elements_first(sol):
    head = build_linked_list([1, 2])
    new_head = sol.deleteAtPosition(head, 0)
    assert linked_list_to_array(new_head) == [2]

def test_delete_two_elements_last(sol):
    head = build_linked_list([1, 2])
    new_head = sol.deleteAtPosition(head, 1)
    assert linked_list_to_array(new_head) == [1]