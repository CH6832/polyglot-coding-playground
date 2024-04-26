#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""singular_value_decomposition.py

Singular Value Decomposition (SVD) is a matrix factorization technique that decomposes a matrix into three matrices: U, S, and V^T, where U and V are orthogonal matrices and S is a diagonal matrix containing the singular values of the original matrix.

    Initialization: Given a matrix A, we compute its SVD using NumPy's np.linalg.svd function.

    Result: The function returns three matrices: U, S, and V^T. U contains the left singular vectors, S contains the singular values as a diagonal matrix, and V^T contains the right singular vectors (transpose of V).

    Example Usage: In the if __name__ == "__main__": block, an example usage of the svd function is provided. We define a matrix A, and then call the svd function to compute its SVD. Finally, we print the left singular vectors (U), singular values (S), and right singular vectors (V^T).

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


import numpy as np
from typing import Tuple


def main() -> None:
    """Driving code and main function"""
    # Example: Singular Value Decomposition (SVD)
    A = np.array([[1, 2], [3, 4], [5, 6]])

    U, S, Vt = svd(A)

    print("Left singular vectors (U):\n", U)
    print("Singular values (S):\n", S)
    print("Right singular vectors (V^T):\n", Vt)
 
    return None


def svd(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Perform Singular Value Decomposition (SVD) of a matrix.

    Args:
        A (np.ndarray): Matrix to decompose.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the left singular vectors (U),
            the singular values (S), and the right singular vectors (V^T).
    """
    U, S_diag, Vt = np.linalg.svd(A)

    # Convert singular values to a diagonal matrix
    S = np.diag(S_diag)

    return U, S, Vt.T


if __name__ == '__main__':
    main()

