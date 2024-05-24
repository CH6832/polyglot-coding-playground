#include <iostream>
#include <vector>
#include <cmath>

/**
 * QR_Decomposition.cpp
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
 * Example Usage: In the main function, an example usage of the qrDecomposition function is provided. We define a matrix
 * A, and then call the qrDecomposition function to compute the QR decomposition. Finally, we print the orthogonal
 * matrix Q and the upper triangular matrix R.
 */

using namespace std;

// Typedef for a matrix
typedef vector<vector<double>> Matrix;

/**
 * Perform QR decomposition of a matrix.
 *
 * @param A Matrix to decompose.
 * @param Q Orthogonal matrix Q (output parameter).
 * @param R Upper triangular matrix R (output parameter).
 */
void qrDecomposition(Matrix& A, Matrix& Q, Matrix& R) {
    int m = A.size();
    int n = A[0].size();

