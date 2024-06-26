#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""breadth_first_search.py

Breadth First Search (BFS) is a fundamental graph traversal algorithm. It involves visiting
all the connected nodes of a graph in a level-by-level manner.

Breadth First Search (BFS) is a graph traversal algorithm that explores all the vertices in a
graph at the current depth before moving on to the vertices at the next depth level. It starts
at a specified vertex and visits all its neighbors before moving on to the next level of neighbors.
BFS is commonly used in algorithms for pathfinding, connected components, and shortest path
problems in graphs.

Let's discuss the algorithm for the BFS:

1. Initialization: Enqueue the starting node into a queue and mark it as visited.
2. Exploration: While the queue is not empty:
  - Dequeue a node from the queue and visit it (e.g., print its value).
  - For each unvisited neighbor of the dequeued node:
    - Enqueue the neighbor into the queue.
    - Mark the neighbor as visited.
3. Termination: Repeat step 2 until the queue is empty.
"""

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


def main():
    """"""
    # Driver code
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)")
    g.BFS(2)

 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    main()