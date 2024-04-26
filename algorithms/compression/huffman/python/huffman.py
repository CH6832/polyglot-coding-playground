#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""huffman.py

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

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Dict, Tuple


def main() -> None:
    """Driving code and main function"""
    text = "hello world"
    encoded_text, codes = compress(text)
    print("Encoded text:", encoded_text)
    print("Codes:", codes)

    decoded_text = decompress(encoded_text, codes)
    print("Decoded text:", decoded_text)


class Node:
    """A node in the Huffman tree."""
    def __init__(self, freq: int, char: str) -> None:
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other: 'Node') -> bool:
        return self.freq < other.freq

def build_tree(text: str) -> Node:
    """Builds a Huffman tree based on the character frequencies in the given text.

    Keyword arguments:
    text (str): The input text.
    """
    freq: Dict[str, int] = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    heap = [Node(f, c) for c, f in freq.items()]

    while len(heap) > 1:
        left = min(heap)
        heap.remove(left)
        right = min(heap)
        heap.remove(right)
        parent = Node(left.freq + right.freq)
        parent.left = left
        parent.right = right
        heap.append(parent)

    return heap[0]

def build_codes(root: Node) -> Dict[str, str]:
    """Builds Huffman codes for each character in the Huffman tree.

    Keyword arguments:
    root (Node): The root node of the Huffman tree.
    """
    codes: Dict[str, str] = {}
    def traverse(node: Node, code: str = '') -> None:
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    traverse(root)
    return codes

def compress(text: str) -> Tuple[str, Dict[str, str]]:
    """Compresses the given text using Huffman coding.

    Keyword arguments:
    text (str): The input text to compress.
    """
    root = build_tree(text)
    codes = build_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def decompress(encoded_text: str, codes: Dict[str, str]) -> str:
    """Decompresses the given encoded text using the provided Huffman codes.

    Keyword arguments:
    encoded_text (str): The encoded text to decompress.
    codes (Dict[str, str]): The Huffman codes used for compression.
    """
    reversed_codes = {v: k for k, v in codes.items()}
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ''
    return decoded_text


if __name__ == '__main__':
    main()

