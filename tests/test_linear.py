from dscollections import Deque, DynamicArray, Queue, SinglyLinkedList, Stack


def test_dynamic_array() -> None:
    arr = DynamicArray([1, 2])
    arr.append(3)
    assert len(arr) == 3
    assert arr.get(1) == 2
    arr.set(1, 20)
    assert list(arr) == [1, 20, 3]
    assert arr.pop() == 3


def test_stack() -> None:
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_queue() -> None:
    queue = Queue[str]()
    queue.enqueue("x")
    queue.enqueue("y")
    assert queue.peek() == "x"
    assert queue.dequeue() == "x"
    assert queue.dequeue() == "y"


def test_deque() -> None:
    d = Deque[int]()
    d.append_right(2)
    d.append_left(1)
    d.append_right(3)
    assert d.pop_left() == 1
    assert d.pop_right() == 3
    assert d.pop_left() == 2


def test_singly_linked_list() -> None:
    linked = SinglyLinkedList([2, 3])
    linked.prepend(1)
    linked.append(4)
    assert list(linked) == [1, 2, 3, 4]
    assert linked.pop_front() == 1
    assert len(linked) == 3
