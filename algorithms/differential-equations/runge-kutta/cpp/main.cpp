#include <iostream>
#include <vector>
#include <functional>

// Function prototype for the Runge-Kutta method
std::pair<std::vector<double>, std::vector<double>> rungeKutta(
    std::function<double(double, double)> func,
    std::pair<double, double> initial_values,
    double step_size,
    int num_steps);

/**
 * @brief Main function to demonstrate the Runge-Kutta method.
 */
int main() {
    // Example: Solve the first-order ODE y' = x + y with initial condition y(0) = 1
    auto func = [](double x, double y) -> double {
        return x + y;
    };

    std::pair<double, double> initial_values = {0.0, 1.0};  // Initial condition: y(0) = 1
    double step_size = 0.1;  // Step size h
    int num_steps = 100;  // Number of steps

    auto [x_values, y_values] = rungeKutta(func, initial_values, step_size, num_steps);

    // Print the approximate solution
    std::cout << "Approximate solution using Runge-Kutta method:" << std::endl;
    for (size_t i = 0; i < x_values.size(); ++i) {
        std::cout << "x = " << x_values[i] << ", y = " << y_values[i] << std::endl;
    }

    return 0;
}

/**
 * @brief Approximate the solution of a first-order ordinary differential equation (ODE) using the Runge-Kutta method.
 * 
 * @param func The first-order ODE in the form dy/dx = f(x, y).
 * @param initial_values Tuple containing the initial value of x and y.
 * @param step_size The step size (or time increment) h.
 * @param num_steps The number of steps to take.
 * @return A pair of vectors containing the values of x and y at each step.
 */
std::pair<std::vector<double>, std::vector<double>> rungeKutta(
    std::function<double(double, double)> func,
    std::pair<double, double> initial_values,
    double step_size,
    int num_steps) {
    
    std::vector<double> x_values = {initial_values.first};
    std::vector<double> y_values = {initial_values.second};

    double x = initial_values.first;
    double y = initial_values.second;

    for (int i = 0; i < num_steps; ++i) {
        double k1 = func(x, y);
        double k2 = func(x + step_size / 2, y + (step_size / 2) * k1);
        double k3 = func(x + step_size / 2, y + (step_size / 2) * k2);
        double k4 = func(x + step_size, y + step_size * k3);

        y += (step_size / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
        x += step_size;

        x_values.push_back(x);
        y_values.push_back(y);
    }

    return {x_values, y_values};
}
