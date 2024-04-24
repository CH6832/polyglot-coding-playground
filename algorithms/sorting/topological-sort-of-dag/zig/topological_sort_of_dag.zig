const std = @import("std");
const HashMap = std.HashMap;
const Vec = std.ArrayList;

pub struct Graph {
    graph: HashMap<usize, Vec<usize>>,
    V: usize,
}

pub fn Graph.init(vertices: usize) Graph {
    return Graph { .graph = HashMap.init(u64, Vec([]usize{})), .V = vertices };
}

pub fn (g: *Graph) addEdge(u: usize, v: usize) void {
    if (!g.graph.containsKey(u)) {
        g.graph.put(u, Vec([]usize{}));
    }
    g.graph.get(u).unwrap().append(v);
}

pub fn (g: *Graph) topologicalSortUtil(v: usize, visited: []bool, stack: *std.ArrayList(usize)) void {
    visited[v] = true;
    if (g.graph.containsKey(v)) {
        const edges = g.graph.get(v).unwrap();
        for (edges) |i| {
            if (!visited[i]) {
                g.topologicalSortUtil(i, visited, stack);
            }
        }
    }
    stack.unshift(v);
}

pub fn (g: *Graph) topologicalSort() void {
    const visited = [_]bool{false} ** g.V;
    var stack = std.ArrayList(usize).init(8);

    for (g.V) |i| {
        if (!visited[i]) {
            g.topologicalSortUtil(i, visited, &stack);
        }
    }

    while (!stack.empty()) {
        const v = stack.pop();
        std.debug.print("{d} ", .{v});
    }
    std.debug.print("\n", .{});
}

pub fn main() void {
    var g = Graph.init(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    
    std.debug.print("Following is a Topological Sort of the given graph\n", .{});
    g.topologicalSort();
}
