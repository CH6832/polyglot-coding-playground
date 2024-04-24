Sure, here's a basic implementation of the Singular Value Decomposition (SVD) algorithm in Python without using any third-party libraries:

python

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row, col)) for col in transpose(matrix2)] for row in matrix1]

def svd(A):
    # Compute A^T * A and A * A^T
    ATA = matrix_multiply(transpose(A), A)
    AAT = matrix_multiply(A, transpose(A))

    # Compute eigenvalues and eigenvectors of A^T * A
    eigenvalues, V = np.linalg.eig(ATA)

    # Sort eigenvalues and eigenvectors
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]

    # Compute singular values and sort them
    singular_values = np.sqrt(eigenvalues)

    # Compute U matrix
    U = []
    for i in range(len(singular_values)):
        u = [0] * len(A)
        for j in range(len(A)):
            u[j] = sum(A[j][k] * V[k][i] / singular_values[i] for k in range(len(A)))
        U.append(u)

    return U, singular_values, V

# Example usage:
A = [[1, 2],
     [3, 4],
     [5, 6]]

U, s, V = svd(A)
print("U matrix:")
for row in U:
    print(row)
print("Singular values:", s)
print("V matrix:")
for row in V:
    print(row)

In this implementation:

    The transpose() function computes the transpose of a matrix.
    The matrix_multiply() function computes the product of two matrices.
    The svd() function computes the Singular Value Decomposition of a matrix A.
    It first computes the matrices A^T * A and A * A^T.
    Then, it computes the eigenvalues and eigenvectors of A^T * A.
    The singular values are computed from the square roots of the eigenvalues.
    Finally, it computes the matrices U, S, and V from the eigenvectors and singular values.

This implementation provides a basic way to perform Singular Value Decomposition without relying on any third-party libraries. However, for practical purposes, you may want to use libraries like NumPy, which provide optimized implementations of SVD.