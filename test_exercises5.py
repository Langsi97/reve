from typing import Tuple, Dict, List
from pytest import mark
from exercises5 import bfs, get_shortest_path, is_bipartite, has_cycle  # type: ignore
import networkx as nx  # type: ignore


def _construct_graph(graph: Dict[int, List[int]]) -> 'nx.DiGraph[int]':
    my_graph = nx.DiGraph()
    for vertex in graph:
        my_graph.add_node(vertex)
        for child_vertex in graph[vertex]:
            my_graph.add_node(child_vertex)
            my_graph.add_edge(vertex, child_vertex)
    return my_graph


@mark.parametrize(
    "graph, start_vertex, expected",
    [
        (
            {0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]},
            0,
            [
                (0, 1, [0]),
                (1, 2, [1]),
                (2, 4, [2, 3]),
                (4, 8, [4, 5, 6, 7]),
                (8, 10, [8, 9]),
            ],
        ),
        (
            {0: [1], 1: [2, 3], 2: [3, 4], 3: [4], 4: [5, 6]},
            0,
            [(0, 1, [0]), (1, 2, [1]), (2, 4, [2, 3]), (4, 5, [4]), (5, 7, [5, 6])],
        ),
    ],
)
def test_bfs(
    graph: Dict[int, List[int]],
    start_vertex: int,
    expected: List[Tuple[int, int, List[int]]],
) -> None:
    my_graph = _construct_graph(graph)
    result = bfs(my_graph, start_vertex)
    for i, j, values in expected:
        assert set(result[i:j]) == set(values)


@mark.parametrize(
    "graph, start_vertex, end_vertex, expected",
    [
        ({0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]}, 0, 0, 0),
        ({0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]}, 0, 9, 4),
        ({0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]}, 1, 9, 3),
        ({0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]}, 1, 0, -1),
        ({0: [1], 1: [2, 3], 2: [3, 4], 3: [4], 4: [5, 6]}, 0, 6, 4),
        ({0: [1], 1: [2, 3], 2: [3, 4], 3: [4], 4: [5, 6]}, 5, 6, -1),
    ],
)
def test_get_shortest_path(
    graph: Dict[int, List[int]], start_vertex: int, end_vertex: int, expected: int
) -> None:
    my_graph = _construct_graph(graph)
    assert get_shortest_path(my_graph, start_vertex, end_vertex) == expected


@mark.parametrize(
    "graph, expected",
    [
        ({0: [3, 1], 1: [0, 2], 2: [1, 3], 3: [2, 0]}, True),
        ({0: [3, 1, 2], 1: [0, 2], 2: [1, 3, 0], 3: [2, 0]}, False),
        ({0: [1, 2], 1: [0, 2], 2: [0, 1]}, False),
        ({0: [1, 0], 1: [0]}, False),
        (
            {
                0: [1],
                1: [0, 2, 3],
                2: [1, 4, 5],
                3: [1, 6, 7],
                4: [2, 8, 9],
                5: [2],
                6: [3],
                7: [3],
                8: [4],
                9: [4],
            },
            True,
        ),
        (
            {0: [1], 1: [0, 2, 3], 2: [1], 3: [1], 4: [5, 6], 5: [4, 6], 6: [4, 5]},
            False,
        ),
        ({0: [1], 1: [0, 2, 3], 2: [1], 3: [1], 4: [5, 6], 5: [4], 6: [4]}, True),
    ],
)
def test_is_bipartite(graph: Dict[int, List[int]], expected: bool) -> None:
    my_graph = _construct_graph(graph)
    my_graph = nx.Graph(my_graph)
    assert is_bipartite(my_graph) == expected


@mark.parametrize(
    "graph, expected",
    [
        ({0: [1], 1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9]}, False),
        ({0: [1], 1: [2, 3], 2: [3, 4], 3: [4], 4: [5, 6]}, False),
        ({0: [1], 1: [2, 3], 2: [3], 3: [4], 4: [2, 5, 6]}, True),
        ({0: [1], 1: [2, 3], 2: [3], 4: [5], 5: [6], 6: [4]}, True),
        ({0: [1], 1: [2], 2: [2]}, True),
        ({0: [1], 1: [2], 2: [1]}, True),
        ({0: [1, 3], 1: [2, 3], 2: [3]}, False),
    ],
)
def test_has_cycle(graph: Dict[int, List[int]], expected: bool):
    my_graph = _construct_graph(graph)
    assert has_cycle(my_graph) == expected
