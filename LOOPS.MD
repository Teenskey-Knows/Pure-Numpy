# Python Loops – How They Work & Supported Data Types

Python provides two main loop types: `for` and `while`. Loops allow you to repeat blocks of code based on conditions or over sequences.

---

## 1. `for` Loop

Used to iterate over a **sequence** (like lists, strings, tuples, dictionaries, sets, or any iterable).

### Syntax
```python
for item in sequence:
    # do something with item
Example: Looping Over a List
python
Copy
Edit
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
Example: Looping Over a String
python
Copy
Edit
for char in "hello":
    print(char)
Example: Looping Over a Tuple
python
Copy
Edit
colors = ("red", "green", "blue")
for color in colors:
    print(color)
Example: Looping Over a Set
python
Copy
Edit
numbers = {1, 2, 3}
for num in numbers:
    print(num)
Example: Looping Over a Dictionary
python
Copy
Edit
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])
Or using .items():

python
Copy
Edit
for key, value in person.items():
    print(f"{key}: {value}")
Example: Using range()
python
Copy
Edit
for i in range(5):
    print(i)  # Output: 0 to 4
2. while Loop
Repeats a block of code as long as a condition is True.

Syntax
python
Copy
Edit
while condition:
    # do something
Example: Counting
python
Copy
Edit
count = 0
while count < 3:
    print(count)
    count += 1
3. Loop Control Statements
break: Exit the loop early
python
Copy
Edit
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2
continue: Skip the current iteration
python
Copy
Edit
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4
4. else Clause in Loops
Executes after the loop completes normally (not via break).

Example with for
python
Copy
Edit
for i in range(3):
    print(i)
else:
    print("Loop completed")  # This runs
Example with while
python
Copy
Edit
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Done")  # This runs