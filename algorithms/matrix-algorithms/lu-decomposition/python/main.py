Here's a basic implementation of LU decomposition in Python without using any third-party libraries:

python

import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        U[i, i:] = A[i, i:] - L[i, :i].dot(U[:i, i:])
        L[i+1:, i] = (A[i+1:, i] - L[i+1:, :i].dot(U[:i, i])) / U[i, i]

    return L, U

# Example usage:
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])  # Square matrix
L, U = lu_decomposition(A)
print("Lower Triangular Matrix (L):")
print(L)
print("Upper Triangular Matrix (U):")
print(U)

In this implementation:

    The lu_decomposition() function takes a square matrix A as input.
    It initializes matrices L and U as identity and zero matrices, respectively.
    It iteratively computes the elements of L and U using the LU decomposition algorithm.
    The resulting matrices L and U are the lower and upper triangular parts of the original matrix A, respectively.

This implementation provides a basic way to perform LU decomposition without relying on any third-party libraries. However, for practical purposes, you may want to use libraries like NumPy, which provide optimized implementations of LU decomposition.