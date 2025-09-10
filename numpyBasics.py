
import numpy as np

from numpy.random import Generator as gen

from numpy.random import PCG64 as pcg

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# # print( a+ b)
# # print( a * b)
# # print( a/ b)


# to_reshape = np.array([10,20,30,40,50,60])

# reshaped = to_reshape.reshape(2,3)

# print(reshaped)

# transpose = reshaped.T

# print(transpose)


# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)

 
# another_matrix = np.array([[9,8,7], [6,5,4],[3,2,1]])
# print(another_matrix)


# matrix_C = np.array([[1,2,3,4,5],[4,6,7,3,5],[8,4,5,2,5]])

# print(matrix_C)


# # print(matrix_C[:,:] > 4)

# print(matrix_C[matrix_C[:,:]>4])


# matrix_D = np.array([[1,2,4,5,6],[3,2,5,7,7],[8,7,9,7,0]])

# print("Squeeze method applied",matrix_D[0:1,0:1].squeeze())


array_RG = gen(pcg(seed =365 ))
seed_Generated = array_RG.choice([1,2,3,4,5],size =(5,5))
print(seed_Generated)