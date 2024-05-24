package main

import "fmt"

func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr) / 2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    merged := make([]int, 0, len(left)+len(right))
    for len(left) > 0 || len(right) > 0 {
        if len(left) == 0 {
            return append(merged, right...)
        }
        if len(right) == 0 {
            return append(merged, left...)
        }
        if left[0] <= right[0] {
            merged = append(merged, left[0])
            left = left[1:]
        } else {
            merged = append(merged, right[0])
            right = right[1:]
        }
    }
    return merged
}

func main() {
    arr := []int{38, 27, 43, 3, 9, 82, 10}
    fmt.Println("Original array:", arr)
    sortedArr := mergeSort(arr)
    fmt.Println("Sorted array:", sortedArr)
}
