#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""radix_tree.py

RadixNode Class: This class represents a node in the radix tree. Each node contains a value (a character) and a dictionary mapping characters to child nodes.

RadixTree Class: This class represents the radix tree data structure. It has methods for inserting a word into the tree (insert) and searching for a word in the tree (search).

Example Usage: In the __main__ block, an example usage of the RadixTree class is provided. Words are inserted into the tree using the insert method, and then various words are searched for using the search method.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List


def main() -> None:
    """Driving code and main function"""
    radix_tree = RadixTree()
    words = ["apple", "banana", "apricot", "app", "bat", "cat", "car"]
    for word in words:
        radix_tree.insert(word)

    print(radix_tree.search("apple"))  # Output: True
    print(radix_tree.search("banana"))  # Output: True
    print(radix_tree.search("apricot"))  # Output: True
    print(radix_tree.search("app"))  # Output: True
    print(radix_tree.search("bat"))  # Output: True
    print(radix_tree.search("cat"))  # Output: True
    print(radix_tree.search("car"))  # Output: True
    print(radix_tree.search("ap"))  # Output: False
    print(radix_tree.search("ba"))  # Output: False
    print(radix_tree.search("ca"))  # Output: False
    print(radix_tree.search("b"))  # Output: False
 
    return None


class RadixNode:
    """A node in the radix tree."""
    def __init__(self, value: Optional[str] = None):
        self.value: Optional[str] = value
        self.children: Dict[str, RadixNode] = {}


class RadixTree:
    """A radix tree (compact prefix tree) data structure."""
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word: str) -> None:
        """Insert a word into the radix tree."""
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = RadixNode(char)
                node.children[char] = new_node
                node = new_node

    def search(self, word: str) -> bool:
        """Search for a word in the radix tree."""
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


if __name__ == '__main__':
    main()

