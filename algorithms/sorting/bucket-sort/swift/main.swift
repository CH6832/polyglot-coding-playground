// Bucket Sort
func bucketSort<T: Comparable>(_ array: [T]) -> [T] {
    guard let maxElement = array.max() else { return [] }
    var buckets = Array(repeating: [T](), count: Int(maxElement) + 1)
    
    for element in array {
        buckets[Int(element)].append(element)
    }
    
    var sortedArray = [T]()
    for bucket in buckets {
        sortedArray += bucket
    }
    
    return sortedArray
}

// Example Usage
let array = [5, 2, 9, 3, 7]
let sortedArray = bucketSort(array)
print(sortedArray) // Output: [2, 3, 5, 7, 9]
