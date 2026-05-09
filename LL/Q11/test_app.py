import pytest
from LL.Q11.app import Node, Solution


@pytest.fixture
def sol():
    return Solution()


def build_cycle(values, pos):
    if not values:
        return None
    head = Node(values[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i, val in enumerate(values[1:], 1):
        current.next = Node(val)
        current = current.next
        if i == pos:
            cycle_node = current

    # create cycle
    if cycle_node:
        current.next = cycle_node

    return head


# Basic cases
def test_cycle_exists(sol):
    head = build_cycle([3, 2, 0, 4], 1)
    assert sol.hasCycle(head) == True

def test_no_cycle(sol):
    head = build_cycle([1, 2, 3, 4], -1)
    assert sol.hasCycle(head) == False

def test_cycle_at_head(sol):
    head = build_cycle([1, 2, 3], 0)
    assert sol.hasCycle(head) == True


# Edge cases
def test_empty_list(sol):
    assert sol.hasCycle(None) == False

def test_single_no_cycle(sol):
    head = build_cycle([1], -1)
    assert sol.hasCycle(head) == False

def test_two_elements_cycle(sol):
    head = build_cycle([1, 2], 0)
    assert sol.hasCycle(head) == True

def test_two_elements_no_cycle(sol):
    head = build_cycle([1, 2], -1)
    assert sol.hasCycle(head) == False

def test_large_cycle(sol):
    head = build_cycle(list(range(1000)), 500)
    assert sol.hasCycle(head) == True

def test_large_no_cycle(sol):
    head = build_cycle(list(range(1000)), -1)
    assert sol.hasCycle(head) == False