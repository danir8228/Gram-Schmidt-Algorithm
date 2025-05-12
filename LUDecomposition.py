#In my research, I discovered Doolittle's Algorithm, which streamlines this code.

#We assume that A is a square matrix
'''
Computes the LU decomposition of a square matrix A
input: square matrix A
output: two square matrices in a list [L, U], both size of A, s.t. when multiplied (in order given), result in A.
'''
def lu_decomposition(A):
    n = len(A)

    # Initialize L and U
    L = identity_matrix(n)
    U = zero_matrix(n)

    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_

        # Lower Triangular
        for k in range(i + 1, n):
            sum_ = sum(L[k][j] * U[j][i] for j in range(i))
            if U[i][i] == 0:
                raise ZeroDivisionError("Zero pivot encountered.")
            L[k][i] = (A[k][i] - sum_) / U[i][i]

    return L, U

'''
returns zero matrix to initialize U 
input: size of the square matrix wanted
output: square zeroes matrix of size inputted
'''
def zero_matrix(size):
    result = []
    for i in range(size):
        row = []
        for k in range(size):
            row.append(0)
        result.append(row)
    return result    

'''
returns identity matrix to initialize L 
input: size of the square matrix wanted
output: square identity matrix of size inputted
'''
def identity_matrix(size):
    I = zero_matrix(size)
    for i in range(size):
        I[i][i] = 1 #first index is the rows, second is the columns
    return I    


def main():
    print("Examples: \n")
    print(f"A zero matrix of size 3: {zero_matrix(3)} \n")
    print(f"An identity matrix of size 3: {identity_matrix(3)} \n")
    print(f"The LU decomposition for the vectors [4,3], [6,3]: {lu_decomposition([[4,3], [6,3]])} \n") #should return L = [[1,0], [1.5, 1]] and U = [[4,3], [0, -1.5]]


if __name__ == "__main__":
    main()