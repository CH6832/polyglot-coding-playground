const quickSort = fn (unsortedList: []anytype) []anytype {
    const elements: usize = unsortedList.len;

    // Base case
    if (elements < 2) {
        return unsortedList;
    }

    var currentPosition: usize = 0; // Position of the partitioning element

    // Partitioning loop
    for (1 .. elements) |i| {
        if (unsortedList[i] <= unsortedList[0]) {
            currentPosition += 1;
            const temp = unsortedList[i];
            unsortedList[i] = unsortedList[currentPosition];
            unsortedList[currentPosition] = temp;
        }
    }

    const temp = unsortedList[0];
    unsortedList[0] = unsortedList[currentPosition];
    unsortedList[currentPosition] = temp; // Brings pivot to its appropriate position

    const left = quickSort(unsortedList[0..currentPosition]); // Sorts the elements to the left of pivot
    const right = quickSort(unsortedList[currentPosition+1..elements]); // Sorts the elements to the right of pivot

    return left ++ @[unsortedList[currentPosition]] ++ right; // Merging everything together
};
