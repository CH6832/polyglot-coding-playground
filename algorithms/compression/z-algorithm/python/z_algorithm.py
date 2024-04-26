#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

This program consists of a function z_algorithm that implements the Z-algorithm to
find all occurrences of a pattern within a text. The module docstring provides an
explanation of the Z-algorithm's functionality and the program's purpose. The function
docstring describes the function's parameters, return type, and includes an example of
usage.

The z_algorithm function takes a string text as input and returns a list containing
the starting indices of all occurrences of the pattern within the text. It follows
the Z-algorithm's steps to calculate the Z-values for each position in the text,
identifying the matches between the pattern and substrings of the text.

Finally, in the __main__ block, an example usage demonstrates how to find occurrences
of a pattern in a given text using the z_algorithm function.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List


def main() -> None:
    """Driving code and main function"""
    text = "abababab"
    pattern = "aba"
    occurrences = z_algorithm(pattern + "$" + text)
    print(f"Occurrences of pattern '{pattern}' in text '{text}': {occurrences}")
 
    return None


def z_algorithm(text: str) -> List[int]:
    """Implements the Z-algorithm to find all occurrences of a pattern in a string.

    The Z-algorithm is an efficient string searching algorithm that finds all occurrences
    of a pattern within a text in linear time complexity. It creates an array Z where Z[i]
    represents the length of the longest substring starting from position i that matches the
    prefix of the text.

    Keyword arguments:
    text -- The text to be searched.
    """
    n = len(text)
    z = [0] * n
    left = right = 0

    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < n and text[z[i]] == text[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1

    # Find all occurrences of the pattern
    pattern_length = len(text)
    occurrences = [i for i in range(pattern_length) if z[i] == pattern_length - i]
    
    return occurrences


if __name__ == '__main__':
    main()

