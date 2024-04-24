Here's a basic implementation of the Gradient Descent algorithm in Python without using any third-party libraries:

python

import numpy as np

def gradient_descent(f, df, x0, learning_rate=0.01, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        gradient = df(x)
        x_new = x - learning_rate * gradient
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
    return x

# Example usage:
def f(x):
    return x**2 + 5 * np.sin(x)

def df(x):
    return 2 * x + 5 * np.cos(x)

x0 = 0  # Initial guess
x_opt = gradient_descent(f, df, x0)
print("Optimal solution:", x_opt)
print("Minimum value:", f(x_opt))

In this implementation:

    The gradient_descent() function takes a function f to minimize, its gradient function df, an initial guess x0, and optional parameters for learning rate, tolerance, and maximum iterations.
    It iteratively updates the solution x by taking steps in the direction of the negative gradient until convergence or the maximum number of iterations is reached.
    The algorithm terminates when the norm of the difference between successive solutions falls below a specified tolerance.
    The function returns the approximate optimal solution x.

This implementation provides a basic way to minimize a function using the Gradient Descent algorithm without relying on any third-party libraries. However, for practical purposes, you may want to use libraries like NumPy for efficient numerical computations and optimization.