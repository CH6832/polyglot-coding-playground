const std = @import("std");
const println = std.debug.print;

pub struct Graph {
    V: usize,
    graph: [][3]usize,
}

pub fn Graph.init(vertices: usize) Graph {
    return Graph { .V = vertices, .graph = [][]usize{} };
}

pub fn (g: *Graph) addEdge(u: usize, v: usize, w: usize) void {
    g.graph.append([u, v, w]);
}

pub fn (g: *Graph) find(parent: []usize, i: usize) usize {
    if (parent[i] != i) {
        parent[i] = g.find(parent, parent[i]);
    }
    return parent[i];
}

pub fn (g: *Graph) union(parent: []usize, rank: []usize, x: usize, y: usize) void {
    if (rank[x] < rank[y]) {
        parent[x] = y;
    } else if (rank[x] > rank[y]) {
        parent[y] = x;
    } else {
        parent[y] = x;
        rank[x] += 1;
    }
}

pub fn (g: *Graph) KruskalMST() void {
    var result = [][]usize{};
    var i: usize = 0;
    var e: usize = 0;
    g.graph = g.graph.sortedBy([]fn(a: [3]usize, b: [3]usize) i32 {
        return a[2] - b[2];
    });

    var parent = []usize{0} ** g.V;
    var rank = []usize{0} ** g.V;

    for (g.V) |node| {
        parent[node] = node;
        rank[node] = 0;
    }

    while (e < g.V - 1) {
        const u = g.graph[i][0];
        const v = g.graph[i][1];
        const w = g.graph[i][2];
        i += 1;

        const x = g.find(parent, u);
        const y = g.find(parent, v);

        if (x != y) {
            e += 1;
            result.append([u, v, w]);
            g.union(parent, rank, x, y);
        }
    }

    var minimumCost: usize = 0;
    println("Edges in the constructed MST\n");
    for (result) |edge| {
        minimumCost += edge[2];
        println("{d} -- {d} == {d}\n", .{edge[0], edge[1], edge[2]});
    }
    println("Minimum Spanning Tree {d}\n", .{minimumCost});
}

pub fn main() void {
    var g = Graph.init(4);
    g.addEdge(0, 1, 10);
    g.addEdge(0, 2, 6);
    g.addEdge(0, 3, 5);
    g.addEdge(1, 3, 15);
    g.addEdge(2, 3, 4);

    g.KruskalMST();
}
