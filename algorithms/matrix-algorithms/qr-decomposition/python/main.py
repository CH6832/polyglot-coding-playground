Here's a basic implementation of QR decomposition in Python without using any third-party libraries:

python
def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def vector_subtract(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def scalar_multiply(c, v):
    return [c * x for x in v]

def qr_decomposition(A):
    m, n = len(A), len(A[0])
    Q = [[0] * m for _ in range(m)]
    R = [[0] * n for _ in range(m)]

    for j in range(n):
        v = list(A[i][j] for i in range(m))
        for i in range(j):
            R[i][j] = dot_product(Q[i], A[j])
            v = vector_subtract(v, scalar_multiply(R[i][j], Q[i]))
        R[j][j] = sum(x ** 2 for x in v) ** 0.5
        Q[j] = [x / R[j][j] for x in v]

    return Q, R

# Example usage:
A = [[4, -1, 0],
     [-1, 4, -1],
     [0, -1, 4]]  # Square matrix

Q, R = qr_decomposition(A)
print("Q (Orthogonal Matrix):")
for row in Q:
    print(row)
print("R (Upper Triangular Matrix):")
for row in R:
    print(row)
In this implementation:

    The qr_decomposition() function takes a matrix A as input.
    It initializes matrices Q and R as zero matrices of appropriate sizes.
    It iteratively computes the columns of Q and the entries of R using the Gram-Schmidt process.
    The resulting matrices Q and R form the QR decomposition of the original matrix A, where Q is orthogonal and R is upper triangular.

This implementation provides a basic way to perform QR decomposition without relying on any third-party libraries. However, for practical purposes, you may want to use libraries like NumPy, which provide optimized implementations of QR decomposition.