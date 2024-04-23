#include <iostream>
#include <vector>

using namespace std;

int binary_search(vector<int>& arr, int low, int high, int x) {
    // Check base case
    if (high >= low) {
        int mid = (high + low) / 2;

        // If element is present at the middle itself
        if (arr[mid] == x)
            return mid;

        // If element is smaller than mid, then it can only
        // be present in left subarray
        else if (arr[mid] > x)
            return binary_search(arr, low, mid - 1, x);

        // Else the element can only be present in right subarray
        else
            return binary_search(arr, mid + 1, high, x);
    }

    // Element is not present in the array
    return -1;
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40};
    int x = 10;

    // First call to binary_search
    binary_search({0,1,2,3,4,5,6,7,8,9,8,9,9}, 2, 7, 4);

    // Second call to binary_search
    int result = binary_search(arr, 0, arr.size() - 1, x);

    if (result != -1)
        cout << "Element " << x << " is present at index " << result << endl;
    else
        cout << "Element " << x << " is not present in the array" << endl;

    return 0;
}
