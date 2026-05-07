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
def test_delete_tail(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.deleteAtTail(head)
    assert linked_list_to_array(new_head) == [1, 2, 3, 4]

def test_delete_tail_two_elements(sol):
    head = build_linked_list([1, 2])
    new_head = sol.deleteAtTail(head)
    assert linked_list_to_array(new_head) == [1]

def test_delete_tail_single(sol):
    head = build_linked_list([1])
    new_head = sol.deleteAtTail(head)
    assert linked_list_to_array(new_head) == []


# Edge cases
def test_delete_tail_empty(sol):
    new_head = sol.deleteAtTail(None)
    assert linked_list_to_array(new_head) == []

def test_delete_tail_multiple_times(sol):
    head = build_linked_list([1, 2, 3])
    head = sol.deleteAtTail(head)
    head = sol.deleteAtTail(head)
    assert linked_list_to_array(head) == [1]

def test_delete_tail_large_list(sol):
    head = build_linked_list(list(range(1, 1000)))
    new_head = sol.deleteAtTail(head)
    assert linked_list_to_array(new_head)[-1] == 998