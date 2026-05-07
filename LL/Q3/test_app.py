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
def test_insert_at_tail(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.insertAtTail(head, 6)
    assert linked_list_to_array(new_head) == [1, 2, 3, 4, 5, 6]

def test_insert_at_tail_single(sol):
    head = build_linked_list([1])
    new_head = sol.insertAtTail(head, 2)
    assert linked_list_to_array(new_head) == [1, 2]

def test_insert_at_tail_empty(sol):
    new_head = sol.insertAtTail(None, 1)
    assert linked_list_to_array(new_head) == [1]

def test_insert_negative(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtTail(head, -1)
    assert linked_list_to_array(new_head) == [1, 2, 3, -1]

def test_insert_zero(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtTail(head, 0)
    assert linked_list_to_array(new_head) == [1, 2, 3, 0]

def test_insert_large_value(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtTail(head, 1000)
    assert linked_list_to_array(new_head) == [1, 2, 3, 1000]

def test_insert_multiple_times(sol):
    head = build_linked_list([1])
    head = sol.insertAtTail(head, 2)
    head = sol.insertAtTail(head, 3)
    head = sol.insertAtTail(head, 4)
    assert linked_list_to_array(head) == [1, 2, 3, 4]

def test_large_list(sol):
    head = build_linked_list(list(range(1, 1000)))
    new_head = sol.insertAtTail(head, 1000)
    assert linked_list_to_array(new_head)[-1] == 1000