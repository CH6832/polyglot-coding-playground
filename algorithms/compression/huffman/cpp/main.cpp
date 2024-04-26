/*
Description:
------------
Building the Huffman Tree: The program first builds a Huffman tree based on the frequencies of characters
in the input text. It creates a node for each unique character, where the frequency of the character
determines the weight of the node. It then combines nodes with the lowest frequencies into parent nodes
until a single root node remains.
Generating Huffman Codes: After building the Huffman tree, the program generates Huffman codes for each
character in the tree. The codes are determined by traversing the tree, assigning '0' to left branches
and '1' to right branches.
Compression: Using the generated Huffman codes, the program compresses the original text by replacing
each character with its corresponding Huffman code.
Decompression: The program can also decompress the encoded text back to the original text using the
provided Huffman codes. It iterates over the encoded text, building the original text by matching
sequences of bits with their corresponding characters in the Huffman codes.

Compile the program:
--------------------
Step 2: Compile each source file
    g++ -c main.cpp -o main.o
    g++ -c TSMSolver.cpp -o TSMSolver.o
Step 2: Link all object files together to create an executable
    g++ main.o TSMSolver.o -o main
*/

#include <iostream>
#include "huffman.h"

using namespace std;


int main() {
    string text = "hello world";

    // Compress the input text using Huffman coding
    string encodedText = Huffman::compress(text);

    // Print the compressed text
    cout << "Encoded text: " << encodedText << endl;

    return 0;
}
