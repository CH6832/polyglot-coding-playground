const countingSort = fn (arr: []const u8) []u8 {
    // The output array that will have sorted arr
    var output: [len(arr)]u8 = undefined;

    // Create a count array to store count of individual
    // characters and initialize count array as 0
    var count: [256]u32 = undefined;

    // For storing the resulting answer since the
    // string is immutable
    var ans: [len(arr)]u8 = undefined;

    // Store count of each character
    for (arr) |i| {
        count[i] += 1;
    }

    // Change count[i] so that count[i] now contains actual
    // position of this character in output array
    for (count[1..]) |count, index| {
        count += count[index - 1];
    }

    // Build the output array
    for (arr) |elem| {
        const index: usize = @intCast(usize, count[elem] - 1);
        output[index] = elem;
        count[elem] -= 1;
    }

    // Copy the output array to arr, so that arr now
    // contains sorted characters
    for (output) |elem, index| {
        ans[index] = elem;
    }
    return ans;
};
