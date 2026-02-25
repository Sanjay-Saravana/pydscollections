"""Tree data structures.

Includes a generic Binary Search Tree with insertion, search, and in-order
traversal utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Generic, TypeVar

T = TypeVar("T")


@dataclass
class _BSTNode(Generic[T]):
    value: T
    left: _BSTNode[T] | None = None
    right: _BSTNode[T] | None = None


class BinarySearchTree(Generic[T]):
    """A basic unbalanced Binary Search Tree (BST).

    Values are inserted according to standard BST ordering.
    Duplicate values are ignored to keep membership deterministic.
    """

    def __init__(self) -> None:
        self._root: _BSTNode[T] | None = None
        self._size = 0

    def insert(self, value: T) -> None:
        """Insert *value* into the tree if it is not already present."""
        if self._root is None:
            self._root = _BSTNode(value)
            self._size += 1
            return

        current = self._root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = _BSTNode(value)
                    self._size += 1
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = _BSTNode(value)
                    self._size += 1
                    return
                current = current.right
            else:
                return

    def contains(self, value: T) -> bool:
        """Return ``True`` if *value* exists in the tree."""
        current = self._root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def in_order(self) -> Generator[T, None, None]:
        """Yield values in sorted order."""

        def walk(node: _BSTNode[T] | None) -> Generator[T, None, None]:
            if node is None:
                return
            yield from walk(node.left)
            yield node.value
            yield from walk(node.right)

        yield from walk(self._root)

    def __contains__(self, value: T) -> bool:
        return self.contains(value)

    def __len__(self) -> int:
        return self._size
