// Insertion Sort
func insertionSort<T: Comparable>(_ array: inout [T]) {
    guard array.count > 1 else { return }
    
    for i in 1..<array.count {
        var currentIndex = i
        while currentIndex > 0 && array[currentIndex] < array[currentIndex - 1] {
            array.swapAt(currentIndex, currentIndex - 1)
            currentIndex -= 1
        }
    }
}

// Example Usage
var array = [5, 2, 9, 3, 7]
insertionSort(&array)
print(array) // Output: [2, 3, 5, 7, 9]
