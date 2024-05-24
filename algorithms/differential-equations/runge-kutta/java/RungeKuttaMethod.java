import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;

/**
 * Main class to demonstrate the Runge-Kutta method.
 */
public class RungeKuttaMethod {
    public static void main(String[] args) {
        // Example: Solve the first-order ODE y' = x + y with initial condition y(0) = 1
        BiFunction<Double, Double, Double> func = (x, y) -> x + y;

        double initialX = 0.0; // Initial value of x
        double initialY = 1.0; // Initial value of y
        double stepSize = 0.1; // Step size h
        int numSteps = 100; // Number of steps

        List<Double> xValues = new ArrayList<>();
        List<Double> yValues = new ArrayList<>();

        rungeKutta(func, initialX, initialY, stepSize, numSteps, xValues, yValues);

        // Print the approximate solution
        System.out.println("Approximate solution using Runge-Kutta method:");
        for (int i = 0; i < xValues.size(); i++) {
            System.out.println("x = " + xValues.get(i) + ", y = " + yValues.get(i));
        }
    }

    /**
     * Approximate the solution of a first-order ordinary differential equation (ODE)
     * using the Runge-Kutta method.
     *
     * @param func        The first-order ODE in the form dy/dx = f(x, y).
     * @param initialX    The initial value of x.
     * @param initialY    The initial value of y.
     * @param stepSize    The step size (or time increment) h.
     * @param numSteps    The number of steps to take.
     * @param xValues     List to store the values of x at each step.
     * @param yValues     List to store the values of y at each step.
     */
    public static void rungeKutta(BiFunction<Double, Double, Double> func,
                                  double initialX, double initialY,
                                  double stepSize, int numSteps,
                                  List<Double> xValues, List<Double> yValues) {
        double x = initialX;
        double y = initialY;

        xValues.add(x);
        yValues.add(y);

        for (int i = 0; i < numSteps; i++) {
            double k1 = func.apply(x, y);
            double k2 = func.apply(x + stepSize / 2, y + (stepSize / 2) * k1);
            double k3 = func.apply(x + stepSize / 2, y + (stepSize / 2) * k2);
            double k4 = func.apply(x + stepSize, y + stepSize * k3);

            y += (stepSize / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
            x += stepSize;

            xValues.add(x);
            yValues.add(y);
        }
    }
}
