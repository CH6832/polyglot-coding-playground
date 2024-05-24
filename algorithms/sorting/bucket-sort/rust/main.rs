// Bucket Sort
fn bucket_sort(array: &[u32]) -> Vec<u32> {
    let max = *array.iter().max().unwrap_or(&0);
    let mut buckets = vec![0; (max + 1) as usize];
    for &num in array {
        buckets[num as usize] += 1;
    }
    let mut sorted_array = Vec::new();
    for (i, &count) in buckets.iter().enumerate() {
        for _ in 0..count {
            sorted_array.push(i as u32);
        }
    }
    sorted_array
}

// Example Usage
fn main() {
    let array = [5, 2, 9, 3, 7];
    let sorted_array = bucket_sort(&array);
    println!("{:?}", sorted_array); // Output: [2, 3, 5, 7, 9]
}
