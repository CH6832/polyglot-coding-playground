const heapSort = fn (arr: []anytype) void {
    const n: usize = arr.len;
    
    // Inner function to heapify a subtree rooted at index i
    const heapify = fn (arr: []anytype, n: usize, i: usize) void {
        var largest: usize = i; // Initialize largest as root
        const l: usize = 2 * i + 1; // left = 2*i + 1
        const r: usize = 2 * i + 2; // right = 2*i + 2

        // See if left child of root exists and is greater than root
        if (l < n) and (arr[i] < arr[l]) {
            largest = l;
        }

        // See if right child of root exists and is greater than root
        if (r < n) and (arr[largest] < arr[r]) {
            largest = r;
        }

        // Change root, if needed
        if (largest != i) {
            const tmp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = tmp; // swap
            // Heapify the root.
            heapify(arr, n, largest);
        }
    };

    // Build a maxheap. Since the last parent will be at ((n//2)-1) we can start at that location.
    for (n / 2 - 1).stepTo(0, -1) |i| {
        heapify(arr, n, i);
    }

    // One by one extract elements
    for (n - 1).stepTo(0, -1) |i| {
        const tmp = arr[0];
        arr[0] = arr[i];
        arr[i] = tmp; // swap
        heapify(arr, i, 0);
    }
};
