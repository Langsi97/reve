from pytest import mark
import networkx as nx

from session5 import bfs, get_shortest_path, is_bipartite, has_cycle


@mark.parametrize("graph_edges, start, list",
                  [
                      ([(1, 2), (2, 3), (2, 4), (4, 3)], 1, [1, 2, 3, 4])
                  ])
def test_bfs(graph_edges, start, list):
    graph = nx.DiGraph()
    graph.add_edges_from(graph_edges)

    assert list == bfs(graph, start)


@mark.parametrize("graph_edges, source, dest, answer",
                  [
                      ([(1, 2), (1, 3), (3, 1), (3, 4), (2, 5), (5, 4)], 1, 4, 2),
                      ([(1, 3), (1, 4), (2, 1), (2, 3), (4, 3)], 1, 1, 0),
                      ([(1, 3), (1, 4), (2, 1), (2, 3), (4, 3)], 3, 1, -1)
                  ])
def test_shortest_path(graph_edges, source, dest, answer):
    graph = nx.DiGraph()
    graph.add_edges_from(graph_edges)

    assert answer == get_shortest_path(graph, source, dest)


@mark.parametrize("graph_edges, answer",
                  [
                      ([(1, 2), (2, 3), (3, 4), (4, 1)], True),
                      ([(1, 2), (2, 3), (3, 1)], False)
                  ])
def test_is_bipartite(graph_edges, answer):
    graph = nx.Graph()
    graph.add_edges_from(graph_edges)

    assert answer == is_bipartite(graph)


@mark.parametrize("graph_edges, answer",
                  [
                      ([(1, 2), (2, 1)], True),
                      ([(1, 2), (2, 3), (3, 1)], True),
                      ([(1, 2), (2, 3), (1, 3)], False)
                  ])
def test_has_cycle(graph_edges, answer):
    graph = nx.DiGraph()
    graph.add_edges_from(graph_edges)

    assert answer == has_cycle(graph)
