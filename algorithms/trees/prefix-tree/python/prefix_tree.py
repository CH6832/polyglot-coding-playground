#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""prefix_tree.py

    TrieNode Class: This class represents a node in the trie. Each node contains a dictionary mapping characters to child nodes and a boolean flag indicating whether the node represents the end of a word.

    Trie Class: This class represents the trie data structure. It has methods for inserting a word into the trie (insert), searching for a word in the trie (search), and checking if there is any word in the trie that starts with a given prefix (starts_with).

    Example Usage: In the __main__ block, an example usage of the Trie class is provided. Words are inserted into the trie using the insert method, and then various words and prefixes are searched for using the search and starts_with methods, respectively.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List, Dict

V = 4


def main() -> None:
    """Driving code and main function"""
    trie = Trie()
    words = ["apple", "banana", "apricot", "app", "bat", "cat", "car"]
    for word in words:
        trie.insert(word)

    print(trie.search("apple"))  # Output: True
    print(trie.search("banana"))  # Output: True
    print(trie.search("apricot"))  # Output: True
    print(trie.search("app"))  # Output: True
    print(trie.search("bat"))  # Output: True
    print(trie.search("cat"))  # Output: True
    print(trie.search("car"))  # Output: True
    print(trie.search("ap"))  # Output: False
    print(trie.search("ba"))  # Output: False
    print(trie.search("ca"))  # Output: False
    print(trie.search("b"))  # Output: False
 
    return None


class TrieNode:
    """A node in the trie."""
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    """A prefix tree (trie) data structure."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for a word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Check if there is any word in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    main()

