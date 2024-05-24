// Merge Sort
fn merge_sort<T: Ord>(array: Vec<T>) -> Vec<T> {
    let len = array.len();
    if len <= 1 {
        return array;
    }
    let mid = len / 2;
    let left = merge_sort(array[..mid].to_vec());
    let right = merge_sort(array[mid..].to_vec());
    merge(left, right)
}

fn merge<T: Ord>(mut left: Vec<T>, mut right: Vec<T>) -> Vec<T> {
    let mut sorted_array = Vec::with_capacity(left.len() + right.len());
    while !left.is_empty() && !right.is_empty() {
        if left[0] <= right[0] {
            sorted_array.push(left.remove(0));
        } else {
            sorted_array.push(right.remove(0));
        }
    }
    sorted_array.extend_from_slice(&left);
    sorted_array.extend_from_slice(&right);
    sorted_array
}

// Example Usage
fn main() {
    let array = vec![5, 2, 9, 3, 7];
    let sorted_array = merge_sort(array);
    println!("{:?}", sorted_array); // Output: [2, 3, 5, 7, 9]
}
