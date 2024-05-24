package main

import (
    "fmt"
)

type Graph struct {
    V       int
    Adj     map[int][]int
    visited map[int]bool
    stack   []int
}

func (g *Graph) addEdge(u, v int) {
    g.Adj[u] = append(g.Adj[u], v)
}

func (g *Graph) topologicalSortUtil(v int) {
    g.visited[v] = true
    for _, i := range g.Adj[v] {
        if !g.visited[i] {
            g.topologicalSortUtil(i)
        }
    }
    g.stack = append(g.stack, v)
}

func (g *Graph) topologicalSort() {
    g.visited = make(map[int]bool)
    g.stack = make([]int, 0)
    for i := 0; i < g.V; i++ {
        if !g.visited[i] {
            g.topologicalSortUtil(i)
        }
    }
    for i := len(g.stack) - 1; i >= 0; i-- {
        fmt.Printf("%d ", g.stack[i])
    }
}

func main() {
    g := Graph{
        V:   6,
        Adj: make(map[int][]int),
    }
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    fmt.Println("Following is a Topological Sort of the given graph:")
    g.topologicalSort()
}
