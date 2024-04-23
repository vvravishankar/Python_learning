# Common method used with tuple

#count(value): Returns the number of occurrences of a specified value in the tuple.
my_tuple = (1, 2, 3, 4, 2, 2)
count_2 = my_tuple.count(2)
print(count_2)  # Output: 3
print("####################################################################################")

#index(value[, start[, end]]): Returns the index of the first occurrence of a specified value in the tuple.
my_tuple = (1, 2, 3, 4, 5)
index_3 = my_tuple.index(3)
print(index_3)  # Output: 2
print("####################################################################################")


#max(tuple): Returns the largest element in the tuple.
my_tuple = (10, 20, 30, 40, 50)
max_value = max(my_tuple)
print(max_value)  # Output: 50
print("####################################################################################")


#min(tuple): Returns the smallest element in the tuple.
my_tuple = (10, 20, 30, 40, 50)
min_value = min(my_tuple)
print(min_value)  # Output: 10
print("####################################################################################")


#sum(tuple): Returns the sum of all elements in the tuple.
my_tuple = (10, 20, 30, 40, 50)
sum_values = sum(my_tuple)
print(sum_values)  # Output: 150
print("####################################################################################")


#len(tuple): Returns the number of elements in the tuple.
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print(length)  # Output: 5
print("####################################################################################")


#sorted(tuple): Returns a new sorted list from the elements of the tuple.
my_tuple = (50, 20, 40, 10, 30)
sorted_list = sorted(my_tuple)