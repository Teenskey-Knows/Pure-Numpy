 Python Functions: From Zero to Hero
📘 1. What Is a Function?
A function is a block of code that performs a specific task and can be reused.

🧠 Why use functions?
Reusability

Better organization

Easier debugging

🛠️ 2. Defining a Simple Function
python
Copy
Edit
def greet():
    print("Hello, world!")
✅ Calling the function:
python
Copy
Edit
greet()
# Output: Hello, world!
🧩 3. Function with Parameters
python
Copy
Edit
def greet(name):
    print(f"Hello, {name}!")
🧪 Call it with arguments:
python
Copy
Edit
greet("Alice")
# Output: Hello, Alice!
🔁 4. Return Values
python
Copy
Edit
def add(a, b):
    return a + b
📥 Store returned value:
python
Copy
Edit
result = add(5, 3)
print(result)
# Output: 8
🧮 5. Default Parameters
python
Copy
Edit
def greet(name="Stranger"):
    print(f"Hi, {name}!")
python
Copy
Edit
greet()            # Output: Hi, Stranger!
greet("Marto")     # Output: Hi, Marto!
📦 6. Keyword Arguments
python
Copy
Edit
def profile(name, age):
    print(f"{name} is {age} years old.")
python
Copy
Edit
profile(age=25, name="Joy")
# Output: Joy is 25 years old.
📚 7. Arbitrary Arguments
*args — multiple positional arguments:
python
Copy
Edit
def total(*numbers):
    return sum(numbers)
python
Copy
Edit
print(total(1, 2, 3, 4))  # Output: 10
**kwargs — multiple keyword arguments:
python
Copy
Edit
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
python
Copy
Edit
show_info(name="Ada", role="Developer")
# Output:
# name = Ada
# role = Developer
🧱 8. Nested Functions
python
Copy
Edit
def outer():
    def inner():
        print("Inside inner function")
    inner()
python
Copy
Edit
outer()
# Output: Inside inner function
🧠 9. Lambda Functions (Anonymous Functions)
python
Copy
Edit
square = lambda x: x * x
print(square(5))  # Output: 25
🎯 10. Higher-Order Functions
Functions that take other functions as arguments or return them.

python
Copy
Edit
def apply(func, value):
    return func(value)

print(apply(lambda x: x*3, 10))  # Output: 30
🔄 11. Recursion
A function calling itself.

python
Copy
Edit
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
python
Copy
Edit
print(factorial(5))  # Output: 120
🛡️ 12. Docstrings
Document your functions.

python
Copy
Edit
def greet(name):
    """This function greets the person by name."""
    print(f"Hello, {name}")
python
Copy
Edit
help(greet)
🏁 Conclusion
Use def to create functions.

Functions can have parameters and return values.

Support for default, keyword, variable-length arguments.

Use functions for cleaner, reusable, and maintainable code.