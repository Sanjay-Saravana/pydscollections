"""Linear data structures.

The module includes array- and list-based linear containers with practical,
Pythonic interfaces and robust input validation.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque as TypingDeque
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    """A resizable array wrapper with explicit append/pop operations.

    This class intentionally mirrors a subset of Python list behavior while
    keeping a focused API suitable for DSA practice and teaching.
    """

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._data: list[T] = list(values) if values is not None else []

    def append(self, value: T) -> None:
        """Append a value at the end of the array."""
        self._data.append(value)

    def pop(self) -> T:
        """Remove and return the last element.

        Raises:
            IndexError: If the array is empty.
        """
        if not self._data:
            raise IndexError("pop from empty DynamicArray")
        return self._data.pop()

    def get(self, index: int) -> T:
        """Return element at *index*.

        Raises:
            IndexError: If index is out of range.
        """
        return self._data[index]

    def set(self, index: int, value: T) -> None:
        """Update the element at *index* with *value*."""
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)


class Stack(Generic[T]):
    """LIFO stack implementation backed by list."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, value: T) -> None:
        self._items.append(value)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty Stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty Stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class Queue(Generic[T]):
    """FIFO queue implementation using :class:`collections.deque`."""

    def __init__(self) -> None:
        self._items: TypingDeque[T] = deque()

    def enqueue(self, value: T) -> None:
        self._items.append(value)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty Queue")
        return self._items.popleft()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty Queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class Deque(Generic[T]):
    """Double-ended queue with operations on both ends."""

    def __init__(self) -> None:
        self._items: TypingDeque[T] = deque()

    def append_left(self, value: T) -> None:
        self._items.appendleft(value)

    def append_right(self, value: T) -> None:
        self._items.append(value)

    def pop_left(self) -> T:
        if not self._items:
            raise IndexError("pop_left from empty Deque")
        return self._items.popleft()

    def pop_right(self) -> T:
        if not self._items:
            raise IndexError("pop_right from empty Deque")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


@dataclass
class _Node(Generic[T]):
    value: T
    next: _Node[T] | None = None


class SinglyLinkedList(Generic[T]):
    """A singly linked list supporting append and prepend operations."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0
        if values is not None:
            for value in values:
                self.append(value)

    def prepend(self, value: T) -> None:
        node = _Node(value=value, next=self._head)
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def append(self, value: T) -> None:
        node = _Node(value=value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("pop_front from empty SinglyLinkedList")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size
