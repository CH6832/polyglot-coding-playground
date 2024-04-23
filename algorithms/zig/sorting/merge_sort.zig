const mergeSort = fn (inputList: []anytype) void {
    // Check if list exists
    if (inputList.len > 1) {
        // Finding mid of list
        const mid: usize = inputList.len / 2;
        // Dividing the list elements into two halves
        const leftPart = inputList[0..mid];
        const rightPart = inputList[mid..];

        // Sorting both halves
        mergeSort(leftPart);
        mergeSort(rightPart);

        var i: usize = 0;
        var j: usize = 0;
        var k: usize = 0;

        // Copy data to temp lists
        while (i < leftPart.len) and (j < rightPart.len) : (void) {
            if (leftPart[i] <= rightPart[j]) {
                inputList[k] = leftPart[i];
                i += 1;
            } else {
                inputList[k] = rightPart[j];
                j += 1;
            }
            k += 1;
        }

        // Check if elements were left
        while (i < leftPart.len) : (void) {
            inputList[k] = leftPart[i];
            i += 1;
            k += 1;
        }

        while (j < rightPart.len) : (void) {
            inputList[k] = rightPart[j];
            j += 1;
            k += 1;
        }
    }
};
