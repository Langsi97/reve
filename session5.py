import networkx as nx
import matplotlib.pyplot as plt


def bfs(graph: nx.DiGraph, s):
    """
    Breath First Search:
    Given a graph and a starting node, compute a list of visited nodes.
    """
    ret = []

    visited = set()
    queue = [s]

    while len(queue) > 0:
        v = queue.pop(0)
        # visit
        visited.add(v)
        ret.append(v)
        
        # bfs
        for i in graph.neighbors(v):
            if i not in visited:
                queue.append(i)  # basically recursive call

    return ret


def get_shortest_path(graph: nx.DiGraph, s, e):
    """
    Computes shortest path between vertices s and e using BFS.
    """

    # If one of the nodes is not present, return -1
    if not graph.has_node(s) or not graph.has_node(e):
        return -1

    # Keep a value for every vertex representing the shortest distance
    # to s. Initialise all distances to -1.
    dist = dict()
    for v in graph:
        dist[v] = -1
    dist[s] = 0

    # Keep a set of visited nodes
    visited = set()
    queue = [s]

    while len(queue) > 0:
        v = queue.pop(0) 

        # visit
        visited.add(v)
        for u in graph.neighbors(v):
            if dist[v] + 1 < dist[u] or dist[u] == -1:
                dist[u] = dist[v] + 1

        # bfs
        for i in graph.neighbors(v):
            if i not in visited:
                queue.append(i)

    return dist[e]


def is_bipartite(graph):
    for v in graph:
        if not _dfs_is_bipartite_rec(graph, v, set(), dict({v: True})):
            return False
    return True


def _dfs_is_bipartite_rec(graph, v, visit, color):
    """
    Helper function testing bipartite property starting from a
    specific vertex.  Idea is that all vertices can be colored
    (True/False). But no two neighboring vertices can have the same
    color.
    """
    #visit
    visit.add(v)

    for u in graph.neighbors(v):
        if u not in color:
            color[u] = not color[v]
        elif color[u] == color[v]:
            return False
    
    #dfs
    for u in graph.neighbors(v):
        if u not in visit and not _dfs_is_bipartite_rec(graph, u, visit, color):
            return False

    return True    


def has_cycle(graph):
    for v in graph:
        if _has_cycle_dfs(graph, v, set(), set()):
            return True
    return False


def _has_cycle_dfs(graph, v, visit, mark):
    """
    We keep a "mark" information. We mark a node if we visit it, but
    after investigating the relevant subgraph, we must unmark these
    nodes. Otherwise we will report on a cycle too quickly.
    """

    # visit and mark
    visit.add(v)
    mark.add(v)

    for w in graph.neighbors(v):
        # we do regular DFS
        if w not in visit:
            return _has_cycle_dfs(graph, w, visit, mark)
        # if we encounter a marked node, report cycle.
        elif w in mark:
            return True

    # after visiting relevant subgraph, undo the mark for the current
    # node. By recursion this will be done for the whole subgraph.
    mark.remove(v)
    return False


def _dfs_is_bipartite(graph, v):
    """This is a non-recursive implementation of _dfs_is_bipartite_rec"""
    color = dict()
    color[v] = True

    visited = set()
    stack = [v]

    while len(stack) > 0:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for w in graph.neighbors(v):
                # color every node the oposite color from the predecessor
                if w not in color:
                    color[w] = not color[v]
                # if the node already has a color, then it must be
                # different. As soon as this is not the case, report
                # false.
                elif color[w] == color[v]:
                    return False
                stack.append(w)
    # if no neighboring vertices have the same color, we must reach
    # the end.
    return True