// Merge Sort
func mergeSort<T: Comparable>(_ array: [T]) -> [T] {
    guard array.count > 1 else { return array }
    
    let middleIndex = array.count / 2
    let leftArray = mergeSort(Array(array[0..<middleIndex]))
    let rightArray = mergeSort(Array(array[middleIndex..<array.count]))
    
    return merge(leftArray, rightArray)
}

func merge<T: Comparable>(_ leftArray: [T], _ rightArray: [T]) -> [T] {
    var leftIndex = 0
    var rightIndex = 0
    var orderedArray: [T] = []
    
    while leftIndex < leftArray.count && rightIndex < rightArray.count {
        if leftArray[leftIndex] < rightArray[rightIndex] {
            orderedArray.append(leftArray[leftIndex])
            leftIndex += 1
        } else {
            orderedArray.append(rightArray[rightIndex])
            rightIndex += 1
        }
    }
    
    orderedArray += Array(leftArray[leftIndex..<leftArray.count])
    orderedArray += Array(rightArray[rightIndex..<rightArray.count])
    
    return orderedArray
}

// Example Usage
let array = [5, 2, 9, 3, 7]
let sortedArray = mergeSort(array)
print(sortedArray) // Output: [2, 3, 5, 7, 9]
