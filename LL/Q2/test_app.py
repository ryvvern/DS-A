import pytest
from LL.Q2.app import Node, Solution


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
def test_insert_at_head(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.insertAtHead(head, 0)
    assert linked_list_to_array(new_head) == [0, 1, 2, 3, 4, 5]

def test_insert_at_head_single(sol):
    head = build_linked_list([1])
    new_head = sol.insertAtHead(head, 0)
    assert linked_list_to_array(new_head) == [0, 1]

def test_insert_at_head_empty(sol):
    new_head = sol.insertAtHead(None, 1)
    assert linked_list_to_array(new_head) == [1]

def test_insert_negative(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtHead(head, -1)
    assert linked_list_to_array(new_head) == [-1, 1, 2, 3]

def test_insert_zero(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtHead(head, 0)
    assert linked_list_to_array(new_head) == [0, 1, 2, 3]

def test_insert_large_value(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtHead(head, 1000)
    assert linked_list_to_array(new_head) == [1000, 1, 2, 3]

def test_insert_multiple_times(sol):
    head = build_linked_list([3])
    head = sol.insertAtHead(head, 2)
    head = sol.insertAtHead(head, 1)
    head = sol.insertAtHead(head, 0)
    assert linked_list_to_array(head) == [0, 1, 2, 3]

def test_original_list_intact(sol):
    head = build_linked_list([1, 2, 3])
    new_head = sol.insertAtHead(head, 0)
    assert linked_list_to_array(new_head) == [0, 1, 2, 3]