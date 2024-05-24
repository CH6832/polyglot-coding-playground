import java.util.Arrays;

/**
 * QR_Decomposition.java
 *
 * QR decomposition is a method used to factorize a matrix into the product of an orthogonal matrix (Q) and an upper
 * triangular matrix (R). Given a matrix A, the QR decomposition algorithm performs the following steps:
 *
 * 1. Initialization: Start with the identity matrix for Q and a copy of A for R.
 * 2. Householder Reflections: Use Householder reflections to transform the matrix A into an upper triangular form R
 *    while simultaneously accumulating the orthogonal matrix Q.
 * 3. Iterative Update: Iterate over each column k of A. Compute the Householder vector v, which defines a reflection
 *    transformation that zeros out the elements below the diagonal in column k of R. Apply the Householder
 *    transformation to update R and accumulate the orthogonal matrix Q.
 * 4. Result: Return the orthogonal matrix Q and the upper triangular matrix R.
 *
 * Example Usage: In the main method, an example usage of the qrDecomposition function is provided. We define a matrix
 * A, and then call the qrDecomposition function to compute the QR decomposition. Finally, we print the orthogonal
 * matrix Q and the upper triangular matrix R.
 */

public class QR_Decomposition {

    /**
     * Main method for driving code and example usage of QR decomposition.
     */
    public static void main(String[] args) {
        // Example: QR decomposition
        double[][] A = {{1, -1, 4}, {2, 3, 1}, {3, 1, 2}};

        double[][] Q = new double[A.length][A.length];
        double[][] R = new double[A.length][A[0].length];

        qrDecomposition(A, Q, R);

        System.out.println("Orthogonal matrix (Q):");
        printMatrix(Q);
        System.out.println("Upper triangular matrix (R):");
        printMatrix(R);
    }

    /**
     * Perform QR decomposition of a matrix.
     *
     * @param A Matrix to decompose.
     * @param Q Orthogonal matrix Q (output parameter).
     * @param R Upper triangular matrix R (output parameter).
     */
    public static void qrDecomposition(double[][] A, double[][] Q, double[][] R) {
        int m = A.length;
        int n = A[0].length;

        for (int k = 0; k < n; k++) {
            double[] x = new double[m - k];
            double[] v = new double[m - k];
            for (int i = k; i < m; i++) {
                x[i - k] = A[i][k];
            }

            double normX = 0;
            for (double value : x) {
                normX += value * value;
            }
            normX = Math.sqrt(normX);
            v[0] = x[0] < 0 ? x[0] - normX : x[0] + normX;
            double normV = 0;
            for (double value : v) {
                normV += value * value;
            }
            normV = Math.sqrt(normV);
            for (int i = 0; i < v.length; i++) {
                v[i] /= normV;
            }

            double[][] Qk = new double[m][m];
            for (int i = 0; i < m; i++) {
                Qk[i][i] = 1;
            }
            for (int i = 0; i < v.length; i++) {
                for (int j = 0; j < v.length; j++) {
                    Qk[i + k][j + k] -= 2 * v[i] * v[j];
                }
            }

            double[][] Ak = new double[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    double sum = 0;
                    for (int l = 0; l < m; l++) {
                        sum += Qk[i][l] * A[l][j];
                    }
                    Ak[i][j] = sum;
                }
            }
            for (int i = 0; i < m; i++) {
                System.arraycopy(Ak[i], 0, A[i], 0, n);
            }

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    R[i][j] = i <= j ? Ak[i][j] : 0;
                }
            }

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < m; j++) {
                    double sum = 0;
                    for (int l = 0; l < m; l++) {
                        sum += Q[i][l] * Qk[l][j];
                    }
                    Q[i][j] = sum;
                }
            }
        }
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
