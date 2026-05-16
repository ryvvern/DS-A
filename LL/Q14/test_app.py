import pytest
from app import Node, Solution


def build_list(values, randoms):
    if not values:
        return None

    nodes = [Node(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    for i, r in enumerate(randoms):
        if r is not None:
            nodes[i].random = nodes[r]

    return nodes[0]


def list_to_array(head):
    result = []
    current = head
    while current:
        random_val = current.random.val if current.random else None
        result.append((current.val, random_val))
        current = current.next
    return result


@pytest.fixture
def sol():
    return Solution()


# Basic cases
def test_standard_case(sol):
    head = build_list([1, 2, 3], [2, 0, None])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, 3), (2, 1), (3, None)]

def test_all_random_none(sol):
    head = build_list([1, 2, 3], [None, None, None])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, None), (2, None), (3, None)]

def test_random_points_to_itself(sol):
    head = build_list([1, 2, 3], [0, 1, 2])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, 1), (2, 2), (3, 3)]

def test_single_element_no_random(sol):
    head = build_list([1], [None])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, None)]

def test_single_element_self_random(sol):
    head = build_list([1], [0])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, 1)]


# Edge cases
def test_empty_list(sol):
    copy = sol.copyRandomList(None)
    assert copy is None

def test_two_elements(sol):
    head = build_list([1, 2], [1, 0])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, 2), (2, 1)]

def test_copy_is_independent(sol):
    head = build_list([1, 2, 3], [None, None, None])
    copy = sol.copyRandomList(head)
    # modifying original shouldn't affect copy
    head.val = 99
    assert copy.val == 1

def test_random_points_to_head(sol):
    head = build_list([1, 2, 3], [None, 0, 0])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, None), (2, 1), (3, 1)]

def test_random_points_to_tail(sol):
    head = build_list([1, 2, 3], [2, 2, None])
    copy = sol.copyRandomList(head)
    assert list_to_array(copy) == [(1, 3), (2, 3), (3, None)]