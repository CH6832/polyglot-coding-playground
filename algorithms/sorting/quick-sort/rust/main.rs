// Quick Sort
fn quick_sort<T: Ord>(array: &mut [T]) {
    let len = array.len();
    if len <= 1 {
        return;
    }
    let pivot_index = partition(array);
    quick_sort(&mut array[..pivot_index]);
    quick_sort(&mut array[pivot_index + 1..]);
}

fn partition<T: Ord>(array: &mut [T]) -> usize {
    let len = array.len();
    let pivot_index = len / 2;
    array.swap(pivot_index, len - 1);
    let mut i = 0;
    for j in 0..len - 1 {
        if array[j] <= array[len - 1] {
            array.swap(i, j);
            i += 1;
        }
    }
    array.swap(i, len - 1);
    i
}

// Example Usage
fn main() {
    let mut array = vec![5, 2, 9, 3, 7];
    quick_sort(&mut array);
    println!("{:?}", array); // Output: [2, 3, 5, 7, 9]
}
