#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""lu_decomposition.py

LU decomposition (also known as LU factorization) is a method used to factorize a square matrix into the product of a lower triangular matrix (L) and an upper triangular matrix (U). Given a matrix A, the LU decomposition algorithm performs the following steps:

    Initialization: Start with the identity matrix for L and a copy of A for U.

    Gaussian Elimination: Perform Gaussian elimination to transform the matrix A into an upper triangular form U while simultaneously computing the multipliers used to create the lower triangular matrix L.

    Iterative Update: Iterate over each column k (except the last one) and each row i below the diagonal. Compute the factor by dividing the element U[i, k] by the pivot element U[k, k]. Update the corresponding element in L and perform row operations to eliminate the elements below the diagonal in column k of U.

    Result: Return the lower triangular matrix L and the upper triangular matrix U.

    Example Usage: In the if __name__ == "__main__": block, an example usage of the lu_decomposition function is provided. We define a square matrix A, and then call the lu_decomposition function to compute the LU decomposition. Finally, we print the lower triangular matrix L and the upper triangular matrix U.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


import numpy as np
from typing import Tuple


def main() -> None:
    """Driving code and main function"""
    # Example: LU decomposition
    A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

    L, U = lu_decomposition(A)

    print("Lower triangular matrix (L):\n", L)
    print("Upper triangular matrix (U):\n", U)
 
    return None


def lu_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Perform LU decomposition of a square matrix.

    Args:
        A (np.ndarray): Square matrix to decompose.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing the lower triangular matrix (L) and the upper triangular matrix (U).
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    for k in range(n-1):
        for i in range(k+1, n):
            if U[k, k] == 0:
                raise ValueError("Matrix is singular")
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            for j in range(k, n):
                U[i, j] -= factor * U[k, j]

    return L, U


if __name__ == '__main__':
    main()

