"""
author : [ Ambe Revelation Langsi ]
studentnumber : [ 2262920 ]
"""

import networkx as nx

# for drawing (visualization)
# import matplotlib.pyplot as plt
# import pydot
# from networkx.drawing.nx_pydot import graphviz_layout

""" Question 1
"""


def general_neighborhood(G, k, x):
    # If x is not in G, raise a KeyError with an error message
    if x not in G:
        raise KeyError(f'Oops, there is no node with label "{x}" in the graph')

    # Using DFS(depth first search) to find nodes within distance k of x
    stack = [(x, 0)]
    visited = {x}
    neighbors = {x}
    while stack:
        u, d = stack.pop()  # Pop the last element of the DFS stack
        if d < k:  # If the depth of the popped node is less than k
            for v in G[u]:  # Iterating over the neighbors of the popped node u
                if v not in visited:
                    # Adding the neighbor v to the set of visited nodes
                    visited.add(v)
                    # we apend the neighbor v onto the DFS stack with a depth of d+1
                    stack.append((v, d+1))
                    # finally, we add the neighbor v to the set of neighbors
                    neighbors.add(v)

    #  returning a list of the set of neighbors
    return list(neighbors)


"""----------------------------Question 2----------------------------------"""


def is_transitive(G):
    """
    Checking whether a given directed graph object G is transitive or not.
    """
    for x in G.nodes():
        for y in G.successors(x):
            for z in G.successors(y):
                if z not in G.successors(x):
                    return False
    return True


"""---------------Question 3-----------------------"""


def transitive_closure(G):
    """
    Returns the transitive closure graph of the input directed graph G.
    """
    T = nx.DiGraph(G)  # creating an object for a copy of G

    # Iterate over all pairs of nodes in G
    for u in G.nodes():
        for v in G.nodes():
            # Check if there is a path from u to v in G
            if nx.has_path(G, u, v):
                # Add an edge from u to v in T
                T.add_edge(u, v)

    return T
