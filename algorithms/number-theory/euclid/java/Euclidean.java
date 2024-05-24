/**
 * Euclidean.java
 *
 * The Euclidean Algorithm is an efficient method for computing the greatest common divisor (GCD) of two integers.
 *
 * Algorithm: The algorithm repeatedly applies the property that the GCD of two numbers is the same as the GCD of the
 * smaller number and the remainder when the larger number is divided by the smaller number. It continues until the
 * remainder is zero, at which point the GCD is the remaining non-zero value.
 *
 * Implementation: The function euclideanAlgorithm takes two integers a and b as input and iterates through the algorithm
 * until b becomes zero. In each iteration, it updates a to b and b to the remainder when a is divided by b. Finally, it
 * returns the absolute value of a, which is the GCD of the two integers.
 *
 * Example Usage: In the main method, an example usage of the euclideanAlgorithm function is provided. We define two
 * integers a and b, and then call the function to compute their GCD. Finally, we print the result.
 */

 public class Euclidean {

    /**
     * Main method for driving code and example usage of Euclidean Algorithm.
     */
    public static void main(String[] args) {
        // Example: Euclidean Algorithm
        int a = 48, b = 18;
        int gcd = euclideanAlgorithm(a, b);
        System.out.println("The GCD of " + a + " and " + b + " is " + gcd + ".");
    }

    /**
     * Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
     *
     * @param a First integer.
     * @param b Second integer.
     * @return The greatest common divisor (GCD) of the two integers.
     */
    public static int euclideanAlgorithm(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return Math.abs(a);
    }
}
