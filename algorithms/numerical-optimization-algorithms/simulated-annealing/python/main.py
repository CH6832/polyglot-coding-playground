Here's a basic implementation of the Simulated Annealing algorithm in Python without using any third-party libraries beyond the standard library:

python

import math
import random

def simulated_annealing(f, initial_state, temperature, cooling_rate, max_iter):
    current_state = initial_state
    current_energy = f(current_state)

    for i in range(max_iter):
        # Annealing schedule
        T = temperature / (1 + i)
        
        # Generate a new candidate state
        new_state = [current_state[j] + random.uniform(-0.1, 0.1) for j in range(len(current_state))]
        new_energy = f(new_state)

        # Acceptance probability
        delta_energy = new_energy - current_energy
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / T):
            current_state = new_state
            current_energy = new_energy

    return current_state

# Example usage:
def quadratic(x):
    return sum(x_i ** 2 for x_i in x)

initial_state = [1, 1]  # Initial state
temperature = 100        # Initial temperature
cooling_rate = 0.01      # Cooling rate
max_iter = 1000          # Maximum number of iterations

optimal_solution = simulated_annealing(quadratic, initial_state, temperature, cooling_rate, max_iter)
print("Optimal solution:", optimal_solution)
print("Minimum value:", quadratic(optimal_solution))

In this implementation:

    The simulated_annealing() function takes a function f to minimize, an initial state initial_state, initial temperature temperature, cooling rate cooling_rate, and maximum number of iterations max_iter.
    It iteratively generates new candidate states and decides whether to accept them based on the acceptance probability, which depends on the energy difference between the current state and the new state, and the current temperature.
    The algorithm simulates the annealing process, gradually reducing the temperature according to the cooling rate.
    The function returns the approximate optimal solution found after the specified number of iterations.

This implementation provides a basic way to minimize a function using the Simulated Annealing algorithm with minimal reliance on third-party libraries.