
**Author: Daniela Ramos**

# **Gram-Schmidt Algorithm**
The Gram-Schmidt Algorithm is a procedure to find an orthonormal basis of a subspace, when given a list of linearly independent vectors that already span that space. 

Here is the doc-string for each function used:

### *gram_schmidt()*
The Gram-Schmidt Algorithm takes a list of linearly independent vectors (I did not implement a check to see if they were not 
independent) and constructs an orthonormal basis of vectors from them. It does this by subtracting the components in existing 
directions from the next vector since it needs to span a new dimension. In other words, this algorithm constructs the next
vector by assuming the previous vectors are already orthogonal. I decided to normalize them all at the end, since the order
of that step doesn't matter.
input: a list of lists, understood to be vectors
output: list of vectors

### *dot_product()*
Computes the dot product of the two vectors
input: two lists, understood to be vectors
output: an int, understood to be a constant

### *denominator()*
Computes the norm of the vector and squares it, which is the denominator of the projection equation.
input: one vector
output: scalar

### *projection()*
Computes the projection of v2 onto v1. 
input: two vectors: v1, v2
output: vector

### *subtract_vec()*
Computes vector subtraction, v1 - v2
input: two vectors: v1, v2
output: one vector

### *divide_vec()*
Divides a vector by a scalar.
input: a vector and a scalar
output: a vector.

### *normalize()*
normalizes all vectors in the array; divides each vector by its length
input: list of vectors (2d array)
output: list of vectors

# **LU Decomposition**
LU Decomposition is an algorithm that factors a square matrix A into:
L, a lower triangular matrix of size A
U, an upper triangular matrix of size A. 
This factorization is incredibly useful to systematically solve systems of equations; In fact, it is widely used by applications that solve these systems. 

Here is the doc-string for each function used:

### *lu_decomposition()*
Computes the LU decomposition of a square matrix A
input: square matrix A
output: two square matrices in a list [L, U], both size of A, s.t. when multiplied (in order given), result in A.

### *zero_matrix()*
Returns zero matrix; used to initialize U 
input: size of the square matrix wanted
output: square zeroes matrix of size inputted

### *identity_matrix()*
Returns identity matrix; used to initialize L 
input: size of the square matrix wanted
output: square identity matrix of size inputted

# **How to Use**

### **Examples**
In order to see a few examples which demonstrate the use of each function, simply run the file, as the *main()* function includes examples. 


### **Further Use**
In order to use any of the functions named above, simply comment out or delete the examples, and call the function with your desired arguments. If there is any confusion about the necessary arguments, including order or type, simply check the doc-string, either in this file, or above the function itself. 

Note that the Gram-Schmidt implementation requires use of the mathematical python library numpy, but only to calculate square roots, which is necessary for the normalization function. There are no other necessary libraries. 