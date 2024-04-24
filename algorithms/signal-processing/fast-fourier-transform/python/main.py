Implementing the Fast Fourier Transform (FFT) algorithm from scratch is quite complex, but I can provide you with a simplified version of the Cooley-Tukey FFT algorithm, which is one of the most commonly used FFT algorithms. Here's a basic implementation in Python:

python

import cmath

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

def ifft(X):
    N = len(X)
    if N <= 1:
        return X
    even = ifft(X[0::2])
    odd = ifft(X[1::2])
    T = [cmath.exp(2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

# Example usage:
x = [0, 1, 2, 3]
X = fft(x)
print("FFT:", X)

# Inverse FFT (IFFT)
x_reconstructed = ifft(X)
print("Reconstructed:", x_reconstructed)

This implementation recursively applies the FFT algorithm to divide the input sequence into smaller subproblems until the base case of size 1 is reached. It then combines the results of the smaller subproblems to compute the FFT of the entire input sequence. The ifft() function is the inverse FFT, which computes the original sequence from its frequency-domain representation.