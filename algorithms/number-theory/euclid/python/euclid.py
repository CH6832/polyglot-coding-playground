#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""euclid.py

The Euclidean Algorithm is an efficient method for computing the greatest common divisor (GCD) of two integers.

    Algorithm: The algorithm repeatedly applies the property that the GCD of two numbers is the same as the GCD of the smaller number and the remainder when the larger number is divided by the smaller number. It continues until the remainder is zero, at which point the GCD is the remaining non-zero value.

    Implementation: The function euclidean_algorithm takes two integers a and b as input and iterates through the algorithm until b becomes zero. In each iteration, it updates a to b and b to the remainder when a is divided by b. Finally, it returns the absolute value of a, which is the GCD of the two integers.

    Example Usage: In the if __name__ == "__main__": block, an example usage of the euclidean_algorithm function is provided. We define two integers a and b, and then call the function to compute their GCD. Finally, we print the result.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List

V = 4


def main() -> None:
    """Driving code and main function"""
    # Example: Euclidean Algorithm
    a, b = 48, 18
    gcd = euclidean_algorithm(a, b)
    print(f"The GCD of {a} and {b} is {gcd}.")
 
    return None


def euclidean_algorithm(a: int, b: int) -> int:
    """Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor (GCD) of the two integers.
    """
    while b:
        a, b = b, a % b
    return abs(a)


if __name__ == '__main__':
    main()

