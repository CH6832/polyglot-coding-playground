#include <iostream>
#include <vector>
#include <complex>
#include "fastFourierTransform.h"

int main() {
    // Example: Compute the FFT of a signal
    std::vector<std::complex<double>> signal = {0, 1, 2, 3, 4, 5, 6, 7};
    std::vector<std::complex<double>> fftResult = FastFourierTransform::computeFFT(signal);
    std::cout << "FFT of the signal: ";
    for (const auto& value : fftResult) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}
