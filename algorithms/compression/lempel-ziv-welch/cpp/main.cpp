/*
Description:
------------
This program solves the Travelling Salesman Problem (TSP) using brute-force permutation.
Given a weighted graph represented as an adjacency matrix, it finds the minimum Hamiltonian cycle,
i.e., a cycle that visits each vertex exactly once and returns to the starting vertex, with the
minimum total weight.

Compile the program:
--------------------
Step 2: Compile each source file
    g++ -c main.cpp -o main.o
    g++ -c LZW.cpp -o LZW.o
Step 2: Link all object files together to create an executable
    g++ main.o LZW.o -o main
*/

#include <iostream>
#include "LZW.h"


using namespace std;

int main() {
    // Example usage
    string input = "ABABABA";
    vector<int> compressedData = compress(input);
    cout << "Compressed: ";
    for (int code : compressedData) {
        cout << code << " ";
    }
    cout << endl;

    string decompressedData = decompress(compressedData);
    cout << "Decompressed: " << decompressedData << std::endl;

    return 0;
}