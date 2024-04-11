# Integers (Immutable)
x = 10
print(type(x))  # Output: <class 'int'>

# Floats (Immutable)
y = 3.14
print(type(y))  # Output: <class 'float'>

# Complex numbers (Immutable)
z = 2 + 3j
print(type(z))  # Output: <class 'complex'>

# Strings (Immutable)
s = "hello"
print(type(s))  # Output: <class 'str'>

# Lists (Mutable)
l = [1, 2, 3]
print(type(l))  # Output: <class 'list'>

# Tuples (Immutable)
t = (1, 2, 3)
print(type(t))  # Output: <class 'tuple'>

# Dictionaries (Mutable)
d = {'a': 1, 'b': 2}
print(type(d))  # Output: <class 'dict'>

# Sets (Mutable)
st = {1, 2, 3}
print(type(st))  # Output: <class 'set'>

# Booleans (Immutable)
b = True
print(type(b))  # Output: <class 'bool'>

'''
Mutable:

Mutable objects can be modified after creation. This means that you can change their state, add, remove, or modify elements without creating a new object.
Examples of mutable objects in Python include lists, dictionaries, and sets.

Immutable:
Immutable objects cannot be modified after creation. Once created, their state cannot be changed.
Examples of immutable objects in Python include integers, floats, complex numbers, strings, tuples, and frozensets.
'''
