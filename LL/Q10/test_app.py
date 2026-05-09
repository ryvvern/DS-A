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
def test_standard_case(sol):
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

def test_one_empty(sol):
    l1 = build_linked_list([1, 2, 3])
    l2 = build_linked_list([])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 2, 3]

def test_both_empty(sol):
    assert linked_list_to_array(sol.mergeTwoLists(None, None)) == []

def test_single_elements(sol):
    l1 = build_linked_list([1])
    l2 = build_linked_list([2])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 2]


# Edge cases
def test_all_same(sol):
    l1 = build_linked_list([1, 1, 1])
    l2 = build_linked_list([1, 1, 1])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 1, 1, 1, 1, 1]

def test_no_overlap(sol):
    l1 = build_linked_list([1, 2, 3])
    l2 = build_linked_list([4, 5, 6])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 2, 3, 4, 5, 6]

def test_second_empty(sol):
    l1 = build_linked_list([])
    l2 = build_linked_list([1, 2, 3])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 2, 3]

def test_different_lengths(sol):
    l1 = build_linked_list([1, 3, 5, 7])
    l2 = build_linked_list([2, 4])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [1, 2, 3, 4, 5, 7]

def test_negative_values(sol):
    l1 = build_linked_list([-3, -1, 0])
    l2 = build_linked_list([-2, 2, 4])
    assert linked_list_to_array(sol.mergeTwoLists(l1, l2)) == [-3, -2, -1, 0, 2, 4]