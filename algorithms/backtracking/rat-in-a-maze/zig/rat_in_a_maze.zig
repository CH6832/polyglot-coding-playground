const std = @import("std");
const mem = std.mem;

// Arrays to represent change in rows and columns
const DR: [4]i32 = [1, 0, 0, -1];
const DC: [4]i32 = [0, -1, 1, 0];
const Direction = "DLRU";

// Function to check if cell(row, col) is inside the maze and unblocked
fn isValid(row: i32, col: i32, n: i32, maze: [][]i32) bool {
    return (0 <= row) and (row < n) and (0 <= col) and (col < n) and (maze[row][col] == 1);
}

fn findPath(row: i32, col: i32, maze: [][]i32, n: i32, ans: [][]u8, currentPath: []const u8) void {
    // If we reach the bottom right cell of the matrix, add
    // the current path to ans and return
    if (row == n - 1) and (col == n - 1) {
        _ = ans.append(currentPath);
        return;
    }

    // Mark the current cell as blocked
    maze[row][col] = 0;

    // Temporary array to hold the next path
    var nextPath: [100]u8 = undefined;
    var nextPathLen: usize = 0;

    for (DR) |dr, i| {
        // Find the next row based on the current row (row)
        // and the dr[] array
        const nextRow = row + dr;

        // Find the next column based on the current column
        // (col) and the dc[] array
        const nextCol = col + DC[i];

        // Check if the next cell is valid or not
        if isValid(nextRow, nextCol, n, maze) {
            mem.copy(
                &nextPath[nextPathLen],
                Direction[i],
                Direction[i].len,
            );
            nextPathLen += Direction[i].len;

            // Recursively call the findPath function for
            // the next cell
            findPath(nextRow, nextCol, maze, n, ans, nextPath);
            nextPathLen -= Direction[i].len;
        }
    }

    // Mark the current cell as unblocked
    maze[row][col] = 1;
}

pub fn main() !void {
    // Driver code
    var maze: [][]i32 = [][]i32{
        []i32{1, 0, 0, 0},
        []i32{1, 1, 0, 1},
        []i32{1, 1, 0, 0},
        []i32{0, 1, 1, 1}
    };

    const n = maze.len;
    var result: [][]u8 = undefined;
    var currentPath: [100]u8 = undefined;

    if (maze[0][0] != 0) and (maze[n - 1][n - 1] != 0) {
        // Function call to get all valid paths
        findPath(0, 0, maze, n, result, currentPath);
    }

    if (result.len == 0) {
        std.debug.print("-1\n", .{});
    } else {
        for (result) |path| {
            const pathSlice = path[0..];
            std.debug.print("{} ", .{pathSlice});
        }
    }
}
