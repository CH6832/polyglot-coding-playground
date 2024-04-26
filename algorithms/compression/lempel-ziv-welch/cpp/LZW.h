#ifndef LZW_ALGORITHM_H
#define LZW_ALGORITHM_H

#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

// Function to compress data using LZW algorithm
std::vector<int> compress(const std::string& data);

// Function to decompress data using LZW algorithm
std::string decompress(const std::vector<int>& compressedData);

#endif // LZW_ALGORITHM_H
