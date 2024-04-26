#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""qr_decomposition.py

QR decomposition is a method used to factorize a matrix into the product of an orthogonal matrix (Q) and an upper triangular matrix (R). Given a matrix A, the QR decomposition algorithm performs the following steps:

    Initialization: Start with the identity matrix for Q and a copy of A for R.

    Householder Reflections: Use Householder reflections to transform the matrix A into an upper triangular form R while simultaneously accumulating the orthogonal matrix Q.

    Iterative Update: Iterate over each column k of A. Compute the Householder vector v, which defines a reflection transformation that zeros out the elements below the diagonal in column k of R. Apply the Householder transformation to update R and accumulate the orthogonal matrix Q.

    Result: Return the orthogonal matrix Q and the upper triangular matrix R.

    Example Usage: In the if __name__ == "__main__": block, an example usage of the qr_decomposition function is provided. We define a matrix A, and then call the qr_decomposition function to compute the QR decomposition. Finally, we print the orthogonal matrix Q and the upper triangular matrix R.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


import numpy as np
from typing import Tuple


def main() -> None:
    """Driving code and main function"""
    # Example: QR decomposition
    A = np.array([[1, -1, 4], [2, 3, 1], [3, 1, 2]])

    Q, R = qr_decomposition(A)

    print("Orthogonal matrix (Q):\n", Q)
    print("Upper triangular matrix (R):\n", R)
 
    return None


def qr_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Perform QR decomposition of a matrix.

    Args:
        A (np.ndarray): Matrix to decompose.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing the orthogonal matrix (Q) and the upper triangular matrix (R).
    """
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()

    for k in range(n):
        x = R[k:, k]
        v = np.zeros_like(x)
        v[0] = np.sign(x[0]) * np.linalg.norm(x)
        v += x
        v /= np.linalg.norm(v)

        Q_k = np.eye(m)
        Q_k[k:, k:] -= 2 * np.outer(v, v)

        R = np.dot(Q_k, R)
        Q = np.dot(Q, Q_k.T)

    return Q, R


if __name__ == '__main__':
    main()

