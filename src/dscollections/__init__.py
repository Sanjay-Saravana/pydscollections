"""dscollections: A polished data-structures package for Python.

This package provides reusable, type-safe, and documented implementations of
foundational data structures for learning and practical software development.
"""

from .graph import Graph
from .heap import MinHeap
from .linear import Deque, DynamicArray, Queue, SinglyLinkedList, Stack
from .tree import BinarySearchTree

__all__ = [
    "DynamicArray",
    "Stack",
    "Queue",
    "Deque",
    "SinglyLinkedList",
    "BinarySearchTree",
    "Graph",
    "MinHeap",
]
