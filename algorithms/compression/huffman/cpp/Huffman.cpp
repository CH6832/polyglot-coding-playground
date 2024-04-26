#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>
#include <limits>
#include "Huffman.h"

using namespace std;
#include "huffman.h"
#include <queue>

// Node class implementation
Node::Node(char data, int freq) : data(data), freq(freq), left(nullptr), right(nullptr) {}

Node::Node(int freq) : data('\0'), freq(freq), left(nullptr), right(nullptr) {}

// Huffman class implementation
string Huffman::compress(const string& text) {
    // Count the frequency of each character in the text
    unordered_map<char, int> freqMap;
    for (char c : text) {
        freqMap[c]++;
    }

    // Build Huffman tree from character frequencies
    Node* root = buildTree(freqMap);

    // Build Huffman codes from the tree
    unordered_map<char, string> codes;
    buildCodes(root, "", codes);

    // Encode the input text using Huffman codes
    string encodedText;
    for (char c : text) {
        encodedText += codes[c];
    }

    // Free memory allocated for the tree nodes
    delete root;

    return encodedText;
}

Node* Huffman::buildTree(const unordered_map<char, int>& freqMap) {
    // Create a priority queue of nodes, ordered by frequency
    priority_queue<Node*, vector<Node*>, CompareNodes> pq;

    // Create leaf nodes for each character and push them into the priority queue
    for (const auto& pair : freqMap) {
        pq.push(new Node(pair.first, pair.second));
    }

    // Construct Huffman tree by merging nodes with lowest frequencies
    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        // Create a new internal node with the sum of frequencies
        Node* parent = new Node(left->freq + right->freq);
        parent->left = left;
        parent->right = right;

        // Push the new internal node back into the priority queue
        pq.push(parent);
    }

    // Return the root of the Huffman tree
    return pq.top();
}

void Huffman::buildCodes(Node* root, const string& prefix, unordered_map<char, string>& codes) {
    if (root->left == nullptr && root->right == nullptr) {
        codes[root->data] = prefix; // Leaf node, store the code for the character
    }
    else {
        buildCodes(root->left, prefix + '0', codes); // Traverse left child with '0' appended to the prefix
        buildCodes(root->right, prefix + '1', codes); // Traverse right child with '1' appended to the prefix
    }
}
