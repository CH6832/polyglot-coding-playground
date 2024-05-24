#include <iostream>
#include <vector>
#include <functional>

/**
 * @brief Approximates the solution of a first-order ordinary differential equation (ODE) using Euler's method.
 * 
 * @param func The first-order ODE in the form dy/dx = f(x, y), provided as a callable function.
 * @param initial_values Tuple containing the initial value of x and y.
 * @param step_size The step size (or time increment) h.
 * @param num_steps The number of steps to take.
 * @return A pair of vectors containing the values of x and y at each step.
 */
std::pair<std::vector<double>, std::vector<double>> euler_method(
    std::function<double(double, double)> func, 
    std::pair<double, double> initial_values, 
    double step_size, 
    int num_steps) 
{
    std::vector<double> x_values;
    std::vector<double> y_values;
    x_values.push_back(initial_values.first);
    y_values.push_back(initial_values.second);

    double x = initial_values.first;
    double y = initial_values.second;

    for (int i = 0; i < num_steps; ++i) {
        double slope = func(x, y);
        y += step_size * slope;
        x += step_size;
        x_values.push_back(x);
        y_values.push_back(y);
    }

    return {x_values, y_values};
}

int main() {
    // Example: Solve the first-order ODE y' = x + y with initial condition y(0) = 1
    auto func = [](double x, double y) -> double {
        return x + y;
    };

    std::pair<double, double> initial_values = {0.0, 1.0};  // Initial condition: y(0) = 1
    double step_size = 0.1;  // Step size h
    int num_steps = 100;  // Number of steps

    auto result = euler_method(func, initial_values, step_size, num_steps);

    // Print the approximate solution
    std::cout << "Approximate solution using Euler's method:" << std::endl;
    for (size_t i = 0; i < result.first.size(); ++i) {
        std::cout << "x = " << result.first[i] << ", y = " << result.second[i] << std::endl;
    }

    return 0;
}
