#include <iostream>
#include <vector>
#include <Eigen/Dense>

/**
 * SingularValueDecomposition.cpp
 *
 * Singular Value Decomposition (SVD) is a matrix factorization technique that decomposes a matrix into three matrices:
 * U, S, and V^T, where U and V are orthogonal matrices and S is a diagonal matrix containing the singular values of the
 * original matrix.
 *
 * Initialization: Given a matrix A, we compute its SVD using Eigen library.
 * Result: The function returns three matrices: U, S, and V^T. U contains the left singular vectors, S contains the
 * singular values as a diagonal matrix, and V^T contains the right singular vectors (transpose of V).
 *
 * Example Usage: In the main function, an example usage of the svd function is provided. We define a matrix A, and then
 * call the svd function to compute its SVD. Finally, we print the left singular vectors (U), singular values (S), and
 * right singular vectors (V^T).
 */

using namespace std;

// Typedef for a matrix
typedef Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> Matrix;

/**
 * Perform Singular Value Decomposition (SVD) of a matrix.
 *
 * @param A Matrix to decompose.
 * @param U Left singular vectors (output parameter).
 * @param S Singular values (output parameter).
 * @param Vt Right singular vectors (transpose of V) (output parameter).
 */
void svd(const Matrix& A, Matrix& U, Matrix& S, Matrix& Vt) {
    Eigen::JacobiSVD<Matrix> svd(A, Eigen::ComputeThinU | Eigen::ComputeThinV);
    U = svd.matrixU();
    S = svd.singularValues().asDiagonal();
    Vt = svd.matrixV().transpose();
}

/**
 * Print a matrix.
 *
 * @param matrix Matrix to print.
 */
void printMatrix(const Matrix& matrix) {
    cout << matrix << endl;
}

int main() {
    // Example: Singular Value Decomposition (SVD)
    Matrix A(3, 2);
    A << 1, 2,
         3, 4,
         5, 6;

    Matrix U, S, Vt;
    svd(A, U, S, Vt);

    cout << "Left singular vectors (U):" << endl;
    printMatrix(U);
    cout << "Singular values (S):" << endl;
    printMatrix(S);
    cout << "Right singular vectors (V^T):" << endl;
    printMatrix(Vt);

    return 0;
}
