#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""segment_tree.py

SegmentTreeNode Class: Represents a node in the segment tree. Each node contains information about the start and end indices of the segment it represents, the total sum (or any other aggregate value) of the segment, and references to its left and right child nodes.

SegmentTree Class: Represents the segment tree data structure. It has methods for building the tree (build_tree), querying the total sum over a range (query), and updating the value of an element (update). The build_tree method constructs the segment tree recursively, dividing the array into smaller segments until each node represents a single element. The query method retrieves the total sum over a given range by traversing the tree recursively. The update method modifies the value of a specific element in the array and updates the segment tree accordingly.

Example Usage: In the __main__ block, an example usage of the SegmentTree class is provided. A segment tree is constructed from a list of numbers, and queries are performed to find the total sum over various ranges. Additionally, an element in the array is updated, and subsequent queries reflect the change in the segment tree.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List


def main() -> None:
    """Driving code and main function"""
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    init_vertex = 0    
    minimum_path = travelling_salesman_problem(graph, init_vertex)
    print(f"Minimum path weight is '{minimum_path}'")
 
    return None


class SegmentTreeNode:
    """A node in the segment tree."""
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class SegmentTree:
    """A segment tree data structure for range queries."""
    def __init__(self, nums: List[int]):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums: List[int], start: int, end: int) -> SegmentTreeNode:
        """Recursively build the segment tree."""
        if start == end:
            node = SegmentTreeNode(start, end)
            node.total = nums[start]
            return node

        mid = (start + end) // 2
        left_node = self.build_tree(nums, start, mid)
        right_node = self.build_tree(nums, mid + 1, end)

        node = SegmentTreeNode(start, end)
        node.total = left_node.total + right_node.total
        node.left = left_node
        node.right = right_node
        return node

    def query(self, start: int, end: int) -> int:
        """Query the total sum over the range [start, end]."""
        return self._query(self.root, start, end)

    def _query(self, node: SegmentTreeNode, start: int, end: int) -> int:
        """Helper function for querying the segment tree."""
        if node.start == start and node.end == end:
            return node.total

        mid = (node.start + node.end) // 2

        if end <= mid:
            return self._query(node.left, start, end)
        elif start >= mid + 1:
            return self._query(node.right, start, end)
        else:
            left_sum = self._query(node.left, start, mid)
            right_sum = self._query(node.right, mid + 1, end)
            return left_sum + right_sum

    def update(self, index: int, value: int) -> None:
        """Update the value of the element at the given index."""
        self._update(self.root, index, value)

    def _update(self, node: SegmentTreeNode, index: int, value: int) -> None:
        """Helper function for updating the segment tree."""
        if node.start == node.end == index:
            node.total = value
            return

        mid = (node.start + node.end) // 2

        if index <= mid:
            self._update(node.left, index, value)
        else:
            self._update(node.right, index, value)

        node.total = node.left.total + node.right.total


if __name__ == '__main__':
    main()

