import numpy as np #only used for square root function

'''
input: a list of lists, understood to be vectors
output: list of vectors
The Gram-Schmidt Algorithm takes a list of linearly independent vectors (I did not implement a check to see if they were not 
independent) and constructs an orthonormal basis of vectors from them. It does this by subtracting the components in existing 
directions from the next vector since it needs to span a new dimension. In other words, this algorithm constructs the next
vector by assuming the previous vectors are already orthogonal. I decided to normalize them all at the end, since the order
of that step doesn't matter.
'''
def gram_schmidt(vectors):
    ans = [] #to store unnormalized orthogonal vectors
    for i in range(len(vectors)): #how many vectors
        #if first vector, just take it as is. 
        if i == 0:
            ans.append(vectors[i])
            continue #passes to next iteration of for loop
        
        w = vectors[i] #before substraction
    
        #iterating through vectors already done, to subtract their parts from the next
        for j in range(i):
            w = subtract_vec(w, projection(ans[j], vectors[i]))
        ans.append(w)

        #normalize array of orthogonal vectors
        ans = normalize(ans)
    return ans    
        

'''
input: two lists, understood to be vectors
output: an int, understood to be a constant
computes the dot product of the two vectors
'''   

def dot_product(v1, v2):
    toAdd = []
    if len(v1) != len(v2):
        raise ValueError("two vectors are not the same length")
    for i in range(len(v1)):
        #multiplying i components and storing them in array at i
        toAdd.append(v1[i] * v2[i])
    return sum(toAdd)
        
'''
input: one vector
output: scalar
computes the norm of the vector and squares it,
which is the denominator of the projection equation.
'''        
def denominator(v1):
    toAdd = []
    for i in range(len(v1)):
        toAdd.append(v1[i] * v1[i])
    return sum(toAdd)    


'''
input: two vectors
output: vector
computes the projection of v2 onto v1. 
'''
def projection(v1, v2):
    ans = []
    coefficient = dot_product(v1, v2)/ denominator(v1)
    for i in range(len(v1)):
        ans.append(coefficient * v1[i])
    return ans    

'''
input: two vectors
output: one vector
computes vector subtraction, v1 - v2
'''
def subtract_vec(v1, v2):
    ans = []
    for i in range(len(v1)):
        ans.append(v1[i] - v2[i])
    return ans    

'''
input: a vector and a scalar
output: a vector.
divides a vector by a scalar.
'''
def divide_vec(v, n):
    for i in range(len(v)):
        v[i] = v[i]/n
    return v    

'''
input: list of vectors (2d array)
output: list of vectors
normalizes all vectors in the array;
divides each vector by its length
'''
def normalize(vectors):
    for i in range(len(vectors)):
        length = np.sqrt(denominator(vectors[i])) #reuse denominator function
        vectors[i] = divide_vec(vectors[i], length)
    return vectors    


def main():
    print("Examples: \n")
    print(f"The dot product of [1,2] and [3,4] is {dot_product([1,2], [3, 4])} \n")
    print(f"The square norm of [1, -1, 1] is {denominator([1, -1, 1])} \n")
    print(f"The projection of [3,1] onto [2,4] is {projection([2,4], [3,1])} \n")
    print(f"The difference of [3,2] and [2,1] is {subtract_vec([3,2], [2,1])} \n")
    print(f"The result of dividing [2,4,6] by 2 is {divide_vec([2,4,6], 2)} \n")
    print(f"The result of Gram-Schmidt on the vectors [1,-1,1], [1,0,1], [1,1,2] is {gram_schmidt([[1,-1,1], [1,0,1], [1,1,2]])} \n")


if __name__ == "__main__":
    main()