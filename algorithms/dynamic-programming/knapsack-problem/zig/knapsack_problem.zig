const std = @import("std");
const debug = std.debug;
const mem = std.mem;

pub fn knapSack(W: i32, wt: []i32, val: []i32, n: i32) i32 {
    // Base Case
    if (n == 0) or (W == 0) {
        return 0;
    }

    // If weight of the nth item is
    // more than Knapsack of capacity W,
    // then this item cannot be included
    // in the optimal solution
    if wt[n - 1] > W {
        return knapSack(W, wt, val, n - 1);
    }

    // return the maximum of two cases:
    // (1) nth item included
    // (2) not included
    else {
        const include = val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1);
        const exclude = knapSack(W, wt, val, n - 1);
        return std.math.max(include, exclude);
    }
}

pub fn main() void {
    // Example usage
    const wt = [_]i32{4, 5, 1};
    const val = [_]i32{1, 2, 3};
    const W: i32 = 4;
    const n: i32 = @intCast(i32, wt.len);
    const result = knapSack(W, wt, val, n);
    debug.print("Maximum possible profit: {}\n", .{result});
}
