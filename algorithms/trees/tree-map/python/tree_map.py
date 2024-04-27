#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tree_map.py

    TreeNode Class: Represents a node in the binary search tree. Each node contains a key-value pair and references to its left and right children.

    TreeMap Class: Implements a sorted map using a binary search tree. It provides methods for inserting, retrieving, and deleting key-value pairs. The tree maintains the property that keys are sorted in ascending order.

    put Method: Inserts or updates a key-value pair in the tree. If the key already exists, its corresponding value is updated.

    get Method: Retrieves the value associated with the given key.

    delete Method: Removes the key-value pair with the given key from the tree.

    traverse_in_order Method: Performs an in-order traversal of the tree and returns key-value pairs as a tuple.

    Example Usage: Demonstrates how to use the TreeMap class by inserting some key-value pairs and printing the contents of the tree using an in-order traversal.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Any, Optional, Tuple


def main() -> None:
    """Driving code and main function"""
    tree_map = TreeMap()
    tree_map.put(5, "five")
    tree_map.put(3, "three")
    tree_map.put(7, "seven")
    tree_map.put(2, "two")
    tree_map.put(4, "four")
    tree_map.put(6, "six")
    tree_map.put(8, "eight")

    print("TreeMap contents (in-order traversal):", tree_map.traverse_in_order())
 
    return None


class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class TreeMap:
    """A sorted map implemented using a binary search tree."""
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def put(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair in the tree."""
        self.root = self._put(self.root, key, value)

    def _put(self, node: Optional[TreeNode], key: Any, value: Any) -> TreeNode:
        """Helper method to recursively insert or update a key-value pair."""
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        
        return node

    def get(self, key: Any) -> Optional[Any]:
        """Retrieve the value associated with the given key."""
        return self._get(self.root, key)

    def _get(self, node: Optional[TreeNode], key: Any) -> Optional[Any]:
        """Helper method to recursively retrieve the value associated with the given key."""
        if node is None:
            return None
        
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def delete(self, key: Any) -> None:
        """Remove the key-value pair with the given key."""
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[TreeNode], key: Any) -> Optional[TreeNode]:
        """Helper method to recursively remove the key-value pair with the given key."""
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._min(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self._delete(node.right, successor.key)
        
        return node

    def _min(self, node: TreeNode) -> TreeNode:
        """Helper method to find the minimum node in the subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def traverse_in_order(self) -> Tuple:
        """Traverse the tree in in-order and return key-value pairs."""
        result = []
        self._traverse_in_order(self.root, result)
        return tuple(result)

    def _traverse_in_order(self, node: Optional[TreeNode], result: List) -> None:
        """Helper method to recursively traverse the tree in in-order."""
        if node is None:
            return
        self._traverse_in_order(node.left, result)
        result.append((node.key, node.value))
        self._traverse_in_order(node.right, result)


if __name__ == '__main__':
    main()

