// Quick Sort
func quickSort<T: Comparable>(_ array: inout [T], low: Int, high: Int) {
    if low < high {
        let pivotIndex = partition(&array, low: low, high: high)
        quickSort(&array, low: low, high: pivotIndex - 1)
        quickSort(&array, low: pivotIndex + 1, high: high)
    }
}

func partition<T: Comparable>(_ array: inout [T], low: Int, high: Int) -> Int {
    let pivot = array[high]
    var i = low
    
    for j in low..<high {
        if array[j] <= pivot {
            array.swapAt(i, j)
            i += 1
        }
    }
    
    array.swapAt(i, high)
    return i
}

// Example Usage
var array = [5, 2, 9, 3, 7]
quickSort(&array, low: 0, high: array.count - 1)
print(array) // Output: [2, 3, 5, 7, 9]
