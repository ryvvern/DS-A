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
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [7, 0, 8]

def test_different_lengths(sol):
    l1 = build_linked_list([9, 9])
    l2 = build_linked_list([1])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [0, 0, 1]

def test_carry_at_end(sol):
    l1 = build_linked_list([9, 9, 9])
    l2 = build_linked_list([1])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [0, 0, 0, 1]

def test_zeros(sol):
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [0]


# Edge cases
def test_single_digits(sol):
    l1 = build_linked_list([5])
    l2 = build_linked_list([5])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [0, 1]

def test_one_empty(sol):
    l1 = build_linked_list([1, 2, 3])
    l2 = build_linked_list([0])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [1, 2, 3]

def test_large_numbers(sol):
    l1 = build_linked_list([9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [8, 9, 9, 9, 1]

def test_all_carries(sol):
    l1 = build_linked_list([9, 9])
    l2 = build_linked_list([9, 9])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [8, 9, 1]

def test_unequal_lengths(sol):
    l1 = build_linked_list([1, 8])
    l2 = build_linked_list([0])
    assert linked_list_to_array(sol.addTwoNumbers(l1, l2)) == [1, 8]