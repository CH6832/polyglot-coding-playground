#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""splay_tree.py

SplayNode Class: Represents a node in the splay tree. Each node contains a key value
and references to its left and right child nodes.

SplayTree Class: Represents the splay tree data structure. It has methods for
inserting a key into the tree (insert), searching for a key in the tree (search),
and performing splay operations to bring a node with a given key to the root of
the tree (_splay, _rotate_left, _rotate_right). The splay operation involves
performing rotations on the tree to move the node closer to the root.

Example Usage: In the __main__ block, an example usage of the SplayTree class is
provided. Keys are inserted into the tree using the insert method, and then various
keys are searched for using the search method. The splay operation is automatically
performed during search operations to optimize the tree structure.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Optional


def main() -> None:
    """Driving code and main function"""
    splay_tree = SplayTree()
    keys = [7, 3, 10, 2, 6, 9, 11, 1, 5, 8, 12]
    for key in keys:
        splay_tree.insert(key)

    print(splay_tree.search(8))  # Output: True
    print(splay_tree.search(4))  # Output: False
 
    return None


class SplayNode:
    """A node in the splay tree."""
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[SplayNode] = None
        self.right: Optional[SplayNode] = None

class SplayTree:
    """A splay tree data structure."""
    def __init__(self):
        self.root: Optional[SplayNode] = None

    def insert(self, key: int) -> None:
        """Insert a key into the splay tree."""
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[SplayNode], key: int) -> SplayNode:
        """Helper function to insert a key into the splay tree."""
        if not node:
            return SplayNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key: int) -> bool:
        """Search for a key in the splay tree."""
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def _splay(self, node: Optional[SplayNode], key: int) -> Optional[SplayNode]:
        """Splay the tree to bring the node with the given key to the root."""
        if not node or node.key == key:
            return node

        if key < node.key:
            if not node.left:
                return node
            if key < node.left.key:
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                node.left.right = self._splay(node.left.right, key)
                if node.left.right:
                    node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        else:
            if not node.right:
                return node
            if key > node.right.key:
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            elif key < node.right.key:
                node.right.left = self._splay(node.right.left, key)
                if node.right.left:
                    node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

    def _rotate_left(self, node: SplayNode) -> SplayNode:
        """Perform a left rotation on the given node."""
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_right(self, node: SplayNode) -> SplayNode:
        """Perform a right rotation on the given node."""
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root


if __name__ == '__main__':
    main()
