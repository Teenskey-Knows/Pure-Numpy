# PYTHON DATA TYPES.

## INTEGERS

### Addition
result_add = 5 + 3  # 8

### Subtraction
result_sub = 10 - 4 # 6

### Multiplication
result_mul = 6 * 7   # 42

### Division (always results in a float in Python 3)
result_div_float = 15 / 3 # 5.0
result_div_float_2 = 10 / 3 # 3.333...

### Floor Division (integer division - discards the remainder)
result_div_floor = 15 // 3 # 5
result_div_floor_2 = 10 // 3 # 3
result_div_floor_neg = -10 // 3 # -4 (rounds towards negative infinity)

### Modulo (remainder after division)
result_mod = 17 % 5  # 2

### Exponentiation (raising to a power)
result_pow = 2 ** 3  # 8
result_pow_neg = 2 ** -1 # 0.5 (results in a float)

## Built-in Functions that Work with Integers 

### abs(): Returns the absolute value
abs_pos = abs(5)    # 5
abs_neg = abs(-5)   # 5

### pow(base, exp[, mod]): Raises base to the power of exp.

### If mod is present, returns (base ** exp) % mod (more efficient)
pow_simple = pow(2, 3)       # 8
pow_mod = pow(10, 3, 7)    # (1000 % 7) = 6

### round(number[, ndigits]): 
- Rounds a number to a given number of decimal places.
- If ndigits is omitted or is None, it returns the nearest integer.
round_up = round(5.6)   # 6
round_down = round(5.4) # 5
round_int = round(5)    # 5

### int(): 
- Converts a value to an integer.

int_float = int(3.14)   # 3 (truncates towards zero)
int_string = int("123")  # 123
int_neg_string = int("-45") # -45


# int(x, base): Converts a string or number to an integer, interpreting x in the given base.
int_base2 = int("1010", 2)  # 10 (binary 1010)
int_base16 = int("FF", 16)    # 255 (hexadecimal FF)

# min(iterable, *args[, key]): Returns the smallest item in an iterable or the smallest of two or more arguments.
min_list = min([1, 5, 2, 8]) # 1
min_args = min(3, 7, 1, 9)   # 1

# max(iterable, *args[, key]): Returns the largest item in an iterable or the largest of two or more arguments.
max_list = max([1, 5, 2, 8]) # 8
max_args = max(3, 7, 1, 9)   # 9

# sum(iterable[, start]): Sums the items of an iterable from left to right and returns the total.
sum_list = sum([1, 2, 3, 4]) # 10
sum_start = sum([1, 2, 3], 5) # 11 (1 + 2 + 3 + 5)

# --- Bitwise Operators (operate on the binary representation of integers) ---

# Bitwise AND (&): Returns 1 if both bits are 1, otherwise 0.
bitwise_and = 5 & 3  # (0101 & 0011) = 0001 (1)

# Bitwise OR (|): Returns 1 if at least one bit is 1.
bitwise_or = 5 | 3   # (0101 | 0011) = 0111 (7)

# Bitwise XOR (^): Returns 1 if the bits are different, 0 if they are the same.
bitwise_xor = 5 ^ 3  # (0101 ^ 0011) = 0110 (6)

# Bitwise NOT (~): Inverts the bits (equivalent to -(n+1)).
bitwise_not = ~5   # -(5 + 1) = -6

# Left Shift (<<): Shifts the bits to the left by a specified number of positions.
# Equivalent to multiplying by 2 raised to the power of the shift.
left_shift = 5 << 2 # (0101 << 2) = 010100 (20) (5 * 2**2)

# Right Shift (>>): Shifts the bits to the right by a specified number of positions.
# Equivalent to integer division by 2 raised to the power of the shift.
right_shift = 5 >> 1 # (0101 >> 1) = 0010 (2) (5 // 2**1)
right_shift_neg = -5 >> 1 # -3 (sign is preserved)

#  Methods of the `int` class (though you typically use operators and built-in functions) 

###  `int.bit_length()`: Returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros.
bit_length_pos = (10).bit_length()   # 4 (binary 1010)
bit_length_neg = (-10).bit_length()  # 4 (binary representation of absolute value)
bit_length_zero = (0).bit_length()   # 0

# `int.to_bytes(length, byteorder, signed=False)`: Returns an array of bytes representing an integer.
to_bytes_pos = (255).to_bytes(1, 'big')      # b'\xff'
to_bytes_multi = (65535).to_bytes(2, 'little') # b'\xff\xff'
to_bytes_signed = (-1).to_bytes(1, 'big', signed=True) # b'\xff'

