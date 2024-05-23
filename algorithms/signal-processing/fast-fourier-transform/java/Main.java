import java.util.List;
import java.util.ArrayList;
import Complex;

public class Main {
    public static void main(String[] args) {
        // Example: Compute the FFT of a signal
        List<Complex> signal = new ArrayList<>();
        signal.add(new Complex(0, 0));
        signal.add(new Complex(1, 0));
        signal.add(new Complex(2, 0));
        signal.add(new Complex(3, 0));
        signal.add(new Complex(4, 0));
        signal.add(new Complex(5, 0));
        signal.add(new Complex(6, 0));
        signal.add(new Complex(7, 0));

        List<Complex> fftResult = FFT.computeFFT(signal);
        System.out.print("FFT of the signal: ");
        for (Complex value : fftResult) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
