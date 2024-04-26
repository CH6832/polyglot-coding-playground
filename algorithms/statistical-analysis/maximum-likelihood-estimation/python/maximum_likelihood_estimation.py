#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""maximum_likelihood_estimation.py

    Likelihood Function: The likelihood function computes the probability of observing the given data for a given set of model parameters. In this implementation, we assume a normal distribution and use the probability density function (PDF) to calculate the likelihood value.

    Maximum Likelihood Estimation: The maximum_likelihood_estimation function performs maximum likelihood estimation to estimate the parameters of the statistical model. It uses optimization techniques to minimize the negative log-likelihood function, which is equivalent to maximizing the likelihood.

    Output: The function returns the estimated parameters of the statistical model, which represent the mean and standard deviation of the assumed normal distribution.

    Example Usage: In the example usage, we demonstrate how to estimate the parameters (mean and standard deviation) of a normal distribution using maximum likelihood estimation. We provide a list of observed data points and call the maximum_likelihood_estimation function to obtain the estimated parameters. The estimated parameters are printed for verification. Adjustments to the observed data and initial guess for the parameters can be made based on the specific problem being solved.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List
import numpy as np
from scipy.optimize import minimize


def main() -> None:
    """Driving code and main function"""
    # Example: Estimate parameters using maximum likelihood estimation
    observed_data = [1.2, 1.5, 2.0, 2.2, 2.8]
    estimated_params = maximum_likelihood_estimation(observed_data)
    print("Estimated parameters (mean, standard deviation):", estimated_params)
 
    return None


def likelihood_function(params: List[float], data: List[float]) -> float:
    """Compute the likelihood function for the given parameters and data.

    Args:
        params (List[float]): The parameters of the statistical model.
        data (List[float]): The observed data.

    Returns:
        float: The likelihood value.
    """
    # Calculate the likelihood value using the probability density function (PDF)
    mu, sigma = params
    likelihood = np.prod(1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * ((data - mu) / sigma) ** 2))
    return -likelihood  # Minimize negative likelihood (equivalent to maximizing likelihood)

def maximum_likelihood_estimation(data: List[float], initial_guess: List[float] = [0, 1]) -> List[float]:
    """Perform maximum likelihood estimation to estimate the parameters of the statistical model.

    Args:
        data (List[float]): The observed data.
        initial_guess (List[float], optional): Initial guess for the parameters. Defaults to [0, 1].

    Returns:
        List[float]: The estimated parameters of the statistical model.
    """
    # Minimize the negative log-likelihood function using optimization
    result = minimize(likelihood_function, initial_guess, args=(data,), method='Nelder-Mead')
    return result.x


if __name__ == '__main__':
    main()

