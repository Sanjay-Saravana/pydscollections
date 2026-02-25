"""Heap data structures.

Contains a typed min-heap wrapper over :mod:`heapq`.
"""

from __future__ import annotations

import heapq
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    """A minimum heap with push/pop/peek operations."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._heap = list(values) if values is not None else []
        heapq.heapify(self._heap)

    def push(self, value: T) -> None:
        heapq.heappush(self._heap, value)

    def pop(self) -> T:
        if not self._heap:
            raise IndexError("pop from empty MinHeap")
        return heapq.heappop(self._heap)

    def peek(self) -> T:
        if not self._heap:
            raise IndexError("peek from empty MinHeap")
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)
