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
