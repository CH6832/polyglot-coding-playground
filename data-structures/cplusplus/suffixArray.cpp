#include <iostream>
#include <vector>
#include <algorithm>

// Define a suffix structure to hold index and suffix string
struct Suffix {
    int index;
    std::string suffix;
};

// Comparator function to compare two suffixes
bool suffixComparator(const Suffix& a, const Suffix& b) {
    return a.suffix < b.suffix;
}

// Function to construct the suffix array
std::vector<int> constructSuffixArray(const std::string& text) {
    int n = text.length();

    // Create an array of suffixes
    std::vector<Suffix> suffixes(n);
    for (int i = 0; i < n; ++i) {
        suffixes[i].index = i;
        suffixes[i].suffix = text.substr(i);
    }

    // Sort the suffixes using the comparator function
    std::sort(suffixes.begin(), suffixes.end(), suffixComparator);

    // Construct the suffix array
    std::vector<int> suffixArray(n);
    for (int i = 0; i < n; ++i) {
        suffixArray[i] = suffixes[i].index;
    }

    return suffixArray;
}

int main() {
    std::string text = "banana";

    // Construct the suffix array
    std::vector<int> suffixArray = constructSuffixArray(text);

    // Print the suffix array
    std::cout << "Suffix Array: ";
    for (int i : suffixArray) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
