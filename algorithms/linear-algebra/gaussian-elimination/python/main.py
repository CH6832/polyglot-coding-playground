Certainly! Here's a basic implementation of Gaussian Elimination in Python without using any third-party libraries:

python

def gaussian_elimination(A, b):
    n = len(A)
    # Augmenting the coefficient matrix with the right-hand side vector
    Ab = [row + [bi] for row, bi in zip(A, b)]

    # Forward elimination
    for i in range(n):
        # Partial pivoting: find the row with the largest absolute value in the current column
        max_row = max(range(i, n), key=lambda r: abs(Ab[r][i]))
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        # Make the diagonal element 1
        divisor = Ab[i][i]
        for j in range(i, n + 1):
            Ab[i][j] /= divisor

        # Eliminate lower triangular elements
        for k in range(i + 1, n):
            multiplier = Ab[k][i]
            for j in range(i, n + 1):
                Ab[k][j] -= multiplier * Ab[i][j]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n]
        for j in range(i + 1, n):
            x[i] -= Ab[i][j] * x[j]

    return x

# Example usage:
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

solution = gaussian_elimination(A, b)
print("Solution:", solution)

In this implementation:

    The gaussian_elimination() function takes the coefficient matrix A and the right-hand side vector b as input.
    It performs Gaussian elimination with partial pivoting to transform the augmented matrix [A | b] into row-echelon form.
    After forward elimination, it performs back substitution to find the solution vector x.
    The function returns the solution vector x.

This implementation provides a basic way to solve a system of linear equations using Gaussian Elimination without relying on any third-party libraries.