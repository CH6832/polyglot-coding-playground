#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""binary_search_tree.py

    Binary Search Tree (BST): The BinarySearchTree class represents a binary search tree data structure. It includes methods for insertion, searching, and inorder traversal.

    TreeNode: The TreeNode class represents a node in the binary search tree. Each node contains a key value and pointers to its left and right children.

    Insertion: The insert method inserts a key into the binary search tree. It recursively inserts the key into the appropriate subtree based on its value.

    Searching: The search method searches for a key in the binary search tree. It recursively traverses the tree to find the node with the given key, returning None if the key is not found.

    Inorder Traversal: The inorder_traversal method performs an inorder traversal of the binary search tree. It recursively visits the left subtree, prints the key of the current node, and then recursively visits the right subtree, resulting in keys printed in sorted order.

    Example Usage: In the example usage section, a binary search tree is created, keys are inserted into it, and an inorder traversal is performed to print the keys in sorted order. Additionally, a search operation is performed to find a specific key in the tree, demonstrating the search functionality.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Optional

class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """A binary search tree."""
    def __init__(self) -> None:
        self.root = None

    def insert(self, key: int) -> None:
        """Insert a key into the binary search tree."""
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[TreeNode], key: int) -> TreeNode:
        """Recursively insert a key into the binary search tree."""
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def search(self, key: int) -> Optional[TreeNode]:
        """Search for a key in the binary search tree."""
        return self._search(self.root, key)

    def _search(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Recursively search for a key in the binary search tree."""
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self) -> None:
        """Perform an inorder traversal of the binary search tree."""
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node: Optional[TreeNode]) -> None:
        """Recursively perform an inorder traversal."""
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=" ")
            self._inorder_traversal(node.right)

if __name__ == "__main__":
    # Example: Create a binary search tree and perform insertions
    bst = BinarySearchTree()
    keys = [10, 5, 15, 3, 7, 12, 17]
    for key in keys:
        bst.insert(key)

    # Perform inorder traversal to print keys in sorted order
    print("Inorder traversal of the binary search tree:")
    bst.inorder_traversal()

    # Search for a key in the binary search tree
    search_key = 7
    result = bst.search(search_key)
    if result:
        print(f"Key {search_key} found in the binary search tree.")
    else:
        print(f"Key {search_key} not found in the binary search tree.")


