#include <iostream>
#include <vector>

/**
 * LU_Decomposition.cpp
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
 * Example Usage: In the main function, an example usage of the luDecomposition function
 * is provided. We define a square matrix A, and then call the luDecomposition function
 * to compute the LU decomposition. Finally, we print the lower triangular matrix L and
 * the upper triangular matrix U.
 */

using namespace std;

// Typedef for a matrix
typedef vector<vector<double>> Matrix;

/**
 * Perform LU decomposition of a square matrix.
 *
 * @param A Square matrix to decompose.
 * @return A pair containing the lower triangular matrix (L) and the upper triangular
 *         matrix (U).
 */
pair<Matrix, Matrix> luDecomposition(const Matrix& A) {
    int n = A.size();
    Matrix L(n, vector<double>(n, 0));
    Matrix U = A;

    // Initialize L as identity matrix and U as a copy of A
    for (int i = 0; i < n; ++i) {
        L[i][i] = 1;
    }

    // Gaussian elimination to transform A into upper triangular form
    for (int k = 0; k < n - 1; ++k) {
        for (int i = k + 1; i < n; ++i) {
            if (U[k][k] == 0) {
                throw invalid_argument("Matrix is singular");
            }
            double factor =             double factor = U[i][k] / U[k][k];
            L[i][k] = factor;
            for (int j = k; j < n; ++j) {
                U[i][j] -= factor * U[k][j];
            }
        }
    }

    return make_pair(L, U);
}

/**
 * Print a matrix.
 *
 * @param matrix Matrix to print.
 */
void printMatrix(const Matrix& matrix) {
    for (const auto& row : matrix) {
        for (double value : row) {
            cout << value << " ";
        }
        cout << endl;
    }
}

int main() {
    // Example: LU decomposition
    Matrix A = {{2, -1, 0}, {-1, 2, -1}, {0, -1, 2}};

    auto LU = luDecomposition(A);
    Matrix L = LU.first;
    Matrix U = LU.second;

    cout << "Lower triangular matrix (L):" << endl;
    printMatrix(L);
    cout << "Upper triangular matrix (U):" << endl;
    printMatrix(U);

    return 0;
}