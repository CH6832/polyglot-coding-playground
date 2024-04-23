#include <iostream>
#include <vector>

int main() {
    // Declare an empty vector of integers
    std::vector<int> dynamicArray;

    // Add elements to the dynamic array
    dynamicArray.push_back(10);
    dynamicArray.push_back(20);
    dynamicArray.push_back(30);

    // Access elements using array syntax
    std::cout << "First element: " << dynamicArray[0] << std::endl;

    // Access elements using iterator
    std::cout << "All elements:";
    for (auto it = dynamicArray.begin(); it != dynamicArray.end(); ++it) {
        std::cout << " " << *it;
    }
    std::cout << std::endl;

    // Modify elements
    dynamicArray[1] = 25;

    // Remove the last element
    dynamicArray.pop_back();

    // Size and capacity of the dynamic array
    std::cout << "Size: " << dynamicArray.size() << std::endl;
    std::cout << "Capacity: " << dynamicArray.capacity() << std::endl;

    return 0;
}
