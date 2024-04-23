# Lists are mutable, meaning they can be modified after creation. Elements can be added, removed, or modified.

#Basic Lists:
#Basic lists contain elements of the same type, such as integers, strings, or floats.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
print(numbers)
print(fruits)
print("############################################################################################################")

#Nested Lists:
#Nested lists contain other lists as elements, creating a hierarchical structure.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table = [['Name', 'Age', 'City'], ['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles']]
print(matrix)
print(table)
print("############################################################################################################")

#Mixed-Type Lists:
#Mixed-type lists contain elements of different data types, including numbers, strings, and even other data structures.
mixed_list = [1, 'apple', True, [2.5, 'banana']]
print(mixed_list)
print("############################################################################################################")

# indexing
my_list = ['apple', 'banana', 'orange', 'grapes']
#Positive Indexing:
#Positive indexing starts from 0 and increments by 1 for each subsequent element.
print(my_list[0])   # Output: 'apple' (first element)
print(my_list[2])   # Output: 'orange' (third element)
print("############################################################################################################")

#Negative Indexing:
#Negative indexing starts from -1 for the last element and decrements by 1 for each preceding element.
#Negative indices count backward from the end of the list.
print(my_list[-1])   # Output: 'grapes' (last element)
print(my_list[-2])   # Output: 'orange' (second to last element)
print("############################################################################################################")

#Slicing:
#Slicing allows you to access a subset of elements within the list.
#You can specify a range of indices using the syntax start:end, where start is inclusive and end is exclusive.
#Omitting start or end indicates the beginning or end of the list, respectively.

print(my_list[1:3])   # Output: ['banana', 'orange'] (elements from index 1 to 2)
print(my_list[:2])    # Output: ['apple', 'banana'] (elements from index 0 to 1)
print(my_list[2:])    # Output: ['orange', 'grapes'] (elements from index 2 to end)
print("############################################################################################################")

#Reversing a List:
#You can reverse a list using the [::-1] slicing notation.
#This notation creates a new list with elements in reverse order without modifying the original list.
reversed_list = my_list[::-1]
print(reversed_list)  # Output: ['grapes', 'orange', 'banana', 'apple']
#OR
my_list.reverse()
print(my_list)  # Output: ['grapes', 'orange', 'banana', 'apple']
print("############################################################################################################")

#Index Error:
#Trying to access an index outside the range of the list will result in an IndexError.
print(my_list[4])   # IndexError: list index out of range
print("############################################################################################################")


