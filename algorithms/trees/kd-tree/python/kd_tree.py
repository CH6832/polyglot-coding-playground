#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""kd_tree.py

    Node Class: Represents a node in the KD tree. Each node contains a k-dimensional point, an axis used for splitting, and references to left and right child nodes.

    KDTree Class: Represents the KD tree data structure. It provides methods for building the tree from a list of points and finding the nearest neighbor of a target point.

    Initialization: In the __init__ method of the KDTree class, the tree is constructed recursively using the _build_tree method.

    Nearest Neighbor Search: The nearest_neighbor method is used to find the nearest neighbor of a given target point. It recursively searches the tree to find the closest point to the target.

    Example Usage: In the __main__ block, an example usage of the KD tree is provided. It initializes a KD tree with a list of points, and then finds the nearest neighbor of a target point and prints the result.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List, Tuple, Optional


def main() -> None:
    """Driving code and main function"""
    # Example usage
    points = [[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]]
    kd_tree = KDTree(points)
    
    target_point = [5, 5]
    nearest_neighbor = kd_tree.nearest_neighbor(target_point)
    print(f"The nearest neighbor of {target_point} is {nearest_neighbor}")
 
    return None


class Node:
    """A node in the KD tree."""
    def __init__(self, point: List[int], axis: int) -> None:
        self.point = point  # The k-dimensional point stored in the node
        self.axis = axis    # The axis used for splitting the space
        self.left: Optional[Node] = None   # Left child node
        self.right: Optional[Node] = None  # Right child node

class KDTree:
    """A KD tree data structure."""
    def __init__(self, points: List[List[int]]) -> None:
        """
        Initialize the KD tree with a list of k-dimensional points.

        Args:
            points (List[List[int]]): A list of k-dimensional points.
        """
        self.root = self._build_tree(points, axis=0)

    def _build_tree(self, points: List[List[int]], axis: int) -> Optional[Node]:
        """
        Recursively build the KD tree from the given points.

        Args:
            points (List[List[int]]): A list of k-dimensional points.
            axis (int): The axis used for splitting the space.

        Returns:
            Optional[Node]: The root node of the constructed subtree.
        """
        if not points:
            return None
        
        # Sort points along the current axis
        points.sort(key=lambda x: x[axis])
        
        # Choose the median point as the pivot
        median_idx = len(points) // 2
        median = points[median_idx]
        
        # Recursively build left and right subtrees
        next_axis = (axis + 1) % len(median)
        node = Node(median, axis)
        node.left = self._build_tree(points[:median_idx], next_axis)
        node.right = self._build_tree(points[median_idx + 1:], next_axis)
        
        return node

    def nearest_neighbor(self, target: List[int]) -> List[int]:
        """
        Find the nearest neighbor of a given target point in the KD tree.

        Args:
            target (List[int]): The target k-dimensional point.

        Returns:
            List[int]: The nearest neighbor point found in the KD tree.
        """
        if not self.root:
            return []
        
        best = [float('inf'), None]  # [distance, nearest point]
        self._nearest_neighbor(self.root, target, best)
        return best[1]

    def _nearest_neighbor(self, node: Optional[Node], target: List[int], best: List[int]) -> None:
        """
        Recursively search for the nearest neighbor of the target point.

        Args:
            node (Optional[Node]): The current node being examined.
            target (List[int]): The target k-dimensional point.
            best (List[int]): The current best distance and nearest point found so far.
        """
        if node is None:
            return
        
        # Calculate the distance from target to the current node
        distance = sum((target[i] - node.point[i]) ** 2 for i in range(len(target)))
        
        # Update best if the current node is closer
        if distance < best[0]:
            best[0] = distance
            best[1] = node.point
        
        # Recursively search left or right subtree based on the splitting axis
        axis = node.axis
        if target[axis] < node.point[axis]:
            self._nearest_neighbor(node.left, target, best)
            if (node.point[axis] - target[axis]) ** 2 < best[0]:
                self._nearest_neighbor(node.right, target, best)
        else:
            self._nearest_neighbor(node.right, target, best)
            if (target[axis] - node.point[axis]) ** 2 < best[0]:
                self._nearest_neighbor(node.left, target, best)


if __name__ == '__main__':
    main()

