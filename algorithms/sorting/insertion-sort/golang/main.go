package main

import "fmt"

// InsertionSort sorts a list of integers using the Insertion Sort algorithm
func InsertionSort(arr []int) {
	n := len(arr)
	for i := 1; i < n; i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
}

func main() {
	arr := []int{12, 11, 13, 5, 6, 7}
	fmt.Println("Original array:", arr)
	InsertionSort(arr)
	fmt.Println("Sorted array:", arr)
}
