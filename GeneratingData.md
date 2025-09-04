### GENERATING DATA WITH NUMPY

##### LOOKING AT np.empty(), np.zeros(), np.ones(), np.full()

````python

#np.empty()

# - Creates and empty N-D array
# - Return an array without initializing entries
# - Fastest way to generate an N-D array

empty_array = np.empty(shape=(2,3))

# np.empty creates the array without initializing the values.

#That means you get whatever random junk was in memory at that moment (it could look like random numbers, but they are not really random, just leftovers)


2. np.zeros()

zero_array = np.zeros(shape =(2,3))

# Will result to an array of zeros which are floating point numbers

zeros_array = np.zeros(shape=(2,3),dtype=int8)

# The above will result to an array of zeros which are integers and not floating point numbers


3. np.ones

ones_array = np.ones(shape=(2,3))


4. np.full()

# Generates an array filled entirely with a specified value
# Contains an additional mandatory argument which is the fill_value
# fill_value takes scalar values

full_array = np.full(shape = (2,3),fill_value=2)







````