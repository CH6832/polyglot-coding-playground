import java.util.ArrayList;
import java.util.List;
import Complex;

public class FFT {
    public static List<Complex> computeFFT(List<Complex> signal) {
        return fft(signal);
    }

    private static List<Complex> fft(List<Complex> signal) {
        int n = signal.size();
        if (n <= 1) {
            return signal;
        }

        // Divide the signal into even and odd parts
        List<Complex> even = new ArrayList<>();
        List<Complex> odd = new ArrayList<>();
        for (int i = 0; i < n; i += 2) {
            even.add(signal.get(i));
            odd.add(signal.get(i + 1));
        }

        // Compute the twiddle factors
        List<Complex> twiddles = new ArrayList<>();
        for (int k = 0; k < n / 2; ++k) {
            double theta = -2 * Math.PI * k / n;
            twiddles.add(new Complex(Math.cos(theta), Math.sin(theta)));
        }

        // Combine the results
        List<Complex> fftSignal = new ArrayList<>(n);
        for (int k = 0; k < n / 2; ++k) {
            fftSignal.add(even.get(k).add(twiddles.get(k).multiply(odd.get(k))));
            fftSignal.add(even.get(k).subtract(twiddles.get(k).multiply(odd.get(k))));
        }

        return fftSignal;
    }
}
