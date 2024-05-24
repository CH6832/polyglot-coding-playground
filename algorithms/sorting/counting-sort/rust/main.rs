// Counting Sort
fn counting_sort(array: &[u32], max_value: usize) -> Vec<u32> {
    let mut counts = vec![0; max_value + 1];
    for &num in array {
        counts[num as usize] += 1;
    }
    let mut sorted_array = Vec::new();
    for (i, &count) in counts.iter().enumerate() {
        for _ in 0..count {
            sorted_array.push(i as u32);
        }
    }
    sorted_array
}

// Example Usage
fn main() {
    let array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
    let max_value = array.iter().max().cloned().unwrap_or(0) as usize;
    let sorted_array = counting_sort(&array, max_value);
    println!("{:?}", sorted_array); // Output: [1, 1, 2,
