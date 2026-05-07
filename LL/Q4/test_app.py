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
def test_insert_in_middle(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.insertAtPosition(head, 99, 2)
    assert linked_list_to_array(new_head) == [1, 2, 99, 3, 4, 5]

def test_insert_at_position_0(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtPosition(head, 99, 0)
    assert linked_list_to_array(new_head) == [99, 1, 2, 3]

def test_insert_at_last_position(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtPosition(head, 99, 3)
    assert linked_list_to_array(new_head) == [1, 2, 3, 99]

def test_insert_at_position_1(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtPosition(head, 99, 1)
    assert linked_list_to_array(new_head) == [1, 99, 2, 3]


# Edge cases
def test_insert_empty_list(sol):
    new_head = sol.insertAtPosition(None, 99, 0)
    assert linked_list_to_array(new_head) == [99]

def test_insert_single_element(sol):
    head = build_linked_list([1])
    new_head = sol.insertAtPosition(head, 99, 1)
    assert linked_list_to_array(new_head) == [1, 99]

def test_insert_at_position_2(sol):
    head = build_linked_list([1, 2, 3, 4])
    new_head = sol.insertAtPosition(head, 99, 2)
    assert linked_list_to_array(new_head) == [1, 2, 99, 3, 4]

def test_insert_negative_value(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtPosition(head, -1, 1)
    assert linked_list_to_array(new_head) == [1, -1, 2, 3]

def test_insert_out_of_bounds(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtPosition(head, 99, 10)
    assert linked_list_to_array(new_head) == [1, 2, 3, 99]

def test_insert_multiple_times(sol):
    head = build_linked_list([1, 2, 3])
    head = sol.insertAtPosition(head, 99, 1)
    head = sol.insertAtPosition(head, 88, 3)
    assert linked_list_to_array(head) == [1, 99, 2, 88, 3]