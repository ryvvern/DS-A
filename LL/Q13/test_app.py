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
def test_remove_second_from_end(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.removeNthFromEnd(head, 2)
    assert linked_list_to_array(new_head) == [1, 2, 3, 5]

def test_remove_last(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.removeNthFromEnd(head, 1)
    assert linked_list_to_array(new_head) == [1, 2, 3, 4]

def test_remove_first(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.removeNthFromEnd(head, 5)
    assert linked_list_to_array(new_head) == [2, 3, 4, 5]

def test_remove_middle(sol):
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.removeNthFromEnd(head, 3)
    assert linked_list_to_array(new_head) == [1, 2, 4, 5]


# Edge cases
def test_single_element(sol):
    head = build_linked_list([1])
    new_head = sol.removeNthFromEnd(head, 1)
    assert linked_list_to_array(new_head) == []

def test_two_elements_remove_last(sol):
    head = build_linked_list([1, 2])
    new_head = sol.removeNthFromEnd(head, 1)
    assert linked_list_to_array(new_head) == [1]

def test_two_elements_remove_first(sol):
    head = build_linked_list([1, 2])
    new_head = sol.removeNthFromEnd(head, 2)
    assert linked_list_to_array(new_head) == [2]

def test_large_list(sol):
    head = build_linked_list(list(range(1, 11)))
    new_head = sol.removeNthFromEnd(head, 5)
    assert linked_list_to_array(new_head) == [1, 2, 3, 4, 5, 7, 8, 9, 10]