Sure, here's a basic implementation of linear regression in Python without using third-party libraries like NumPy or scikit-learn:

python

def mean(values):
    return sum(values) / float(len(values))

def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

def variance(values, mean):
    return sum([(x - mean)**2 for x in values])

def coefficients(x, y):
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return b0, b1

def linear_regression(train):
    x = [row[0] for row in train]
    y = [row[1] for row in train]
    b0, b1 = coefficients(x, y)
    return b0, b1

# Example usage:
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
b0, b1 = linear_regression(dataset)
print("Coefficients: b0=%.3f, b1=%.3f" % (b0, b1))

This implementation calculates the coefficients (intercept and slope) for a simple linear regression model using the ordinary least squares method. It defines functions to compute the mean, covariance, and variance, and then uses these functions to calculate the coefficients based on the input dataset. Finally, it applies the linear regression function to a sample dataset and prints the coefficients.