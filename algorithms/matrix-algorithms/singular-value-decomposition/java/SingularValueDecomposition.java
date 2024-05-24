import java.util.Arrays;

/**
 * SingularValueDecomposition.java
 *
 * Singular Value Decomposition (SVD) is a matrix factorization technique that decomposes a matrix into three matrices:
 * U, S, and V^T, where U and V are orthogonal matrices and S is a diagonal matrix containing the singular values of the
 * original matrix.
 *
 * Initialization: Given a matrix A, we compute its SVD using Java's built-in libraries.
 * Result: The function returns three matrices: U, S, and V^T. U contains the left singular vectors, S contains the singular
 * values as a diagonal matrix, and V^T contains the right singular vectors (transpose of V).
 *
 * Example Usage: In the main method, an example usage of the svd function is provided. We define a matrix A, and then
 * call the svd function to compute its SVD. Finally, we print the left singular vectors (U), singular values (S), and
 * right singular vectors (V^T).
 */
public class SingularValueDecomposition {

    /**
     * Main method for driving code and example usage of SVD.
     */
    public static void main(String[] args) {
        // Example: Singular Value Decomposition (SVD)
        double[][] A = {{1, 2}, {3, 4}, {5, 6}};

        double[][] U = new double[A.length][A.length];
        double[][] S = new double[A.length][A[0].length];
        double[][] Vt = new double[A[0].length][A[0].length];

        svd(A, U, S, Vt);

        System.out.println("Left singular vectors (U):");
        printMatrix(U);
        System.out.println("Singular values (S):");
        printMatrix(S);
        System.out.println("Right singular vectors (V^T):");
        printMatrix(Vt);
    }

    /**
     * Perform Singular Value Decomposition (SVD) of a matrix.
     *
     * @param A Matrix to decompose.
     * @param U Left singular vectors (output parameter).
     * @param S Singular values (output parameter).
     * @param Vt Right singular vectors (transpose of V) (output parameter).
     */
    public static void svd(double[][] A, double[][] U, double[][] S, double[][] Vt) {
        Jama.Matrix matrix = new Jama.Matrix(A);
        Jama.SingularValueDecomposition svd = matrix.svd();
        Jama.Matrix UMatrix = svd.getU();
        Jama.Matrix SMatrix = svd.getS();
        Jama.Matrix VtMatrix = svd.getV().transpose();

        // Copy U matrix
        for (int i = 0; i < U.length; i++) {
            for (int j = 0; j < U[i].length; j++) {
                U[i][j] = UMatrix.get(i, j);
            }
        }

        // Copy S matrix
        for (int i = 0; i < S.length; i++) {
            for (int j = 0; j < S[i].length; j++) {
                S[i][j] = (i == j) ? SMatrix.get(i, j) : 0;
            }
        }

        // Copy Vt matrix
        for (int i = 0; i < Vt.length; i++) {
            for (int j = 0; j < Vt[i].length; j++) {
                Vt[i][j] = VtMatrix.get(i, j);
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
