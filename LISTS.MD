# LIST

### Empty list
````PYTHON
empty_list = []
print(f"Empty list: {empty_list}")

````
### List of numbers

````PYTHON
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

````

### List of strings

````PYTHON
fruits = ["apple", "banana", "cherry"]
print(f"List of fruits: {fruits}")

````

### Mixed data types (possible, but generally less common for clarity)

````PYTHON
mixed_list = [1, "hello", True, 3.14]
print(f"Mixed list: {mixed_list}")

````

### Using the list() constructor

````PYTHON

another_list = list(("red", "green", "blue")) # Note the double parentheses for a tuple
print(f"List using constructor: {another_list}")

````

## LIST METHODS


### ACCESSING LISTS / INDEXING

my_list = ["a", "b", "c", "d", "e"]

### Accessing the first element
print(f"First element: {my_list[0]}")

### Accessing the third element
print(f"Third element: {my_list[2]}")

### Accessing the last element (negative indexing)
print(f"Last element: {my_list[-1]}")

### Accessing the second to last element
print(f"Second to last element: {my_list[-2]}")


## Slicing Lists

- You can extract a sub-section (slice) of a list using the slicing operator :.

````Python

my_list = ["a", "b", "c", "d", "e", "f", "g"]


# Elements from index 2 up to (but not including) index 5
print(f"Slice [2:5]: {my_list[2:5]}")

# Elements from the beginning up to (but not including) index 4
print(f"Slice [:4]: {my_list[:4]}")

# Elements from index 3 to the end
print(f"Slice [3:]: {my_list[3:]}")

# Elements from index -4 up to (but not including) index -1
print(f"Slice [-4:-1]: {my_list[-4:-1]}")

## -1 is for accessing the last element in a list so -2 is the 2nd last & so forth

# Copy the entire list
print(f"Full copy: {my_list[:]}")

# Slice with step (start:end:step)
print(f"Slice with step [::2]: {my_list[::2]}") # Every second element
Output:

Slice [2:5]: ['c', 'd', 'e']
Slice [:4]: ['a', 'b', 'c', 'd']
Slice [3:]: ['d', 'e', 'f', 'g']
Slice [-4:-1]: ['d', 'e', 'f']
Full copy: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Slice with step [::2]: ['a', 'c', 'e', 'g']

````

## Modifying Elements

- Lists are mutable meaning you can change their elements after creation.

````python

colors = ["red", "green", "blue"]
print(f"Original list: {colors}")

# Change an element at a specific index
colors[1] = "yellow"
print(f"Modified list: {colors}")

# Change a range of elements (slicing assignment)
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40] # Replaces elements at index 1, 2, 3
print(f"Modified range: {numbers}")

# Replace with more or fewer items
more_numbers = [1, 2, 3, 4, 5]
more_numbers[1:3] = [100, 200, 300, 400] # Replaces elements at index 1, 2
print(f"Replace with more items: {more_numbers}")

Output:

Original list: ['red', 'green', 'blue']
Modified list: ['red', 'yellow', 'blue']
Modified range: [1, 20, 30, 40, 5]
Replace with more items: [1, 100, 200, 300, 400, 4, 5]

