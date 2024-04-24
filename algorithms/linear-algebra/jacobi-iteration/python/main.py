Sure, here's a basic implementation of the Jacobi Iteration method in Python without using any third-party libraries:

python

def jacobi_iteration(A, b, initial_guess, tolerance, max_iterations):
    n = len(A)
    x = initial_guess[:]
    x_new = [0] * n

    for _ in range(max_iterations):
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        # Check convergence
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new

        x = x_new[:]

    print("Did not converge within the maximum number of iterations.")
    return None

# Example usage:
A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]
initial_guess = [0, 0, 0]  # Initial guess
tolerance = 1e-6            # Tolerance for convergence
max_iterations = 1000       # Maximum number of iterations

solution = jacobi_iteration(A, b, initial_guess, tolerance, max_iterations)
if solution is not None:
    print("Solution:", solution)

In this implementation:

    The jacobi_iteration() function takes the coefficient matrix A, the right-hand side vector b, an initial guess for the solution, tolerance for convergence, and the maximum number of iterations as input.
    It iteratively updates the solution vector x using the Jacobi iteration method until either convergence is achieved or the maximum number of iterations is reached.
    At each iteration, it computes the updated solution vector x_new based on the Jacobi iteration formula.
    It checks for convergence by comparing the differences between corresponding elements of the old and new solution vectors.
    If convergence is achieved within the specified tolerance, it returns the solution vector. Otherwise, it prints a message indicating convergence failure.

This implementation provides a basic way to solve a system of linear equations using the Jacobi Iteration method without relying on any third-party libraries.