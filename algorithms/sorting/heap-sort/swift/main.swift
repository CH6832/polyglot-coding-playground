// Heap Sort
func heapSort<T: Comparable>(_ array: inout [T]) {
    func heapify(_ array: inout [T], _ count: Int, _ index: Int) {
        var largest = index
        let left = 2 * index + 1
        let right = 2 * index + 2
        
        if left < count && array[left] > array[largest] {
            largest = left
        }
        
        if right < count && array[right] > array[largest] {
            largest = right
        }
        
        if largest != index {
            array.swapAt(index, largest)
            heapify(&array, count, largest)
        }
    }
    
    for i in (0..<array.count / 2).reversed() {
        heapify(&array, array.count, i)
    }
    
    for i in (1..<array.count).reversed() {
        array.swapAt(0, i)
        heapify(&array, i, 0)
    }
}

// Example Usage
var array = [5, 2, 9, 3, 7]
heapSort(&array)
print(array) // Output: [2, 3, 5, 7, 9]
