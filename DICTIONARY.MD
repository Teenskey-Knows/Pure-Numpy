# Python Dictionaries: A Comprehensive Guide with Code Examples

Dictionaries in Python are **unordered collections** of key-value pairs. Each key in a dictionary is unique, and you can use immutable types (like strings, numbers, or tuples) as keys.

---

## 1. Creating a Dictionary

### Empty Dictionary
```python
# Create an empty dictionary
my_dict = {}
print(my_dict)  # Output: {}


# Create a dictionary with some initial key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)



# Access a value by its key
name = person["name"]
print(name)  # Output: Alice


# Using get() method, which allows a default value if the key is not found
age = person.get("age", "Not Found")
print(age)  # Output: 30

# Key that does not exist
country = person.get("country", "Not Found")
print(country)  # Output: Not Found


# Add a new key-value pair
person["country"] = "USA"
print(person)


# Update the value associated with an existing key
person["age"] = 31
print(person)


# Remove a key-value pair using del
del person["city"]
print(person)


# Remove a key and get its value using pop()
removed_value = person.pop("age", None)
print(removed_value)  # Output: 31
print(person)


# Remove and return the last inserted key-value pair
# (In versions before Python 3.7, dictionary order is not guaranteed)
key, value = person.popitem()
print(f"Removed: {key} -> {value}")
print(person)


for key in person:
    print(key, person[key])


for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")



Dictionary Methods Overview
keys(): Returns a view of the dictionary’s keys.

values(): Returns a view of the dictionary’s values.

items(): Returns a view of the dictionary’s key-value pairs.

clear(): Removes all items from the dictionary.

copy(): Returns a shallow copy of the dictionary.

update(): Updates the dictionary with key-value pairs from another dictionary.



# Update dictionary with another dictionary
additional_info = {"profession": "Engineer", "city": "Boston"}
person.update(additional_info)
print(person)





## 1. `keys()`

Returns a view object that displays a list of all the keys in the dictionary.


person = {"name": "Alice", "age": 30, "city": "New York"}
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Convert to list if needed
keys_list = list(person.keys())
print(keys_list)  # Output: ['name', 'age', 'city']


## 2. Values

print(person.values())  # Output: dict_values(['Alice', 30, 'New York'])

# Convert to list
values_list = list(person.values())
print(values_list)  # Output: ['Alice', 30, 'New York']


## 3. Items

print(person.items())  
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Iterate over items
for key, value in person.items():
    print(f"{key}: {value}")

## 4. Clear()

person.clear()
print(person)  # Output: {}

## 5. copy()


original = {"a": 1, "b": 2}
clone = original.copy()

print(clone)  # Output: {'a': 1, 'b': 2}

# Modify the clone
clone["a"] = 99
print(original)  # Output: {'a': 1, 'b': 2} — original remains unchanged

## 6. update()

person = {"name": "Alice", "age": 30}
update_data = {"age": 31, "city": "Boston"}

person.update(update_data)
print(person)
# Output: {'name': 'Alice', 'age': 31, 'city': 'Boston'}

## 7. get("key","default")
Returns the value for the specified key. If the key is not found, returns None or a provided default value.

print(person.get("name"))       # Output: Alice
print(person.get("country"))    # Output: None
print(person.get("country", "Unknown"))  # Output: Unknown


## 8. pop("key","default")
Removes the specified key and returns the corresponding value. If key is not found, returns default if given, otherwise raises a KeyError.


age = person.pop("age")
print(age)        # Output: 31
print(person)     # Output: {'name': 'Alice', 'city': 'Boston'}

# With default
missing = person.pop("zipcode", "Not Found")
print(missing)    # Output: Not Found


## 9. popitem()
Removes and returns the last inserted key-value pair as a tuple.

last_item = person.popitem()
print(last_item)  # Example Output: ('city', 'Boston')
print(person)     # Output: {'name': 'Alice'}
⚠️ Note: Before Python 3.7, the order of insertion is not preserved.

## 10. setdefault(key[, default])
Returns the value of the key. If the key does not exist, inserts the key with the specified default value.

person = {"name": "Alice"}
age = person.setdefault("age", 25)
print(age)        # Output: 25
print(person)     # Output: {'name': 'Alice', 'age': 25}

# Key already exists
existing = person.setdefault("name", "Bob")
print(existing)   # Output: Alice (unchanged)


## 11. fromkeys(iterable, value=None)
Creates a new dictionary from the given iterable with each element as a key and the same specified value.

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


## 12.Dictionary Comprehensions
You can create dictionaries using comprehensions to generate key-value pairs from iterables.

Example: Creating a Dictionary from a List
python
Copy
Edit
# Create a dictionary that maps numbers to their squares
squares = {num: num ** 2 for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## 13. Example: Conditional Dictionary Comprehension
# Create a dictionary with even numbers and their doubles
even_doubles = {num: num * 2 for num in range(1, 11) if num % 2 == 0}
print(even_doubles)  # Output: {2: 4, 4: 8, 6: 12, 8: 16, 10: 20}


8. Nested Dictionaries
Dictionaries can also contain other dictionaries as values.

# Dictionary representing a person with nested address information
person = {
    "name": "Bob",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Los Angeles",
        "zip": "90001"
    }
}

# Accessing nested dictionary elements
print(person["address"]["city"])  # Output: Los Angeles

