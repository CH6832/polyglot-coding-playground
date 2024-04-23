const std = @import("std");
const print = std.io.getStdOut().writeAll;

pub const Graph = struct {
    const Node = struct {
        u: usize,
        v: usize,
    };

    nodes: []Node,
    visited: []bool,

    pub fn addEdge(self: *Graph, u: usize, v: usize) void {
        const newNode = Graph.Node{ .u = u, .v = v };
        self.nodes.append(newNode);
    }

    pub fn DFSUtil(self: *Graph, v: usize) void {
        self.visited[v] = true;
        const buffer: [20]u8 = undefined;
        var index: usize = 0;
        index += std.mem.formatInt(buffer[index..], v, .{});
        index += std.mem.copy(buffer[index..], " ", 1);
        _ = print(buffer[0..index]);

        for (self.nodes) |node| {
            if (node.u == v) | (node.v == v) {
                const neighbor = (node.u == v) ? node.v : node.u;
                if (!self.visited[neighbor]) {
                    self.DFSUtil(neighbor);
                }
            }
        }
    }

    pub fn DFS(self: *Graph) void {
        const V = self.nodes.len;
        self.visited = std.heap.Allocator([]bool).alloc(V);

        for (V) |i| {
            self.visited[i] = false;
        }

        for (V) |i| {
            if (!self.visited[i]) {
                self.DFSUtil(i);
            }
        }
    }
};

pub fn main() void {
    const g = Graph{ .nodes = []Graph.Node{} };
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    const buffer: [50]u8 = undefined;
    var index: usize = 0;
    index += std.mem.copy(buffer[index..], "Following is Depth First Traversal\n", 33);
    _ = print(buffer[0..index]);

    g.DFS();
}
