Sure, here's a basic example of Monte Carlo simulation for estimating the value of π without using any third-party libraries:

python

import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        # Generate random x and y coordinates in the range [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Estimate pi based on the ratio of points inside the circle to the total points
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

# Example usage:
num_samples = 1000000  # Number of samples
pi_estimate = estimate_pi(num_samples)
print("Estimated value of pi:", pi_estimate)

In this implementation:

    The estimate_pi() function takes the number of samples as input and performs a Monte Carlo simulation to estimate the value of π.
    It generates random points (x, y) within the range [-1, 1] and counts the number of points that fall within the unit circle (i.e., satisfy the condition x**2 + y**2 <= 1).
    The estimated value of π is calculated based on the ratio of points inside the circle to the total number of points, multiplied by 4 (since we're working within the unit square).
    Finally, the estimated value of π is returned.

This approach provides a simple yet effective way to approximate the value of π using random sampling. The accuracy of the estimate improves as the number of samples increases.
