import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;

/**
 * Approximates the solution of a first-order ordinary differential equation (ODE) using Euler's method.
 * 
 * @param func The first-order ODE in the form dy/dx = f(x, y), provided as a callable function.
 * @param initialValues Tuple containing the initial value of x and y.
 * @param stepSize The step size (or time increment) h.
 * @param numSteps The number of steps to take.
 * @return A pair of lists containing the values of x and y at each step.
 */
public class EulerMethod {
    public static Pair<List<Double>, List<Double>> eulerMethod(
            BiFunction<Double, Double, Double> func, 
            Pair<Double, Double> initialValues, 
            double stepSize, 
            int numSteps) {
        
        List<Double> xValues = new ArrayList<>();
        List<Double> yValues = new ArrayList<>();
        xValues.add(initialValues.getKey());
        yValues.add(initialValues.getValue());

        double x = initialValues.getKey();
        double y = initialValues.getValue();

        for (int i = 0; i < numSteps; ++i) {
            double slope = func.apply(x, y);
            y += stepSize * slope;
            x += stepSize;
            xValues.add(x);
            yValues.add(y);
        }

        return new Pair<>(xValues, yValues);
    }

    public static void main(String[] args) {
        // Example: Solve the first-order ODE y' = x + y with initial condition y(0) = 1
        BiFunction<Double, Double, Double> func = (x, y) -> x + y;

        Pair<Double, Double> initialValues = new Pair<>(0.0, 1.0);  // Initial condition: y(0) = 1
        double stepSize = 0.1;  // Step size h
        int numSteps = 100;  // Number of steps

        Pair<List<Double>, List<Double>> result = eulerMethod(func, initialValues, stepSize, numSteps);

        // Print the approximate solution
        System.out.println("Approximate solution using Euler's method:");
        for (int i = 0; i < result.getKey().size(); ++i) {
            System.out.printf("x = %.2f, y = %.2f%n", result.getKey().get(i), result.getValue().get(i));
        }
    }
}

class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() {
        return key;
    }

    public V getValue() {
        return value;
    }
}
