#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

The Runge-Kutta method is a numerical technique used to approximate the solution of ordinary differential equations (ODEs). It is a higher-order method compared to Euler's method and provides more accurate results.

    runge_kutta function: This function takes four arguments:
        func: The first-order ODE in the form dy/dx = f(x, y), provided as a callable function.
        initial_values: Tuple containing the initial value of x and y.
        step_size: The step size (or time increment) h.
        num_steps: The number of steps to take.

    Approximating the solution: Inside the runge_kutta function, the Runge-Kutta method calculates the value of y at each step by using a weighted average of several slope estimates calculated at different points within the step. It then updates the value of x and appends both x and y values to their respective lists.

    Example usage: In the if __name__ == "__main__": block, an example usage of the Runge-Kutta method is provided to solve the first-order ODE y' = x + y with the initial condition y(0) = 1. The function func defines the ODE, and the initial values, step size, and number of steps are specified. The result is then printed, showing the approximate solution at each step.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List, Callable, Tuple

V = 4


def main() -> None:
    """Driving code and main function"""
    def func(x: float, y: float) -> float:
        """The first-order ODE: y' = x + y."""
        return x + y

    initial_values = (0, 1)  # Initial condition: y(0) = 1
    step_size = 0.1  # Step size h
    num_steps = 100  # Number of steps

    x_values, y_values = runge_kutta(func, initial_values, step_size, num_steps)

    # Print the approximate solution
    print("Approximate solution using Runge-Kutta method:")
    for x, y in zip(x_values, y_values):
        print(f"x = {x}, y = {y}")
 
    return None


def runge_kutta(func: Callable[[float, float], float], initial_values: Tuple[float, float],
                step_size: float, num_steps: int) -> Tuple[list, list]:
    """Approximate the solution of a first-order ordinary differential equation (ODE) 
    using the Runge-Kutta method.

    Args:
        func (Callable[[float, float], float]): The first-order ODE in the form dy/dx = f(x, y).
        initial_values (Tuple[float, float]): Tuple containing the initial value of x and y.
        step_size (float): The step size (or time increment) h.
        num_steps (int): The number of steps to take.

    Returns:
        Tuple[list, list]: Two lists containing the values of x and y at each step.
    """
    x_values = [initial_values[0]]
    y_values = [initial_values[1]]

    x = initial_values[0]
    y = initial_values[1]

    for _ in range(num_steps):
        k1 = func(x, y)
        k2 = func(x + step_size / 2, y + (step_size / 2) * k1)
        k3 = func(x + step_size / 2, y + (step_size / 2) * k2)
        k4 = func(x + step_size, y + step_size * k3)

        y += (step_size / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += step_size

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


if __name__ == '__main__':
    main()

