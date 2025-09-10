### RANDOM GENERATORS AND SEEDS

- Start by importing Generator and PCG64

```python

from numpy.random import Generator as gen

from numpy.random import PCG64 as pcg


```

- The Generator function takes a bit generator as an input and creates generator objects: numpy.random.Generator class

- PCG64 is short name for Permutation Congruential Generator.

- NumPy's random number generator and seeds are used to create sequences of seemingly random numbers that are actually reproducible. 

- This means you can get the exact same sequence of "random" numbers every time you run your code, which is crucial for things like scientific simulations, machine learning models, and testing.

```python

array_RG = gen(pcg())
array_RG.normal()
# The output is a single numeric value generated from a normal distribution.
# 0.2442263330674519
array_RG.normal(size=5)
#We can also specify the size of the output to indicate how many random values we want to be generated.
#Output will be: 
[ 0.33032371 -1.64381631 -0.04511023  0.8498047   1.53692559]

array_RG.normal(size = (5,5))
# If we put a tuple as the size the output will look as below:

[[ 1.93377683 -0.80150266  1.23929195  0.47611404 -0.56367856]
 [-1.54336153 -0.68740475 -0.5594701   0.17439918  0.54459243]
 [-0.1424702   1.51282522 -0.93371344 -0.98886255  0.16732294]
 [ 0.01030851  0.35549089  0.2275175  -0.92290965  0.98389582]
 [ 1.2267252  -0.66783354 -0.69145393  1.03534345  0.83523344]]


```

- The above showcases how to create random values.

- Everytime we call a method, the Generator randomly selects a "seed"

- Seed - a set of starting parameters for the algorithm

### Generating consistent/same values

- When we want to run the same function with the same arguments we will get the same output.
- Below is how to do it.
- The seed can be the numeric values or a sequence of numbers.

````python

array_RG = gen(pcg(seed =365 ))
array_RG.normal(size =(5,5))

[[-0.13640899  0.09414431 -0.06300442  1.05391641 -0.6866818 ]
 [-0.50922173 -0.7999526   0.73041825  0.08825439 -2.1177576 ]
 [ 0.65526774 -0.48095012 -0.5519114  -0.58578662 -0.98257896]
 [ 1.12378166 -1.30984316 -0.04703774  0.955272    0.26071745]
 [-0.20023668 -1.50172484 -1.4929163   0.96535084  1.18694633]]

````

- A seed only lasts for one execution of a method or function before it is reset.
- In short, if we run array_RG.normal(size = (5,5)) outside the execution it result to random 5 by 5 array.

### GENREATING INTEGERS, PROBABILITIES, AND RANDOM CHOICES

#### numpy.integers()

- Generates whole numbers (integers).
- Requires defining a fixed range of values to choose from.
- If we only provide a single value like it automatically assumes we only want integers between 0 and 10 excluding the value we passed.

````python
array_RG = gen(pcg(seed = 365))
array_RG.integers(10, size=(5,5))

[[0 7 6 7 8]
 [6 6 2 0 6]
 [3 0 3 7 9]
 [1 1 8 7 4]
 [4 8 6 4 9]]


````

- We can also  change the intervals by introducing high and low as shown below:


````python
array_RG = gen(pcg(seed = 365))
array_RG.integers(low = 10, high = 100, size = (5,5))

[[18 78 64 78 84]
 [66 67 28 10 69]
 [45 15 37 74 96]
 [19 21 89 73 54]
 [53 84 66 51 92]]

````

#### Probabilites

- Now we are looking into Probabilities.
- Probabilites do not work with high and low as here:: array_RG.integers(low = 10, high = 100, size = (5,5))
- This is because Probabilities are always between 0 and 1.

````python

array_RG = gen(pcg(seed = 365))

array_RG.random(size=(5,5))

[[0.75915734 0.7662218  0.6291028  0.20336599 0.66501486]
 [0.06559111 0.71326309 0.10812106 0.87969046 0.49405844]
 [0.82472673 0.45652944 0.07367232 0.69628564 0.36690736]
 [0.29787156 0.4996155  0.4865245  0.62740703 0.54952637]
 [0.64894629 0.04411757 0.7206516  0.84594003 0.17159792]]

# We get a 5 by 5 matrix of between 0 and 1.
# The values in it are extracted from a continuous uniform distribution.
# Statistically speaking, this means getting any of the infinitely many values in the interval is equally likely here.

````

#### Choice: numpy.choice()

- Simulates the idea of making an arbitrary choice out of a given sequence, be it a list , array or tuple.

````python
array_RG = gen(pcg(seed = 365))
array_RG.choice([1,2,3,4,5],size=(5,5))

[[1 4 4 4 5]
 [4 4 2 1 4]
 [2 1 2 4 5]
 [1 1 5 4 3]
 [3 5 4 3 5]]

# If we fail to provide out input values, the method defaults to using a descret uniform distribution 

# The first line of your code initializes a NumPy random number generator. The second line uses that generator to create a 5x5 array of random choices from a given list, with specified probabilities.

#Explanation of the Code
#array_RG = gen(pcg(seed=365)): This line creates an instance of a random number generator.

#pcg(seed=365): This part creates a specific type of bit generator, a PCG64 (Permuted Congruential Generator). The seed=365 argument provides a starting point for the random sequence. Using a seed ensures that if you run this code again, you will get the exact same sequence of "random" numbers.

#gen(...): The gen function wraps the bit generator to create a Generator object. This object is the main interface for creating random numbers, arrays, and choices. The resulting array_RG variable is now your repeatable, seeded random number generator.

#array_RG.choice([1,2,3,4,5], p=[0.1,0.1,0.1,0.1,0.7], size = (5,5)): This line uses the generator to create an array of random choices.

#choice([1,2,3,4,5]): This method is being told to pick random numbers from the list [1, 2, 3, 4, 5]. This is the population from which elements are chosen.

#p=[0.1,0.1,0.1,0.1,0.7]: This is the probability of picking each corresponding element from the list. The p array must have the same number of elements as the population. In this case, there is a 70% chance of picking the number 5, and a 10% chance of picking any of the other numbers.

#size = (5,5): This specifies the shape of the output array. The method will return a 2-dimensional array with 5 rows and 5 columns, for a total of 25 randomly chosen numbers.

#The Error
#The p values represent the probabilities of choosing each element from your list. A fundamental rule of probability is that the sum of all probabilities for all possible outcomes must equal 1.

#If the p values are not correct—specifically, if they do not sum to 1—NumPy will raise a ValueError.

#ValueError: 'p' must sum to 1.0 (at least within a reasonable tolerance)

#This error will occur, for example, if your p list was [0.1, 0.1, 0.1, 0.1, 0.6], which sums to 0.9. NumPy explicitly checks this condition to ensure that your probability distribution is valid.
````


#### GENERATING ARRAYS FROM KNOWN DISTRIBUTION


