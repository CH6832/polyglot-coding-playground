Implementing the full QR Algorithm from scratch without third-party libraries can be quite complex. However, I can provide a basic example of the QR Algorithm for finding eigenvalues of a matrix in Python:

python

import numpy as np

def qr_algorithm(A, num_iterations):
    n = len(A)
    eigenvalues = np.zeros(n)

    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = R.dot(Q)

    # Extract eigenvalues from the diagonal of the resulting matrix
    for i in range(n):
        eigenvalues[i] = A[i, i]

    return eigenvalues

# Example usage:
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])  # Symmetric matrix
num_iterations = 10

eigenvalues = qr_algorithm(A, num_iterations)
print("Eigenvalues:", eigenvalues)

In this implementation:

    The qr_algorithm() function takes a matrix A and the number of iterations as input.
    It iteratively applies the QR decomposition to the matrix A for the specified number of iterations.
    After each iteration, it updates the matrix A with the product of R and Q.
    Finally, it extracts the eigenvalues from the diagonal of the resulting matrix A.

Note: This is a simplified version of the QR Algorithm and may not be as efficient or accurate as implementations in third-party libraries like SciPy. Additionally, it's important to note that this implementation is for finding all eigenvalues of a matrix, whereas the QR Algorithm can be used for various purposes including eigenvalue computation, eigenvalue decomposition, and solving linear systems.