import java.util.Arrays;

/**
 * LU_Decomposition.java
 *
 * LU decomposition (also known as LU factorization) is a method used to factorize
 * a square matrix into the product of a lower triangular matrix (L) and an upper
 * triangular matrix (U). Given a matrix A, the LU decomposition algorithm performs
 * the following steps:
 *
 * 1. Initialization: Start with the identity matrix for L and a copy of A for U.
 * 2. Gaussian Elimination: Perform Gaussian elimination to transform the matrix A
 *    into an upper triangular form U while simultaneously computing the multipliers
 *    used to create the lower triangular matrix L.
 * 3. Iterative Update: Iterate over each column k (except the last one) and each
 *    row i below the diagonal. Compute the factor by dividing the element U[i][k] by
 *    the pivot element U[k][k]. Update the corresponding element in L and perform row
 *    operations to eliminate the elements below the diagonal in column k of U.
 * 4. Result: Return the lower triangular matrix L and the upper triangular matrix U.
 *
 * Example Usage: In the main method, an example usage of the luDecomposition function
 * is provided. We define a square matrix A, and then call the luDecomposition function
 * to compute the LU decomposition. Finally, we print the lower triangular matrix L and
 * the upper triangular matrix U.
 */

public class LU_Decomposition {

    /**
     * Main method for driving code and example usage of LU decomposition.
     */
    public static void main(String[] args) {
        // Example: LU decomposition
        double[][] A = {{2, -1, 0}, {-1, 2, -1}, {0, -1, 2}};

        double[][][] LU = luDecomposition(A);
        double[][] L = LU[0];
        double[][] U = LU[1];

        System.out.println("Lower triangular matrix (L):");
        printMatrix(L);
        System.out.println("Upper triangular matrix (U):");
        printMatrix(U);
    }

    /**
     * Perform LU decomposition of a square matrix.
     *
     * @param A Square matrix to decompose.
     * @return A 3D array containing the lower triangular matrix (L) and the upper
     *         triangular matrix (U).
     */
    public static double[][][] luDecomposition(double[][] A) {
        int n = A.length;
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];

        // Initialize L as identity matrix and U as a copy of A
        for (int i = 0; i < n; i++) {
            L[i][i] = 1;
            System.arraycopy(A[i], 0, U[i], 0, n);
        }

        // Gaussian elimination to transform A into upper triangular form
        for (int k = 0; k < n - 1; k++) {
            for (int i = k + 1; i < n; i++) {
                if (U[k][k] == 0) {
                    throw new IllegalArgumentException("Matrix is singular");
                }
                double factor = U[i][k] / U[k][k];
                L[i][k] = factor;
                for (int j = k; j < n; j++) {
                    U[i][j] -= factor * U[k][j];
                }
            }
        }

        double[][][] result = {L, U};
        return result;
    }

    /**
     * Print a matrix.
     *
     * @param matrix Matrix to print.
     */
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
