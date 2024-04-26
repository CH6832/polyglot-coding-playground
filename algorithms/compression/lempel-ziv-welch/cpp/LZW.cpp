#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <limits>
#include "LZW.h"
#include <unordered_map>

std::vector<int> compress(const std::string& data) {
    std::unordered_map<std::string, int> dictionary;
    std::vector<int> result;

    // Initialize dictionary with ASCII characters
    for (int i = 0; i < 256; ++i) {
        dictionary[std::string(1, char(i))] = i;
    }

    std::string currentString;
    for (char c : data) {
        std::string newString = currentString + c;
        if (dictionary.find(newString) != dictionary.end()) {
            currentString = newString;
        }
        else {
            // Output code for the current string
            result.push_back(dictionary[currentString]);
            // Add new string to dictionary
            dictionary[newString] = dictionary.size();
            currentString = std::string(1, c);
        }
    }

    // Output code for the last string
    result.push_back(dictionary[currentString]);

    return result;
}

std::string decompress(const std::vector<int>& compressedData) {
    std::unordered_map<int, std::string> dictionary;
    std::string result;

    // Initialize dictionary with ASCII characters
    for (int i = 0; i < 256; ++i) {
        dictionary[i] = std::string(1, char(i));
    }

    int nextCode = 256;
    std::string currentString = std::string(1, char(compressedData[0]));
    result += currentString;

    for (size_t i = 1; i < compressedData.size(); ++i) {
        int code = compressedData[i];
        std::string newString;
        if (dictionary.find(code) != dictionary.end()) {
            newString = dictionary[code];
        }
        else {
            newString = currentString + currentString[0];
        }
        result += newString;
        // Add entry to dictionary
        dictionary[nextCode++] = currentString + newString[0];
        currentString = newString;
    }

    return result;
}
