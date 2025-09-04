#### SCALA

1. Scalar (the simplest)

A scalar is just a single number.

It has magnitude only (no direction).

Think of it like temperature, mass, or your bank balance (if only one number could describe it).

Examples:

5
5, 
−
2.7
−2.7, 
𝜋
π, 
2
2
	​


In NumPy:

a = 5   # scalar



#### VECTOR

2. Vector (a list of numbers)

A vector is an ordered collection of scalars.

It has both magnitude and direction.

You can picture it as an arrow in space: the numbers tell you how far to move along each axis.

Examples:


=[3,4] (like moving 3 steps east, 4 steps north).


=[1,2,2].

Its magnitude is found by Pythagoras:


v = np.array([3, 4])   # vector in 2D


#### MATRIX


3. Matrix (a grid of numbers)

A matrix is a 2D array of scalars (rows × columns).

You can think of it as a bunch of vectors stacked side by side.

Matrices are used for transformations (rotating, scaling, projecting), and also to represent systems of equations.


That’s a 2×3 matrix (2 rows, 3 columns).


#### Array Dimensionality

```python

matrix_D = np.array([[1,2,4,5,6],[3,2,5,7,7],[8,7,9,7,0]])

type(matrix_D[0,0])

#Ans = numpy.int32
print(matrix_D[0,0])
#Output will be just 1

type(matrix_D[0,0:1])

#Ans = numpy.ndarray

print(matrix_D[0,0:1])

#Output will be [1]

type(matrix_D[0:1,0:1])

#Ans = numpy.ndarray

print(matrix_D[0:1,0:1])

#Ans = [[1]]

## The difference it make whether we're storing it as a scalar, vector or matrix.
## Certain functions or methods can only be executed with inputs of a fixed size



# THE SQUEEZE METHOD

# Squeeze method removes all the unnecessary dimensions of an array.

matrix_D[0:1,0:1].squeeze()

# Ans = 1
# The output will be a 0-D array but of type N-D array



### ANOTHER WAY OF DOING IT WILL BE 

np.squeeze(matrix_D[0:1,0:1])

# Ans  = 1 
````