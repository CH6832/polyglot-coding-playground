#ifndef FAST_FOURIER_TRANSFORM_H
#define FAST_FOURIER_TRANSFORM_H

#include <vector>
#include <complex>

class FastFourierTransform {
public:
    // Public interface
    static std::vector<std::complex<double>> computeFFT(const std::vector<std::complex<double>>& signal);

private:
    // Private helper functions
    static std::vector<std::complex<double>> fft(const std::vector<std::complex<double>>& signal);
};

#endif