# `int.from_bytes(bytes, byteorder, signed=False)`: Returns the integer represented by the given array of bytes.
from_bytes_big = int.from_bytes(b'\x0a', 'big')      # 10
from_bytes_little = int.from_bytes(b'\xff\xff', 'little') # 65535
from_bytes_signed = int.from_bytes(b'\xff', 'big', signed=True) # -1

# --- Boolean Context (integers can be evaluated in a boolean context) ---

# 0 is considered False
if 0:
    print("This won't print")

# Any non-zero integer is considered True
if 5:
    print("This will print")

if -3:
    print("This will also print")


# --- Comparison Operators (result in a boolean) ---

### Equal to (==)
is_equal = 5 == 5   # True
is_not_equal = 5 == 3 # False

# Not equal to (!=)
is_not_equal_2 = 5 != 3 # True
is_equal_2 = 5 != 5   # False

# Greater than (>)
is_greater = 10 > 5  # True

# Less than (<)
is_less = 5 < 10   # True

# Greater than or equal to (>=)
is_greater_equal = 5 >= 5 # True

# Less than or equal to (<=)
is_less_equal = 5 <= 5  # True



## STRING METHOD

- Strings have a lot of useful methods:

### capitalize()
Capitalizes the first letter of the string.
```python
s = "hello"
print(s.capitalize())  # Output: "Hello"

```
### lower()
Converts the string to lowercase.

```python
s = "HELLO"
print(s.lower())  # Output: "hello"

```

### upper()
Converts the string to uppercase.

```python
s = "hello"
print(s.upper())  # Output: "HELLO"

```
### title()
Capitalizes the first letter of each word.

```python
s = "hello world"
print(s.title())  # Output: "Hello World"

```

### split()
Splits the string into a list of substrings.

``` python

s = "hello world"
print(s.split())  # Output: ['hello', 'world']

```

### join()
Joins elements of an iterable into a single string.

```python
lst = ['hello', 'world']
print(" ".join(lst))  # Output: "hello world"

```

### replace()
Replaces occurrences of a substring with another.

``` python

s = "hello world"
print(s.replace("world", "Python"))  # Output: "hello Python"

```
### strip()
Removes leading and trailing whitespaces.
```python
s = "   hello world   "
print(s.strip())  # Output: "hello world"

```

### startswith()
Checks if the string starts with a specific substring.

```python
s = "hello world"
print(s.startswith("hello"))  # Output: True
```

### endswith()
Checks if the string ends with a specific substring.

```python

s = "hello world"
print(s.endswith("world"))  # Output: True

```

### find()
Finds the first occurrence of a substring.
```python

s = "hello world"
print(s.find("world"))  # Output: 6 (index of "world")

```

### count()
Counts the number of occurrences of a substring.
```python

s = "hello hello world"
print(s.count("hello"))  # Output: 2
```

### format()
Formats strings using placeholders.

```python
name = "Martoh"
print("Hello, {}".format(name))  # Output: "Hello, Martoh"
```

### isalpha()
Checks if all characters are alphabetic.

```python

s = "hello"
print(s.isalpha())  # Output: True
```

### isdigit()
Checks if the string contains only digits.

```python

s = "12345"
print(s.isdigit())  # Output: True

```


# Boolean

```python

is_sunny = True
is_raining = False

```

## Boolean Operations (Logical Operators)

- You can combine and manipulate boolean values using logical `and`, `or` and `not`.

### and
- The `and` operator returns `True` if both operands are `True` otherwise, it returns false

```python

can_vote = True
is_citizen = True
is_adult = True

# Both conditions must be True to vote
eligible_to_vote = can_vote and is_citizen and is_adult

print(f"Is eligible to vote? {eligible_to_vote}")

can_afford_car = True
has_driving_license = False

can_buy_car = can_afford_car and has_driving_license
print(f"Can buy car? {can_buy_car}")

```

### or

- The `or` operator returns `True` if at least one of the operands is `True`

- Returns `False` only if both operands are `False`


### `not` Operator

- The `not` operator inverts the boolean value of its operand.

````python

is_admin = True
is_guest = False

print(f"Is not admin? {not is_admin}")
print(f"Is not guest? {not is_guest}")

````

### Comparison Operators

Comparison operators `(>, <, ==, !=, >=, <=)` evaluate the relationship between operands and return True or False.


### `Truthiness` and `Falsiness`

- In Python, not just True and False are considered boolean in a conditional context. 

- Many other data types have an inherent "truthiness" or "falsiness."

#### Falsy values:

- False
- None
- 0 (integer zero)
- 0.0 (float zero)
- '' or "" (empty string)
- [] (empty list)
- () (empty tuple)
- {} (empty dictionary)
- set() (empty set)

### Truthy values:

Anything else (non-empty strings, non-zero numbers, non-empty collections, etc.)