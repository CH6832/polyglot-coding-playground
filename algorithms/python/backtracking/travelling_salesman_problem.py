#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

Rat in a maze is an example to display how backtrackng canbe
used to solve the problem.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/
"""

from sys import maxsize
from itertools import permutations

V = 4

def travelling_salesman_problem(graph: list[list], s: int):
    """Implementation of traveling Salesman Problem.

    Args:
        graph (Any): .
        s (Any): .

    Returns:
        int: Prints out results.
    """ 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
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
    travelling_salesman_problem()
