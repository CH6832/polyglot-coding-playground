#ifndef HUFFMAN_H
#define HUFFMAN_H

#include <string>
#include <unordered_map>

using namespace std;


// Node class represents a node in the Huffman tree
class Node {
public:
    char data;          // Character stored in the node (for leaf nodes)
    int freq;           // Frequency of the character or sum of frequencies for internal nodes
    Node* left;         // Pointer to the left child
    Node* right;        // Pointer to the right child

    // Constructor for leaf nodes
    Node(char data, int freq);

    // Constructor for internal nodes
    Node(int freq);
};

// Huffman class contains functions for Huffman compression and decompression
class Huffman {
public:
    // Compress the input text using Huffman coding
    static string compress(const string& text);

private:
    // Comparison function for priority queue
    struct CompareNodes {
        bool operator()(const Node* lhs, const Node* rhs) const {
            return lhs->freq > rhs->freq;
        }
    };

    // Build Huffman tree from given character frequencies
    static Node* buildTree(const unordered_map<char, int>& freqMap);

    // Recursively build Huffman codes by traversing the Huffman tree
    static void buildCodes(Node* root, const string& prefix, unordered_map<char, string>& codes);
};

#endif // HUFFMAN_H

