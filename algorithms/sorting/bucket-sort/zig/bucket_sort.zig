const bucketSort = fn (x: []f64) []f64 {
    // Insertion sort for sorting individual buckets
    const insertionSort = fn (b: []f64) []f64 {
        var up: f64 = undefined;
        var j: i32 = undefined;
        for (b) |i| {
            up = b[i];
            j = i - 1;
            while (j >= 0 and b[j] > up) : (void) {
                b[j + 1] = b[j];
                j -= 1;
            }
            b[j + 1] = up;
        }
        return b;
    }

    var arr: [10][]f64 = undefined;
    const slot_num: i32 = 10;
    for (arr) |_, i| {
        arr[i] = []f64{};
    }

    // Put array elements in different buckets
    for (x) |j| {
        const index_b: i32 = @intCast(i32, slot_num * j);
        arr[index_b].append(j);
    }

    // Sort individual buckets
    for (arr) |bucket, _| {
        insertionSort(bucket);
    }

    // Concatenate the result
    var k: i32 = 0;
    for (arr) |bucket| {
        for (bucket) |_, elem| {
            x[k] = elem;
            k += 1;
        }
    }
    return x;
};