`````

## Adding Elements

##  append(): Adds an element to the end of the list.


fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")
Output:

After append('cherry'): ['apple', 'banana', 'cherry']


## b. insert(): Inserts an element at a specified index.


fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange") # Inserts "orange" at index 1
print(f"After insert(1, 'orange'): {fruits}")
Output:

After insert(1, 'orange'): ['apple', 'orange', 'banana', 'cherry']


## c. extend(): Adds elements from another iterable (like another list, tuple, etc.) to the end of the current list.

list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(f"After extend(list2): {list1}")

tuple_data = ("a", "b")
list1.extend(tuple_data)
print(f"After extend(tuple_data): {list1}")

After extend(list2): [1, 2, 3, 4, 5]
After extend(tuple_data): [1, 2, 3, 4, 5, 'a', 'b']


## Removing Elements

### remove(): Removes the first occurrence of a specified value.

my_items = ["pen", "book", "pen", "eraser"]
my_items.remove("pen") # Removes the first "pen"

print(f"After remove('pen'): {my_items}")

Output:

After remove('pen'): ['book', 'pen', 'eraser']

## b. pop(): Removes and returns the element at a specified index. If no index is given, it removes and returns the last item.

my_list = ["a", "b", "c", "d"]
removed_item = my_list.pop(1) # Removes item at index 1 ("b")
print(f"Removed item: {removed_item}, List now: {my_list}")

last_item = my_list.pop() # Removes the last item ("d")
print(f"Removed last item: {last_item}, List now: {my_list}")
Output:

Removed item: b, List now: ['a', 'c', 'd']
Removed last item: d, List now: ['a', 'c']

## c. del keyword: Removes element(s) by index or slice, or deletes the entire list.


my_list = ["red", "green", "blue", "yellow"]
del my_list[1] # Deletes element at index 1 ("green")
print(f"After del my_list[1]: {my_list}")

my_list = ["red", "green", "blue", "yellow"]
del my_list[0:2] # Deletes elements from index 0 to 1
print(f"After del my_list[0:2]: {my_list}")

# Delete the entire list object
# del my_list # This would make my_list undefined
Output:

After del my_list[1]: ['red', 'blue', 'yellow']
After del my_list[0:2]: ['blue', 'yellow']


## d. clear(): Removes all elements from the list, leaving it empty.

my_list = [1, 2, 3, 4]
my_list.clear()
print(f"After clear(): {my_list}")

After clear(): []


## Other Useful List Methods

### a. count(): Returns the number of times a specified value appears in the list.


numbers = [1, 2, 2, 3, 1, 4, 2]
count_of_2 = numbers.count(2)
print(f"Count of 2: {count_of_2}")
Output:

Count of 2: 3

### b. index(): Returns the index of the first occurrence of a specified value. Raises a ValueError if the value is not found.


fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")
print(f"Index of 'banana': {index_of_banana}")

# To handle cases where the item might not be present:
if "grape" in fruits:
    print(f"Index of 'grape': {fruits.index('grape')}")
else:
    print("'grape' not found in the list.")
Output:

Index of 'banana': 1
'grape' not found in the list.


## c. sort(): Sorts the list in ascending order by default. Modifies the list in-place.


numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(f"Sorted numbers (ascending): {numbers}")

words = ["banana", "apple", "cherry"]
words.sort()
print(f"Sorted words (alphabetical): {words}")

# Sort in descending order
numbers.sort(reverse=True)
print(f"Sorted numbers (descending): {numbers}")
Output:

Sorted numbers (ascending): [1, 1, 2, 3, 4, 5, 9]
Sorted words (alphabetical): ['apple', 'banana', 'cherry']
Sorted numbers (descending): [9, 5, 4, 3, 2, 1, 1]

## d. reverse(): Reverses the order of elements in the list in-place.

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(f"Reversed list: {my_list}")
Output:

Reversed list: [5, 4, 3, 2, 1]

## e. copy(): Returns a shallow copy of the list. Important for avoiding unintended modifications when assigning lists.


original_list = [1, 2, 3]
copied_list = original_list.copy() # Creates a new list object

copied_list.append(4)

print(f"Original list: {original_list}") # Original remains unchanged
print(f"Copied list: {copied_list}")

# Without copy(), both would refer to the same list:
# another_reference = original_list
# another_reference.append(5)
# print(f"Original list after direct reference append: {original_list}") # Original would also be [1, 2, 3, 5]
Output:

Original list: [1, 2, 3]
Copied list: [1, 2, 3, 4]

## List Length
Use the len() function to get the number of elements in a list.


my_list = ["one", "two", "three"]
list_length = len(my_list)
print(f"Length of the list: {list_length}")
Output:

Length of the list: 3


## Iterating Through a List (Loops)
You can easily loop through the items in a list.

Python

fruits = ["apple", "banana", "cherry"]

print("Iterating through fruits:")
for fruit in fruits:
    print(fruit)

print("\nIterating with index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
Output:

Iterating through fruits:
apple
banana
cherry

Iterating with index:
Index 0: apple
Index 1: banana
Index 2: cherry