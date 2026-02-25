from dscollections import BinarySearchTree, Graph, MinHeap


def test_bst_insertion_and_traversal() -> None:
    bst = BinarySearchTree[int]()
    for value in [10, 5, 15, 12, 18, 5]:
        bst.insert(value)

    assert 12 in bst
    assert 7 not in bst
    assert list(bst.in_order()) == [5, 10, 12, 15, 18]
    assert len(bst) == 5


def test_graph_bfs_and_dfs() -> None:
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    bfs_path = list(graph.bfs("A"))
    dfs_path = list(graph.dfs("A"))

    assert bfs_path[0] == "A"
    assert set(bfs_path) == {"A", "B", "C", "D"}
    assert dfs_path[0] == "A"
    assert set(dfs_path) == {"A", "B", "C", "D"}


def test_min_heap() -> None:
    heap = MinHeap([5, 2, 7])
    heap.push(1)
    assert heap.peek() == 1
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert len(heap) == 2
