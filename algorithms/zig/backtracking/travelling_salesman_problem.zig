const std = @import("std");

var maxInt = i32.max;

fn factorial(n: i32) i32 {
    var result: i32 = 1;
    for (1..(n + 1)) |i| {
        result *= i;
    }
    return result;
}

fn travellingSalesmanProblem(graph: [][]i32, s: i32) i32 {
    const V = graph.len;
    var vertex = []i32{};

    for (graph) |row, i| {
        if (i != s) {
            vertex |= i;
        }
    }

    var minPath: i32 = maxInt;
    var permutations = std.math.factorial(vertex.len);

    for (0..permutations) |permutation| {
        var currentPathWeight: i32 = 0;
        var k: i32 = s;

        for (vertex) |j| {
            currentPathWeight += graph[k][j];
            k = j;
        }
        currentPathWeight += graph[k][s];

        minPath = @intCast(i32, @min(@intCast(u32, minPath), @intCast(u32, currentPathWeight)));
    }

    return minPath;
}

pub fn main() void {
    const V = 4;
    var graph = [][]i32{
        []i32{0, 10, 15, 20},
        []i32{10, 0, 35, 25},
        []i32{15, 35, 0, 30},
        []i32{20, 25, 30, 0},
    };

    const s = 0;
    const minPath = travellingSalesmanProblem(graph, s);

    if (minPath == maxInt) {
        std.debug.print("-1\n", .{});
    } else {
        std.debug.print("Minimum cost of TSP: {}\n", .{minPath});
    }
}
