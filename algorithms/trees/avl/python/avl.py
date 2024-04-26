#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""avl.py

    AVL Tree: The AVLTree class represents the AVL tree data structure. It consists of methods for insertion and traversal operations.

    AVLNode: The AVLNode class represents a node in the AVL tree. Each node contains a key value, height, and pointers to its left and right children.

    Insertion: The insert method inserts a key into the AVL tree while maintaining the balance property. It recursively inserts the key into the appropriate subtree and performs rotations as necessary to balance the tree.

    Rotations: The _rotate_right and _rotate_left methods perform right and left rotations, respectively, at a given node to balance the tree.

    Height and Balance Factor: The _height method calculates the height of a node, while the _balance_factor method calculates the balance factor (difference in heights of the left and right subtrees).

    Inorder Traversal: The inorder_traversal method performs an inorder traversal of the

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Optional

class AVLNode:
    """A node in the AVL tree."""
    def __init__(self, key: int) -> None:
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    """A self-balancing AVL tree."""
    def __init__(self) -> None:
        self.root = None

    def _height(self, node: Optional[AVLNode]) -> int:
        """Return the height of the node."""
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        """Return the balance factor of the node."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node: AVLNode) -> None:
        """Update the height of the node based on its children."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """Perform a right rotation at the given node."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """Perform a left rotation at the given node."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, key: int) -> None:
        """Insert a key into the AVL tree."""
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        """Recursively insert a key into the AVL tree."""
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        # Update height of the current node
        self._update_height(node)

        # Perform rotations to balance the tree
        balance = self._balance_factor(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def inorder_traversal(self) -> None:
        """Perform an inorder traversal of the AVL tree."""
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node: Optional[AVLNode]) -> None:
        """Recursively perform an inorder traversal."""
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=" ")
            self._inorder_traversal(node.right)

if __name__ == "__main__":
    # Example: Create an AVL tree and perform insertions
    avl_tree = AVLTree()
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        avl_tree.insert(key)

    print("Inorder traversal of the AVL tree:")
    avl_tree.inorder_traversal()


