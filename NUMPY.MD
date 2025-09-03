## Numpy

### Creating Numpy Array

```python

arr = np.array([1,3,5])

zeroes = np.zeroes((3,3))

ones = np.ones((2,4))

range_array = np.arange(1,100,3)

linspace_array = np.linspace(0,10,3)

```

### Manipulating Arrays

```python

arr = np.array([2,3,5,6,5])

reshaped = arr.reshape((3,2))

# Adding Arrays

arr = np.array([1,2,3])

expanded = arr[:, np.newaxis]

# In NumPy slicing, a colon : by itself means "select all elements along this dimension.

#np.newaxis is a special constant in NumPy (it's essentially None).

# When used as an index in array slicing, it tells NumPy to insert a new dimension of size 1 at that position.

#Output
[[1]
 [2]
 [3]]

```

### Basic Operations on Arrays

#### Element-wise Operations

```python

a = np.array ([1,2,3])
b = np.array([4,5,6])

print (a+b)
print (a * b)
print(a/b)

# output

# [5 7 9]
# [ 4 10 18]
# [0.25 0.4  0.5 ]

arr = np.array([4,16,25])
np.sqrt(arr)
# Output
[2 4  5]

np.sum(arr)
# 45

np.mean(arr)

np.max(arr)


```

### Array Indexing, Slicing, and Reshaping

#### Indexing & Indexing
```python
arr = np.array([10,20,30,40,50])

arr[2]

arr[1:4]

arr[:3]

arr[3:]

#Indexing for more dimensions: Example
array_dimension = np.array([[1,2,3],[4,5,6],[7,8,9]])

#To get the second dimension of the array you can index as follows.

array_dimension[1]
#Output =>
array([4,5,6])

#To get the second element of the second dimension, the below two ways will work:

array_dimension[1][1]
array_dimension[1,1]
#The above 2 ways will work which will give you an output of 5
```

#### Reshaping

```python

to_reshape = np.array([10,20,30,40,50,60])

reshaped = to_reshape.reshape(2,3)
#Output
[[10 20 30]
 [40 50 60]]


```

### Transposing

```python

transposed = reshaped.T

#Output

[[10 40]
 [20 50]
 [30 60]]

 ```


 ```python
 matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
 print(matrix)

[[1 2 3]
 [4 5 6]
 [7 8 9]]

 another_matrix = np.array([9,8,7], [6,5,4],[3,2,1])
print(another_matrix)

[[9 8 7]
 [6 5 4]
 [3 2 1]]


# Addition

matrix + another_matrix



```


## Assigning types in Numpy Arrays

```python
#Numpy Arrays can support all the data types supported by C e.g booleans, int. e.t.c

#Example

array_a = np.array([1,2,3,4], dtype="float32")
#The dtype float32 means for each element we are asigning a float that will occupy 32 bits of memory

#Another way of assigning data types can be the use of np.dataType

array_b = np.array([3,4,5],dtype=np.float16)


```

### Numpy Functions
- Looking at Broadcasting, Type Casting & Computing over a given axis
### Broad Casting
 - Stretching one variable over the other to produce an output with the same shape 

##### Rules of Broadcasting

- The arrays have the same shpae
- The arrays have the same number of dimensions, and the length of each dimension is either common or 1.
- The arrays that have too few dimensions can have their shapes  altered with a dimension 1, to satisfy the second rule.
  
```python
array_a = np.array([1,2,4])

array_b = np.array([[1],[6]])

matrix_C = np.array([[5,6,7],[9,0,2]])

# Example of Running a Function along a given axis

array_mean = np.mean(array_b, axis=0)
# The above will compute the mean along the columns & when axis= 1 that will compute axis along the row.


```


