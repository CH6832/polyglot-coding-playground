Here's a basic implementation of the gradient descent algorithm in Python without using any third-party libraries:

python

def gradient_descent(x, y, learning_rate, epochs):
    m = 0  # Slope of the line
    b = 0  # Intercept of the line
    n = len(x)

    for _ in range(epochs):
        # Calculate gradients
        m_gradient = 0
        b_gradient = 0
        for i in range(n):
            m_gradient += -2 * x[i] * (y[i] - (m * x[i] + b))
            b_gradient += -2 * (y[i] - (m * x[i] + b))

        # Update parameters using gradients
        m -= (learning_rate * m_gradient) / n
        b -= (learning_rate * b_gradient) / n

    return m, b

# Example usage:
x = [1, 2, 3, 4, 5]  # Input features
y = [2, 4, 5, 4, 5]  # Target values
learning_rate = 0.01
epochs = 1000

m, b = gradient_descent(x, y, learning_rate, epochs)
print("Slope (m):", m)
print("Intercept (b):", b)

In this implementation:

    The gradient_descent() function takes input features x, target values y, learning rate, and the number of epochs as parameters.
    It initializes the slope m and intercept b to zero.
    It iterates through the specified number of epochs and calculates the gradients for the slope and intercept.
    It updates the parameters m and b using the gradients and learning rate.
    Finally, it returns the updated slope and intercept.

This implementation performs gradient descent to find the best-fitting line (slope and intercept) for the given input-output data points.
