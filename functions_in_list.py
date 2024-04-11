# Common function used with LIST

my_list = ['apple', 'banana', 'orange', 'grapes']

#append(): Adds an element to the end of the list.
my_list.append('kiwi')
print(my_list)  # Output: ['apple', 'banana', 'orange', 'grapes', 'kiwi']

#extend(): Extends the list by appending elements from another iterable.
my_list.extend(['melon', 'pineapple'])
print(my_list)  # Output: ['apple', 'banana', 'orange', 'grapes', 'melon', 'pineapple']

#insert(): Inserts an element at a specified position.
my_list.insert(2, 'mango')
print(my_list)  # Output: ['apple', 'banana', 'mango', 'orange', 'grapes', 'melon', 'pineapple']

#remove(): Removes the first occurrence of a value from the list.
my_list.remove('orange')
print(my_list)  # Output: ['apple', 'banana', 'mango', 'grapes', 'melon', 'pineapple']

#pop(): Removes the element at the specified position and returns it. If no index is specified, removes and returns the last item in the list.
popped_element = my_list.pop(2)
print(popped_element)  # Output: 'mango'
print(my_list)  # Output: ['apple', 'banana', 'grapes', 'melon', 'pineapple']

#index(): Returns the index of the first occurrence of a value in the list.
idx = my_list.index('banana')
print(idx)  # Output: 1

#count(): Returns the number of occurrences of a value in the list.
count = my_list.count('grapes')
print(count)  # Output: 1

#sort(): Sorts the list in ascending order (or descending with reverse=True).
my_list.sort()
print(my_list)  # Output: ['apple', 'banana', 'grapes', 'melon', 'pineapple']

#reverse(): Reverses the elements of the list in place.
my_list.reverse()
print(my_list)  # Output: ['pineapple', 'melon', 'grapes', 'banana', 'apple']

#copy(): Returns a shallow copy of the list.
new_list = my_list.copy()
print(new_list)  # Output: ['pineapple', 'melon', 'grapes', 'banana', 'apple']

#clear(): Removes all elements from the list.
my_list.clear()
print(my_list)  # Output: []
##############################################################################################
my_list_new = [3, 1, 4, 1, 5, 9, 2, 6]

#len(): function is not specific to lists but is commonly used with them to get the length or the number of elements in the list.
length_of_list = len(my_list_new)
print(length_of_list)  # Output: 8


#max(): Returns the maximum value in the list.
max_value = max(my_list_new)
print(max_value)  # Output: 9

#min(): Returns the minimum value in the list.
my_list_new = min(my_list_new)
print(min_value)  # Output: 1

#sum(): Returns the sum of all values in the list.
sum_of_list = sum(my_list_new)
print(sum_of_list)  # Output: 31

###############################################################################################

#zip(): function is used to combine multiple iterables (such as lists) into tuples.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = zip(list1, list2)
print(list(zipped))  # Output: [('a', 1), ('b', 2), ('c', 3)]
#If the input iterables are of different lengths, zip() stops when the shortest iterable is exhausted.

# unzip : You can also unzip a zipped iterable using the zip() function in conjunction with the unpacking operator *:
zipped = [('a', 1), ('b', 2), ('c', 3)]
unzipped = list(zip(*zipped))
print(unzipped)  # Output: [('a', 'b', 'c'), (1, 2, 3)]









