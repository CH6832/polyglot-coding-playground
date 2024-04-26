#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""travelling_salesman_problem.py

Euler's method is a numerical technique used to approximate the solution of ordinary differential equations
(ODEs). Given an initial condition and the derivative of the function with respect to the independent
variable, Euler's method iteratively calculates the value of the function at discrete points.

    euler_method function: This function takes four arguments:
        func: The first-order ODE in the form dy/dx = f(x, y), provided as a callable function.
        initial_values: Tuple containing the initial value of x and y.
        step_size: The step size (or time increment) h.
        num_steps: The number of steps to take.

    Approximating the solution: Inside the euler_method function, Euler's method iteratively calculates the
    value of y at each step by updating it according to the slope of the function at the current point.
    It then updates the value of x and appends both x and y values to their respective lists.

    Example usage: In the if __name__ == "__main__": block, an example usage of Euler's method is provided
    to solve the first-order ODE y' = x + y with the initial condition y(0) = 1. The function func defines
    the ODE, and the initial values, step size, and number of steps are specified. The result is then
    printed, showing the approximate solution at each step.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import Callable, Tuple


def main() -> None:
    """Driving code and main function"""
   # Example: Solve the first-order ODE y' = x + y with initial condition y(0) = 1
    def func(x: float, y: float) -> float:
        """The first-order ODE: y' = x + y."""
        return x + y

    initial_values = (0, 1)  # Initial condition: y(0) = 1
    step_size = 0.1  # Step size h
    num_steps = 100  # Number of steps

    x_values, y_values = euler_method(func, initial_values, step_size, num_steps)

    # Print the approximate solution
    print("Approximate solution using Euler's method:")
    for x, y in zip(x_values, y_values):
        print(f"x = {x}, y = {y}")
 
    return None


def euler_method(func: Callable[[float, float], float], initial_values: Tuple[float, float], 
                 step_size: float, num_steps: int) -> Tuple[list, list]:
    """Approximate the solution of a first-order ordinary differential equation (ODE) 
    using Euler's method.

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
        slope = func(x, y)
        y += step_size * slope
        x += step_size

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


if __name__ == '__main__':
    main()

