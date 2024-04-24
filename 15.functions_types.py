#In programming, there are various types of functions that serve different purposes and have different characteristics. Here are some common types of functions:

#Built-in Functions:  These are functions that are provided by the programming language itself. They are typically included in the standard library and can be used directly without the need for further implementation
print("Hello, World!")  # Simple function 

#User-defined Functions: These are functions defined by the programmer to perform specific tasks. User-defined functions allow for code reuse and abstraction, making programs more modular and easier to maintain
# Example of a user-defined function
def add_numbers(a, b): # Function with Arguments
    return a + b        # Retrun type functions

result = add_numbers(5, 3)
print(result)  # Output: 8

#Pure Functions: Pure functions are functions that, given the same input, will always return the same output and have no side effects. They don't modify any external state or data. Pure functions are deterministic and have benefits like ease of testing and reasoning about the code.

# Example of a pure function
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20


#Impure Functions: Unlike pure functions, impure functions may have side effects or produce different results for the same input. They might modify external state or perform I/O operations. While impure functions are sometimes necessary, they can make code harder to understand and test.
# Example of an impure function
def greet(name):
    print("Hello, " + name)

greet("Alice")  # Output: Hello, Alice


#Recursive Functions: Recursive functions are functions that call themselves within their definition. They are often used to solve problems that can be broken down into smaller, similar sub-problems. Recursion can be a powerful technique, but it requires careful design to avoid infinite loops and excessive memory consumption.
# Example of a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # Output: 120


#Higher-order Functions: Higher-order functions are functions that can take other functions as arguments or return functions as results. They enable functional programming paradigms like map, filter, and reduce.
# Example of a higher-order function
def apply_operation(operation, x, y):
    return operation(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 4, 3)
print(result)  # Output: 7

#Anonymous Functions (Lambda Functions): Anonymous functions, also known as lambda functions or function literals, are functions that are not bound to an identifier and can be defined inline. They are often used for short, one-off operations where defining a named function would be overkill.
# Example of an anonymous function
double = lambda x: x * 2

result = double(5)
print(result)  # Output: 10

#Callback Functions: Callback functions are functions that are passed as arguments to other functions and are executed after a certain operation is completed. They are commonly used in event-driven programming and asynchronous operations to handle responses or events.

# Example of a callback function
def process_data(data, callback):
    processed_data = data * 2
    callback(processed_data)

def print_data(data):
    print("Processed data:", data)

process_data(5, print_data)  # Output: Processed data: 10

#Generator Functions: Generator functions are functions that can be paused and resumed, allowing them to produce a sequence of values lazily. They are particularly useful for dealing with large datasets or infinite sequences, as they avoid the need to store the entire sequence in memory at once.
# Example of a generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator function
counter = count_up_to(5)
for num in counter:
    print(num)  # Output: 1, 2, 3, 4, 5

#Class Methods: In object-oriented programming, class methods are functions that are associated with a class rather than with instances of the class. They can access and modify class-level variables and are typically called using the class name rather than an instance.
# Example of a class method
class MyClass:
    @classmethod
    def greet(cls, name):
        print("Hello, " + name)

MyClass.greet("Bob")  # Output: Hello, Bob







