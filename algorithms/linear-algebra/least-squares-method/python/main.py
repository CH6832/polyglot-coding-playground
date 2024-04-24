Here's a basic implementation of the Least Squares Method in Python without using any third-party libraries:

python

def least_squares_method(x, y):
    n = len(x)

    # Calculate the mean of x and y
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Calculate the coefficients
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x)**2 for i in range(n))
    b1 = numerator / denominator
    b0 = mean_y - b1 * mean_x

    return b0, b1

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

b0, b1 = least_squares_method(x, y)
print("Intercept (b0):", b0)
print("Slope (b1):", b1)

In this implementation:

    The least_squares_method() function takes two lists x and y representing the input features and target values, respectively.
    It calculates the coefficients of the linear regression model using the least squares method.
    First, it computes the mean of x and y.
    Then, it calculates the slope b1 and intercept b0 using the formulas derived from the least squares method.
    Finally, it returns the calculated coefficients.

This implementation provides a basic way to perform linear regression using the least squares method without relying on any third-party libraries.