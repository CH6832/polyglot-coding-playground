#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nearest_neighbour_with_kd_tree.py.py



.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List

V = 4


def main() -> None:
    """Driving code and main function"""
    # Example usage
    graph = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7),
             (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10),
             (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    
    minimum_spanning_tree = kruskal(graph)
    print("Minimum Spanning Tree:")
    for edge in minimum_spanning_tree:
        print(edge)
 
    return None


class UnionFind:
    """A data structure for implementing Union-Find operations."""
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u: int) -> int:
        """Find the parent of the given element u."""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        """Union the sets containing elements u and v."""
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(graph: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Find the minimum spanning tree of a graph using Kruskal's algorithm.

    Args:
        graph (List[Tuple[int, int, int]]): An edge-weighted graph represented as a list of tuples (u, v, weight).

    Returns:
        List[Tuple[int, int, int]]: The minimum spanning tree represented as a list of tuples (u, v, weight).
    """
    # Sort edges by weight
    graph.sort(key=lambda x: x[2])
    
    # Initialize union-find data structure
    n = len(graph)
    uf = UnionFind(n)
    
    # Initialize minimum spanning tree
    mst = []
    
    # Iterate through edges in increasing order of weight
    for edge in graph:
        u, v, weight = edge
        # Check if adding edge creates a cycle
        if uf.find(u) != uf.find(v):
            # Add edge to MST
            mst.append(edge)
            # Union the sets containing u and v
            uf.union(u, v)
    
    return mst


if __name__ == '__main__':
    main()

