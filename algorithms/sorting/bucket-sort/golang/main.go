package main

import (
    "fmt"
    "sort"
)

func bucketSort(arr []float64) []float64 {
    n := len(arr)
    buckets := make([][]float64, n)
    for i := 0; i < n; i++ {
        index := int(arr[i] * float64(n))
        buckets[index] = append(buckets[index], arr[i])
    }
    for i := 0; i < n; i++ {
        sort.Float64s(buckets[i])
    }
    k := 0
    for i := 0; i < n; i++ {
        for j := 0; j < len(buckets[i]); j++ {
            arr[k] = buckets[i][j]
            k++
        }
    }
    return arr
}

func main() {
    arr := []float64{0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68}
    fmt.Println("Original array:", arr)
    sortedArr := bucketSort(arr)
    fmt.Println("Sorted array:", sortedArr)
}
