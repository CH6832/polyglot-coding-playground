#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

The orientation function calculates the orientation of three points (p, q, r) using
the cross product method. It returns 0 if the points are collinear, 1 if they form
a clockwise orientation, and 2 if they form a counterclockwise orientation.

The convex_hull function finds the convex hull of a set of points using the Graham
Scan algorithm. It first finds the point with the lowest y-coordinate (and the
leftmost point in case of a tie) and sorts the remaining points by polar angle
in counterclockwise order with respect to the first point. Then, it initializes
a stack for the convex hull and iterates over the sorted points, adding them to
the convex hull if they form a counterclockwise orientation with respect to the
last two points on the stack.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


import math
from typing import Tuple, List
import matplotlib.pyplot as plt


def main() -> None:
    """Driving code and main function"""
    # Example points
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]

    # Find the convex hull
    convex_points = convex_hull(points)

    # Plot the points and convex hull
    plt.scatter(*zip(*points), color='blue', label='Points')
    plt.plot(*zip(*convex_points + [convex_points[0]]), color='red', linestyle='-', linewidth=2, label='Convex Hull')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Convex Hull Example')
    plt.legend()
    plt.show()
 
    return None


def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    """Calculates the orientation of three points (p, q, r).

    Args:
        p (Tuple[int, int]): The first point as a tuple (x, y).
        q (Tuple[int, int]): The second point as a tuple (x, y).
        r (Tuple[int, int]): The third point as a tuple (x, y).

    Returns:
        int: Returns 0 if p, q, and r are collinear, 1 if they form a clockwise orientation,
             and 2 if they form a counterclockwise orientation.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Finds the convex hull of a set of points using the Graham Scan algorithm.

    Args:
        points (List[Tuple[int, int]]): A list of points represented as tuples (x, y).

    Returns:
        List[Tuple[int, int]]: A list of points on the convex hull in counterclockwise order.
    """
    n = len(points)
    if n < 3:
        return []

    # Find the point with the lowest y-coordinate (and the leftmost point in case of a tie)
    min_idx = 0
    for i in range(1, n):
        if points[i][1] < points[min_idx][1] or (points[i][1] == points[min_idx][1] and points[i][0] < points[min_idx][0]):
            min_idx = i

    # Swap the first point with the point found above
    points[0], points[min_idx] = points[min_idx], points[0]

    # Sort the remaining points by polar angle in counterclockwise order with respect to the first point
    anchor = points[0]
    points[1:] = sorted(points[1:], key=lambda x: (180 + (180 / 3.14159265358979323846) * (math.atan2(x[1] - anchor[1], x[0] - anchor[0]))))

    # Initialize the stack for the convex hull
    stack = [points[0], points[1]]

    # Iterate over the sorted points and keep adding them to the convex hull
    for i in range(2, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])

    return stack


if __name__ == '__main__':
    main()

