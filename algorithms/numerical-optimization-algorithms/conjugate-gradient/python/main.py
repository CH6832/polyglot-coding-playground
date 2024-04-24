Here's a basic implementation of the Conjugate Gradient method in Python without using any third-party libraries:

python

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def matrix_vector_multiply(A, v):
    return [dot_product(row, v) for row in A]

def vector_subtract(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def vector_add(v1, v2):
    return [x + y for x, y in zip(v1, v2)]

def scalar_multiply(c, v):
    return [c * x for x in v]

def conjugate_gradient(A, b, x0, tol=1e-10, max_iter=1000):
    x = x0
    r = vector_subtract(b, matrix_vector_multiply(A, x))
    p = r
    rsold = dot_product(r, r)

    for i in range(max_iter):
        Ap = matrix_vector_multiply(A, p)
        alpha = rsold / dot_product(p, Ap)
        x = vector_add(x, scalar_multiply(alpha, p))
        r = vector_subtract(r, scalar_multiply(alpha, Ap))
        rsnew = dot_product(r, r)
        if rsnew < tol:
            break
        beta = rsnew / rsold
        p = vector_add(r, scalar_multiply(beta, p))
        rsold = rsnew

    return x

# Example usage:
A = [[4, -1, 0],
     [-1, 4, -1],
     [0, -1, 4]]  # Symmetric positive definite matrix
b = [1, 2, 3]   # Right-hand side vector
x0 = [0, 0, 0]  # Initial guess

x = conjugate_gradient(A, b, x0)
print("Solution:", x)

In this implementation:

    The conjugate_gradient() function takes a matrix A, a right-hand side vector b, an initial guess x0, and optional parameters tol (tolerance for convergence) and max_iter (maximum number of iterations) as input.
    It iteratively updates the solution vector x using the Conjugate Gradient method until convergence or reaching the maximum number of iterations.
    The functions dot_product(), matrix_vector_multiply(), vector_subtract(), vector_add(), and scalar_multiply() perform basic vector and matrix operations.

This implementation provides a basic way to solve a linear system of equations using the Conjugate Gradient method without relying on any third-party libraries. However, for practical purposes, you may want to use libraries like NumPy, which provide optimized implementations of linear solvers.