#include "fastFourierTransform.h"
#include <iostream>
#include <vector>
#include <complex>

std::vector<std::complex<double>> FastFourierTransform::computeFFT(const std::vector<std::complex<double>>& signal) {
    return fft(signal);
}

std::vector<std::complex<double>> FastFourierTransform::fft(const std::vector<std::complex<double>>& signal) {
    int n = signal.size();
    if (n <= 1) {
        return signal;
    }

    // Divide the signal into even and odd parts
    std::vector<std::complex<double>> even, odd;
    for (int i = 0; i < n; i += 2) {
        even.push_back(signal[i]);
        odd.push_back(signal[i + 1]);
    }

    // Compute the twiddle factors
    std::vector<std::complex<double>> twiddles;
    for (int k = 0; k < n / 2; ++k) {
        double theta = -2 * M_PI * k / n;
        twiddles.push_back(std::polar(1.0, theta));
    }

    // Combine the results
    std::vector<std::complex<double>> fftSignal(n);
    for (int k = 0; k < n / 2; ++k) {
        fftSignal[k] = even[k] + twiddles[k] * odd[k];
        fftSignal[k + n / 2] = even[k] - twiddles[k] * odd[k];
    }

    return fftSignal;
}
