const std = @import("std");

fn binarySearch(arr: []i32, x: i32) !usize {
    var low: usize = 0;
    var high: usize = arr.len - 1;

    while (low <= high) {
        const mid = (low + high) / 2;

        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return error.NotFound;
}

pub fn main() !void {
    var arr: [10]i32 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
    const target: i32 = 15;

    const index = try binarySearch(arr, target);
    if (index == error.NotFound) {
        std.debug.print("Element ", .{ target });
        std.debug.print(" not found in the array.\n", .{});
    } else {
        std.debug.print("Element ", .{ target });
        std.debug.print(" found at index ", .{ index });
        std.debug.print(".\n", .{});
    }
}
