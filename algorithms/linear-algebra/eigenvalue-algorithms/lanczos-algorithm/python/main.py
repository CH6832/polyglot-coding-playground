Implementing the full Lanczos algorithm from scratch can be quite complex, especially without using third-party libraries. However, I can provide a simplified version of the Lanczos algorithm for finding eigenvalues and eigenvectors of a symmetric matrix. Here's a basic implementation in Python:

python

import numpy as np

def lanczos_algorithm(A, num_iterations):
    n = len(A)
    Q = np.zeros((n, num_iterations))
    alpha = np.zeros(num_iterations)
    beta = np.zeros(num_iterations - 1)

    Q[:, 0] = np.random.rand(n)  # Random initial vector

    for k in range(num_iterations):
        if k > 0:
            Q[:, k] = A.dot(Q[:, k - 1]) - beta[k - 1] * Q[:, k - 2]

        alpha[k] = Q[:, k].dot(A.dot(Q[:, k]))
        if k < num_iterations - 1:
            v = A.dot(Q[:, k]) - alpha[k] * Q[:, k]
            beta[k] = np.linalg.norm(v)
            if beta[k] == 0:
                break
            Q[:, k + 1] = v / beta[k]

    T = np.diag(alpha) + np.diag(beta, k=1) + np.diag(beta, k=-1)
    eigenvalues, eigenvectors = np.linalg.eig(T)
    return eigenvalues, eigenvectors

# Example usage:
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]])  # Symmetric matrix
num_iterations = 3

eigenvalues, eigenvectors = lanczos_algorithm(A, num_iterations)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

In this implementation:

    The lanczos_algorithm() function takes a symmetric matrix A and the number of Lanczos iterations as input.
    It generates a random initial vector Q[:, 0] and iteratively constructs the Lanczos basis vectors Q[:, k].
    At each iteration, it computes the Lanczos coefficients alpha[k] and beta[k].
    It constructs the tridiagonal matrix T using the Lanczos coefficients.
    Finally, it uses numpy.linalg.eig() to compute the eigenvalues and eigenvectors of T.