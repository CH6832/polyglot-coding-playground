#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fenwick_tree.py

    FenwickTree Class: This class represents the Fenwick tree data structure. It has methods for updating elements, querying prefix sums, and querying the sum of elements in a given range.

    Initialization: In the __init__ method, the Fenwick tree is initialized with a given size. The tree is represented as a list with one extra element for 0-based indexing.

    Update Method: The update method updates the value at a given index by adding a delta value. It uses bitwise operations to efficiently traverse the tree and update the relevant nodes.

    Query Methods: The query method calculates the prefix sum up to a given index, while the range_query method calculates the sum of elements in a given range. Both methods use bitwise operations to efficiently traverse the tree and calculate the sums.

    Example Usage: In the __main__ block, an example usage of the Fenwick tree is provided. It initializes a Fenwick tree with a list of numbers, updates the tree with the numbers, and then prints the prefix sums up to each index.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List

class FenwickTree:
    """A Fenwick tree (Binary Indexed Tree) for efficient prefix sum calculations."""
    
    def __init__(self, size: int) -> None:
        """Initialize the Fenwick tree with given size."""
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """
        Update the value at the given index by adding delta.

        Args:
            index (int): The index to be updated.
            delta (int): The value to be added to the element at index.
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        """
        Calculate the prefix sum up to the given index.

        Args:
            index (int): The index up to which the prefix sum is calculated.

        Returns:
            int: The prefix sum up to the given index.
        """
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, start: int, end: int) -> int:
        """
        Calculate the sum of elements in the range [start, end].

        Args:
            start (int): The start index of the range.
            end (int): The end index of the range.

        Returns:
            int: The sum of elements in the range [start, end].
        """
        return self.query(end) - self.query(start - 1) if start > 0 else self.query(end)

if __name__ == "__main__":
    # Example usage
    nums = [1, 3, 5, 7, 9, 11, 13, 15]
    fenwick_tree = FenwickTree(len(nums))
    for i, num in enumerate(nums, 1):
        fenwick_tree.update(i, num)
    
    # Print prefix sums
    for i in range(len(nums) + 1):
        print(f"Prefix sum up to index {i}: {fenwick_tree.query(i)}")
