Here's a basic implementation of the fourth-order Runge-Kutta method in Python without using any third-party libraries:

python

def runge_kutta_method(f, y0, t0, tn, h):
    num_steps = int((tn - t0) / h)  # Calculate number of steps
    t_values = [t0 + i * h for i in range(num_steps + 1)]  # Generate time values
    y_values = [y0]  # Initialize list to store solution

    # Iterate through each time step
    for i in range(1, num_steps + 1):
        t_prev = t_values[i - 1]
        y_prev = y_values[i - 1]

        # Compute Runge-Kutta coefficients
        k1 = h * f(t_prev, y_prev)
        k2 = h * f(t_prev + h/2, y_prev + k1/2)
        k3 = h * f(t_prev + h/2, y_prev + k2/2)
        k4 = h * f(t_prev + h, y_prev + k3)

        # Compute next solution value using weighted average of the coefficients
        y_next = y_prev + (k1 + 2*k2 + 2*k3 + k4) / 6

        # Store the next solution value
        y_values.append(y_next)

    return t_values, y_values

# Example usage:
def f(t, y):
    return y - t**2 + 1  # Example ODE dy/dt = y - t^2 + 1

y0 = 0.5  # Initial condition
t0 = 0    # Initial time
tn = 2    # End time
h = 0.2   # Step size

t_values, y_values = runge_kutta_method(f, y0, t0, tn, h)
for t, y in zip(t_values, y_values):
    print(f"t = {t}, y = {y}")

In this implementation:

    The runge_kutta_method() function takes the function f(t, y) representing the ordinary differential equation (ODE), initial condition y0, initial time t0, end time tn, and step size h as input.
    It calculates the number of steps based on the given time range and step size and generates a list of time values.
    It iterates through each time step and computes the Runge-Kutta coefficients k1, k2, k3, and k4.
    It computes the next solution value using a weighted average of these coefficients.
    The solution values are stored in a list and returned.

This implementation provides a basic way to solve ordinary differential equations using the fourth-order Runge-Kutta method without relying on any third-party libraries.