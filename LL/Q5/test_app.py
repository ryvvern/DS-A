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
def test_delete_head(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.deleteAtHead(head)
    assert linked_list_to_array(new_head) == [2, 3, 4, 5]

def test_delete_head_single(sol):
    head = build_linked_list([1])
    new_head = sol.deleteAtHead(head)
    assert linked_list_to_array(new_head) == []

def test_delete_head_two_elements(sol):
    head = build_linked_list([1, 2])
    new_head = sol.deleteAtHead(head)
    assert linked_list_to_array(new_head) == [2]


# Edge cases
def test_delete_head_empty(sol):
    new_head = sol.deleteAtHead(None)
    assert linked_list_to_array(new_head) == []

def test_delete_head_multiple_times(sol):
    head = build_linked_list([1, 2, 3])
    head = sol.deleteAtHead(head)
    head = sol.deleteAtHead(head)
    assert linked_list_to_array(head) == [3]

def test_delete_head_large_list(sol):
    head = build_linked_list(list(range(1, 1000)))
    new_head = sol.deleteAtHead(head)
    assert linked_list_to_array(new_head)[0] == 2