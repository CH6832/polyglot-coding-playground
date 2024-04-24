const std = @import("std");

pub fn bubbleSort(arr: []i32) void {
    const n = arr.len;
    for (i := 0; i < n; i += 1) {
        for (j := 0; j < n - i - 1; j += 1) {
            if (arr[j] > arr[j + 1]) {
                const temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                // Visualization (pause for a short duration)
                std.os.sleep(std.time.Milliseconds(100));
                // Output the current state of the array
                for (arr) |elem| {
                    std.debug.print("{} ", .{ elem });
                }
                std.debug.print("\n", .{});
            }
        }
    }
}

pub fn main() !void {
    var arr: [7]i32 = [64, 34, 25, 12, 22, 11, 90];

    std.debug.print("Unsorted array: ", .{});
    for (arr) |elem| {
        std.debug.print("{} ", .{ elem });
    }
    std.debug.print("\n", .{});

    bubbleSort(arr);

    std.debug.print("Sorted array: ", .{});
    for (arr) |elem| {
        std.debug.print("{} ", .{ elem });
    }
    std.debug.print("\n", .{});
}
