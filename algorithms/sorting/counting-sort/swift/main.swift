// Counting Sort
func countingSort(_ array: [Int], maxValue: Int) -> [Int] {
    var counts = Array(repeating: 0, count: maxValue + 1)
    
    for element in array {
        counts[element] += 1
    }
    
    var sortedArray = [Int]()
    
    for (value, count) in counts.enumerated() {
        sortedArray += Array(repeating: value, count: count)
    }
    
    return sortedArray
}

// Example Usage
let array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
let maxValue = array.max() ?? 0
let sortedArray = countingSort(array, maxValue: maxValue)
print(sortedArray) // Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
