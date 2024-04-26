#include "ZAlgo.h"

std::vector<int> z_algorithm(const std::string& text) {
    int n = text.length();
    std::vector<int> z(n, 0);
    int left = 0, right = 0;

    for (int i = 1; i < n; ++i) {
        if (i <= right) {
            z[i] = std::min(right - i + 1, z[i - left]);
        }
        while (i + z[i] < n && text[z[i]] == text[i + z[i]]) {
            z[i]++;
        }
        if (i + z[i] - 1 > right) {
            left = i;
            right = i + z[i] - 1;
        }
    }

    // Find all occurrences of the pattern
    int pattern_length = text.length();
    std::vector<int> occurrences;
    for (int i = 0; i < pattern_length; ++i) {
        if (z[i] == pattern_length - i) {
            occurrences.push_back(i);
        }
    }

    return occurrences;
}
