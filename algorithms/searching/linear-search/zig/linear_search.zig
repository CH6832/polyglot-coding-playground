const std = @import("std");

fn linearSearch(arr: []i32, x: i32) !usize {
    var i: usize = 0;
    while (i < arr.len) {
        if (arr[i] == x) {
            return i;
        }
        i += 1;
    }
    return error.NotFound;
}

pub fn main() !void {
    var arr: [7]i32 = [64, 34, 25, 12, 22, 11, 90];
    const target: i32 = 22;

    const index = try linearSearch(arr, target);
    if (index == error.NotFound) {
        std.debug.print("Element ", .{ target });
        std.debug.print(" not found in the array.\n", .{});
    } else {
        std.debug.print("Element ", .{ target });
        std.debug.print(" found at index ", .{ index });
        std.debug.print(".\n", .{});
    }
}
