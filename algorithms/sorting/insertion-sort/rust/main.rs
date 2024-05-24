// Insertion Sort
fn insertion_sort<T: Ord>(array: &mut [T]) {
    let len = array.len();
    for i in 1..len {
        let mut j = i;
        while j > 0 && array[j - 1] > array[j] {
            array.swap(j - 1, j);
            j -= 1;
        }
    }
}

// Example Usage
fn main() {
    let mut array = vec![5, 2, 9, 3, 7];
    insertion_sort(&mut array);
    println!("{:?}", array); // Output: [2, 3, 5, 7, 9]
}
