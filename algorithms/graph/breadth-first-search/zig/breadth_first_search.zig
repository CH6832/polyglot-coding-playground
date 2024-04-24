const std = @import("std");
const print = std.io.getStdOut().writeAll;

pub const Graph = struct {
    const Node = struct {
        u: usize,
        v: usize,
    };

    nodes: []Node,

    pub fn addEdge(self: *Graph, u: usize, v: usize) void {
        const newNode = Graph.Node{ .u = u, .v = v };
        self.nodes.append(newNode);
    }

    pub fn BFS(self: *Graph, s: usize) void {
        var visited = []bool{false} ** self.nodes.len;

        var queue = []usize{};
        queue.append(s);
        visited[s] = true;

        while (queue.len != 0) : (queue = queue[1..]) {
            const current = queue[0];
            const buffer: [20]u8 = undefined;
            var index: usize = 0;
            index += std.mem.formatInt(buffer[index..], current, .{});
            index += std.mem.copy(buffer[index..], " ", 1);
            _ = print(buffer[0..index]);

            for (self.nodes) |node| {
                if (node.u == current) | (node.v == current) {
                    const neighbor = (node.u == current) ? node.v : node.u;
                    if (!visited[neighbor]) {
                        queue.append(neighbor);
                        visited[neighbor] = true;
                    }
                }
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

    const buffer: [100]u8 = undefined;
    var index: usize = 0;
    index += std.mem.copy(buffer[index..], "Following is Breadth First Traversal (starting from vertex 2)\n", 65);
    _ = print(buffer[0..index]);

    g.BFS(2);
}
