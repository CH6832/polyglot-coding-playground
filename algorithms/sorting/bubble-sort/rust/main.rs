// Bubble Sort
fn bubble_sort<T: Ord>(array: &mut [T]) {
    let len = array.len();
    for i in 0..len {
        for j in 1..(len - i) {
            if array[j - 1] > array[j] {
                array.swap(j - 1, j);
            }
        }
    }
}

// Example Usage
fn main() {
    let mut array = [5, 2, 9, 3, 7];
    bubble_sort(&mut array);
    println!("{:?}", array); // Output: [2, 3, 5, 7, 9]
}
