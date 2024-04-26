#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fast_fourier_transform.py

The Fast Fourier Transform (FFT) algorithm is an efficient algorithm for computing the Discrete Fourier Transform (DFT) of a sequence or signal. Here's how the algorithm works:

    Divide and Conquer: The input signal is divided into two parts: even-indexed and odd-indexed elements. This process is recursively applied to each part until the base case is reached (a signal with one or zero elements).

    Compute Twiddle Factors: Twiddle factors are precomputed complex numbers that represent the rotation in the frequency domain. These factors are calculated using Euler's formula.

    Combine Results: The results from the even and odd parts are combined using the twiddle factors to form the final FFT result. This step is performed recursively until the FFT of the entire signal is computed.

    Termination: The recursion terminates when the base case is reached, and the FFT of the input signal is obtained.

In the example usage, we demonstrate how to compute the FFT of a signal using the fft function. We provide a sample signal [0, 1, 2, 3, 4, 5, 6, 7] and obtain its FFT. The result is printed for verification. Adjustments to the input signal can be made based on the specific problem being solved.

.. _PEP 0000:
    https://peps.python.org/pep-0000/
"""


from typing import List, Tuple
import cmath


def main() -> None:
    """Driving code and main function"""
    # Example: Compute the FFT of a signal
    signal = [0, 1, 2, 3, 4, 5, 6, 7]
    fft_result = fft([complex(x) for x in signal])
    print("FFT of the signal:", fft_result)
 
    return None


def fft(signal: List[complex]) -> List[complex]:
    """Compute the Fast Fourier Transform (FFT) of a given signal.

    Args:
        signal (List[complex]): The input signal in the time domain.

    Returns:
        List[complex]: The FFT of the input signal.
    """
    n = len(signal)
    if n <= 1:
        return signal

    # Divide the signal into even and odd parts
    even = fft(signal[0::2])
    odd = fft(signal[1::2])

    # Compute the twiddle factors
    twiddles = [cmath.exp(-2j * cmath.pi * k / n) for k in range(n // 2)]

    # Combine the results
    fft_signal = [0] * n
    for k in range(n // 2):
        fft_signal[k] = even[k] + twiddles[k] * odd[k]
        fft_signal[k + n // 2] = even[k] - twiddles[k] * odd[k]

    return fft_signal


if __name__ == '__main__':
    main()

