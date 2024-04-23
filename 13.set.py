#In Python, a set is a built-in data type that represents an unordered collection of unique elements. Sets are mutable, which means you can add or remove elements from them. However, sets themselves are unordered, so they do not support indexing or slicing like sequences such as lists or tuples.

#Homogeneous Sets:
#Homogeneous sets contain elements of the same data type. They are often used to represent collections of items that share a common characteristic.
int_set = {1, 2, 3, 4, 5}
print(int_set)
print("#####################################################################################################################")

#Heterogeneous Sets:
#Heterogeneous sets contain elements of different data types. They can store a mix of integers, strings, floats, or other data types.
mixed_set = {1, 'apple', 3.14, True}
print(mixed_set)
print("#####################################################################################################################")

#Empty Sets:
#Empty sets contain no elements. They are often used as placeholders or to initialize sets for later use.
empty_set = set()
print(empty_set)
print("#####################################################################################################################")

#Frozen Sets:
#Frozen sets are immutable sets. Once created, the elements cannot be added or removed from them. They are useful in situations where you need a set that cannot be modified.
frozen_set = frozenset({1, 2, 3})
print(frozen_set)
print("#####################################################################################################################")

#Set Comprehensions:
#Set comprehensions provide a concise way to create sets using a loop and an expression. They are similar to list comprehensions but produce sets instead of lists.
squares_set = {x**2 for x in range(1, 6)}
print(squares_set)
print("#####################################################################################################################")

#Subset, Superset, and Equal Sets:
#Sets can be compared for subset, superset, and equality relationships using operators like <=, >=, and ==.
set1 = {1, 2, 3}
set2 = {1, 2}
is_subset = set2 <= set1
is_superset = set1 >= set2
is_equal = set1 == set2
print(is_subset)
print(is_superset)
print(is_equal)
