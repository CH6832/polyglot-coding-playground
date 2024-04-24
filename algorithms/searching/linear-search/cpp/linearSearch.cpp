#include <iostream>
#include <vector>

using namespace std;

int linear_search(vector<int>& arr, int x) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {4, 8, 2, 6, 9, 0, 3};
    int x = 4;

    int result = linear_search(arr, x);

    if (result != -1) {
        cout << "Element " << x << " is present at index " << result << endl;
    } else {
        cout << "Element " << x << " is not present in the array" << endl;
    }

    return 0;
}
