#Tuples in Python are immutable sequences, meaning they cannot be modified after creation. Therefore, there are only two built-in methods available for tuples:

#Homogeneous Tuples:
#Homogeneous tuples contain elements of the same data type. They are often used to represent collections of items that share a common characteristic.
int_tuple = (1, 2, 3, 4, 5)
str_tuple = ('apple', 'banana', 'orange')
print(str_tuple)
print("###############################################################################################################")

#Heterogeneous Tuples:
#Heterogeneous tuples contain elements of different data types. They can store a mix of integers, strings, floats, or other data types.
mixed_tuple = (1, 'apple', 3.14, True)
print(str_tuple)
print("###############################################################################################################")


#Named Tuples:
#Named tuples are tuples with named elements, providing more descriptive access to the elements. They are defined using the collections.namedtuple() function.
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
print("###############################################################################################################")


#Immutable Tuples:
#Tuples in Python are immutable, meaning their elements cannot be modified after creation. This immutability ensures that tuples remain consistent and predictable throughout their lifecycle.
my_tuple = (1, 2, 3)
print(my_tuple)
print("###############################################################################################################")

#Empty Tuples:
#Empty tuples contain no elements. They are often used as placeholders or to represent the absence of data.
empty_tuple = ()
print(empty_tuple)
print("###############################################################################################################")

#Singleton Tuples:
#Singleton tuples contain a single element. Despite having only one element, they maintain the tuple syntax by including a comma after the element.
single_tuple = (42,)
print(single_tuple)
print("###############################################################################################################")

# Attempting to modify a tuple will result in an error
my_tuple[0] = 10  # Raises TypeError: 'tuple' object does not support item assignment
