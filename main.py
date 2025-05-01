#hold vectors as arrays (lists)
#so vectors would be 2d arrays

#number of vectors is i 

A = [[1,2], [3,4],] #as column vectors

def gram_schmidt(A):
    for i in len(A): #how many vectors
        if i == 1:
            #q = A[i] #takes first vector as it is. 
            return
        

'''
input: two lists, understood to be vectors
output: an int, understood to be a constant
computes the dot product of the two vectors
'''   

def dot_product(v1, v2):
    toAdd = []
    if len(v1) != len(v2):
        raise ValueError("two vectors are not the same length")
    for i in len(v1):
        
        



dot_product([1,2], [3, 4])
