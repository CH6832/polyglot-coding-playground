const std = @import("std");
const println = std.debug.print;

const inf: i32 = 1_000_000;

pub fn minDistance(dist: []i32, sptSet: []bool, V: usize) usize {
    var minIndex: usize = 0;
    var min: i32 = inf;

    for (V) |v| {
        if dist[v] < min && !sptSet[v] {
            min = dist[v];
            minIndex = v;
        }
    }

    return minIndex;
}

pub fn dijkstra(graph: [][]i32, src: usize) void {
    const V: usize = graph.len;
    var dist = [_]i32{0} ** V;
    var sptSet = [_]bool{false} ** V;

    for (V) |v| {
        dist[v] = inf;
    }

    dist[src] = 0;

    for (V) |count| {
        const u = minDistance(dist, sptSet, V);
        sptSet[u] = true;

        for (V) |v| {
            if graph[u][v] != 0 && !sptSet[v] && dist[u] + graph[u][v] < dist[v] {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    println("Vertex \t Distance from Source\n");
    for (V) |node| {
        println("{d} \t\t {d}\n", .{node, dist[node]});
    }
}

pub fn main() void {
    var graph = [][]i32{
        [_]i32{0, 4, 0, 0, 0, 0, 0, 8, 0},
        [_]i32{4, 0, 8, 0, 0, 0, 0, 11, 0},
        [_]i32{0, 8, 0, 7, 0, 4, 0, 0, 2},
        [_]i32{0, 0, 7, 0, 9, 14, 0, 0, 0},
        [_]i32{0, 0, 0, 9, 0, 10, 0, 0, 0},
        [_]i32{0, 0, 4, 14, 10, 0, 2, 0, 0},
        [_]i32{0, 0, 0, 0, 0, 2, 0, 1, 6},
        [_]i32{8, 11, 0, 0, 0, 0, 1, 0, 7},
        [_]i32{0, 0, 2, 0, 0, 0, 6, 7, 0}
    };

    dijkstra(graph, 0);
}
