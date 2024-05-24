// Heap Sort
fn heap_sort<T: Ord>(array: &mut [T]) {
    for i in (0..array.len() / 2).rev() {
        heapify(array, i, array.len());
    }
    for i in (1..array.len()).rev() {
        array.swap(0, i);
        heapify(array, 0, i);
    }
}

fn heapify<T: Ord>(array: &mut [T], mut root: usize, size: usize) {
    loop {
        let mut max = root;
        let left = 2 * root + 1;
        let right = 2 * root + 2;

        if left < size && array[left] > array[max] {
            max = left;
        }

        if right < size && array[right] > array[max] {
            max = right;
        }

        if max != root {
            array.swap(root, max);
            root = max;
        } else {
            break;
        }
    }
}

// Example Usage
fn main() {
    let mut array = vec![5, 2, 9, 3, 7];
    heap_sort(&mut array);
    println!("{:?}", array); // Output: [2, 3, 5, 7, 9]
}
