### _like functions

- Equivalent to np.empty(), np.zeros,np.ones, np.full

- We don't need to specify a shape or type

- We need to provide another array (whose shape and type we take)

- _like functions are useful as it acts as a second array where we store a value or each element of the original one

- It is also convenient when working with huge databases (faster loading times)

````python

matrix_A = np.array([[1,2,4,5],[4,5,3,4],[8,6,4,3]])

array_empty_like = np.empty_like(matrix_A)

# Remember, the empty function does not provide consistent output, so it might vary.

print (array_empty_like)

 [[ 9007633053253716 32651591227605107 27866160140451941 31244194868494433]
 [29555310643380340 32651234743943278 28710585070059624  9007633053515881]
 [27866456493391987 28429423626027113               100 29555375072935936]]


````

#### np.empty_like , np.zeros_like, np.ones_like, np.full_like

- Will only cover np.zeros_like since the other above functions work in a similar manner.

````python

array_0s_like = np.zeros_like(matrix_A)

# The output will always be full of zeros.

# Practical Application of zeros_like
1. Starting point for a planner
2. A "switch" where we can change the values from 0 to 1 (and back)




````