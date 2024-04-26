#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""bayesian_inference.py

    Bayes' Theorem: Bayesian inference is based on Bayes' theorem, which states that the posterior probability of a hypothesis given new evidence is proportional to the product of the prior probability of the hypothesis and the likelihood of the evidence given the hypothesis, divided by the evidence.

    Input Parameters: The function bayesian_inference takes two dictionaries as input parameters:
        priors: A dictionary mapping hypothesis names to their prior probabilities.
        likelihoods: A dictionary mapping hypothesis names to lists of likelihoods for different pieces of evidence.

    Updating Probabilities: The function computes the updated probabilities of each hypothesis using Bayes' theorem. It iterates over each hypothesis, calculates the numerator of Bayes' theorem (prior * likelihood), and divides it by the evidence to obtain the updated probability.

    Example Usage: In the example usage, we demonstrate how to perform Bayesian inference with given priors and likelihoods. We call the bayesian_inference function with the provided inputs and print the updated probabilities for each hypothesis. Adjustments to the priors and likelihoods can be made based on the specific problem being solved.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from sys import maxsize
from itertools import permutations
from typing import List

V = 4


def main() -> None:
    """Driving code and main function"""
    # Example: Perform Bayesian inference with given priors and likelihoods
    priors = {"Hypothesis A": 0.3, "Hypothesis B": 0.7}
    likelihoods = {"Hypothesis A": [0.8, 0.2], "Hypothesis B": [0.4, 0.6]}
    updated_probs = bayesian_inference(priors, likelihoods)
    print("Updated probabilities after Bayesian inference:")
    for hypothesis, probability in updated_probs.items():
        print(f"{hypothesis}: {probability}")
 
    return None


def bayesian_inference(priors: Dict[str, float], likelihoods: Dict[str, List[float]]) -> Dict[str, float]:
    """Perform Bayesian inference to update priors based on likelihoods.

    Args:
        priors (Dict[str, float]): A dictionary mapping hypothesis names to their prior probabilities.
        likelihoods (Dict[str, List[float]]): A dictionary mapping hypothesis names to lists of likelihoods.

    Returns:
        Dict[str, float]: A dictionary mapping hypothesis names to their updated probabilities.
    """
    updated_probs = {}

    # Compute the denominator (evidence) by summing the products of priors and likelihoods
    evidence = sum(priors[h] * l for h, l in likelihoods.items())

    # Update the probabilities of each hypothesis using Bayes' theorem
    for hypothesis, prior in priors.items():
        likelihood = likelihoods[hypothesis]
        updated_probs[hypothesis] = (prior * likelihood) / evidence

    return updated_probs


if __name__ == '__main__':
    main()

