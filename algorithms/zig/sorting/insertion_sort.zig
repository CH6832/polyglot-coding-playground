const insertionSort = fn (listToSort: []anytype) void {
    const n: usize = listToSort.len;

    // Iterate over array to be sorted
    for (1 .. n) |i| {
        var x = listToSort[i]; // Get each element
        var j = i - 1; // Get one position before x
        // Shift until reaching index 0 or getting an element smaller than x
        while (j >= 0) and (x < listToSort[j]) : (void) {
            // Swap here
            listToSort[j + 1] = listToSort[j];
            j -= 1;
        }
        // Keep as it is
        listToSort[j + 1] = x;
    }
};
