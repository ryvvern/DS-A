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
def test_reverse_standard(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == [5, 4, 3, 2, 1]

def test_reverse_two_elements(sol):
    head = build_linked_list([1, 2])
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == [2, 1]

def test_reverse_single(sol):
    head = build_linked_list([1])
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == [1]


# Edge cases
def test_reverse_empty(sol):
    new_head = sol.reverseList(None)
    assert linked_list_to_array(new_head) == []

def test_reverse_large(sol):
    head = build_linked_list(list(range(1, 1000)))
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == list(range(999, 0, -1))

def test_reverse_duplicates(sol):
    head = build_linked_list([1, 1, 2, 2, 3])
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == [3, 2, 2, 1, 1]

def test_reverse_negative(sol):
    head = build_linked_list([-1, -2, -3])
    new_head = sol.reverseList(head)
    assert linked_list_to_array(new_head) == [-3, -2, -1]