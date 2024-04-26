#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

The program implements a solution to the Traveling Salesman Problem (TSP), a classic problem
in graph theory and combinatorial optimization. The goal of the TSP is to find the shortest
possible route that visits every city exactly once and returns to the original city. In this
program, cities are repressented as vertices of a graph, and the distances between them are
represented by edge weights in the graph.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List

V = 4


def main() -> None:
    """Driving code and main function"""
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    init_vertex = 0    
    minimum_path = travelling_salesman_problem(graph, init_vertex)
    print(f"Minimum path weight is '{minimum_path}'")
 
    return None


def travelling_salesman_problem(graph: List[List[int]], s: int) -> int:
    """This function takes two arguments: graph, which represents the weighted graph as an adjacency matrix,
    and s, which is the starting vertex for the salesman. It computes the minimum Hamiltonian cycle (a
    cycle that visits each vertex exactly once and returns to the starting vertex) in the given graph. The
    function utilizes brute-force permutation to iterate through all possible permutations of vertices,
    calculating the total path weight for each permutation. It returns the minimum path weight among all
    permutations, which represents the shortest possible route for the salesman.

    Keyword arguments:
    graph (List[List[int]]) -- The adjacency matrix representing the weighted graph.
    s (int) -- The starting vertex for the salesman.
    """
    # store all vertex apart from source vertex
    vertex = []

    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    jls_extract_var = next_permutation

    for i in jls_extract_var:
        # store current Path weight(cost)
        current_pathweight = 0
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)
        
    return min_path


if __name__ == '__main__':
    main()

