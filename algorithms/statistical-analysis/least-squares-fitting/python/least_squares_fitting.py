#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""least_squares_fitting.py

    Vandermonde Matrix: The first step in the least squares fitting algorithm is to create the Vandermonde matrix, which is a matrix of powers of the input x-values. Each row of the matrix corresponds to a data point, and each column corresponds to a power of x.

    Least Squares Fitting: The least squares fitting is performed using the numpy.linalg.lstsq function, which calculates the coefficients of the polynomial curve that minimizes the sum of the squares of the differences between the observed y-values and the predicted y-values.

    Output: The function returns two arrays:
        coefficients: An array of coefficients of the polynomial curve, where the coefficients are in descending order of powers (highest power first).
        residuals: An array of residuals, which represent the errors between the observed and predicted y-values.

    Example Usage: In the example usage, we demonstrate how to fit a polynomial curve of degree 2 to a set of data points with given x and y values. We call the least_squares_fit function with the provided inputs and print the coefficients of the polynomial curve and the residuals. Adjustments to the x and y values, as well as the degree of the polynomial curve, can be made based on the specific problem being solved.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List, Tuple
import numpy as np


def main() -> None:
    """Driving code and main function"""
    # Example: Fit a polynomial curve to a set of data points
    x_values = [1, 2, 3, 4, 5]
    y_values = [2.3, 3.5, 4.2, 5.0, 6.1]
    degree = 2
    coefficients, residuals = least_squares_fit(x_values, y_values, degree)
    print("Coefficients of the polynomial curve:", coefficients)
    print("Residuals (errors):", residuals)
 
    return None


def least_squares_fit(x_values: List[float], y_values: List[float], degree: int) -> Tuple[np.ndarray, np.ndarray]:
    """Perform least squares fitting to find the coefficients of the polynomial curve.

    Args:
        x_values (List[float]): The x-coordinates of the data points.
        y_values (List[float]): The y-coordinates of the data points.
        degree (int): The degree of the polynomial curve to fit.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing the coefficients of the polynomial curve.
            The first element is an array of coefficients in descending order of powers (highest power first).
            The second element is an array of residuals (errors).
    """
    # Create the Vandermonde matrix
    X = np.vander(x_values, degree + 1, increasing=True)

    # Perform least squares fitting
    coefficients, residuals, _, _ = np.linalg.lstsq(X, y_values, rcond=None)

    return coefficients, residuals


if __name__ == '__main__':
    main()

