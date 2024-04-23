#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <thread>

using namespace std;

void bubble_sort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                // Visualization (pause for a short duration)
                this_thread::sleep_for(chrono::milliseconds(100));
                // Output the current state of the array
                for (int k = 0; k < n; ++k) {
                    cout << arr[k] << " ";
                }
                cout << endl;
            }
        }
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    int n = arr.size();

    cout << "Unsorted array: ";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    bubble_sort(arr);

    cout << "Sorted array: ";
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
