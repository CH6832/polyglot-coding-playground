// Bubble Sort
func bubbleSort<T: Comparable>(_ array: inout [T]) {
    guard array.count > 1 else { return }
    
    for i in 0..<array.count {
        for j in 1..<array.count - i {
            if array[j] < array[j - 1] {
                array.swapAt(j, j - 1)
            }
        }
    }
}

// Example Usage
var array = [5, 2, 9, 3, 7]
bubbleSort(&array)
print(array) // Output: [2, 3, 5, 7, 9]
