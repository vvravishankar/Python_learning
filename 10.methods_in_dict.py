# Common method used with Dicitonary

my_dict = {'a': 1, 'b': 2, 'c': 3}

#clear(): Removes all items from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}
print("###############################################################################################")

my_dict = {'a': 1, 'b': 2, 'c': 3}
#copy(): Returns a shallow copy of the dictionary.
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
print("###############################################################################################")


#get(key[, default]): Returns the value associated with the specified key. If the key is not found, it returns the default value (None by default).
value = my_dict.get('a')
print(value)  # Output: 1
print("###############################################################################################")

#items(): Returns a view object that displays a list of a dictionary's (key, value) tuple pairs.
items_view = my_dict.items()
print(items_view)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
print("###############################################################################################")

#keys(): Returns a view object that displays a list of all the keys in the dictionary.
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])
print("###############################################################################################")

#values(): Returns a view object that displays a list of all the values in the dictionary.
values_view = my_dict.values()
print(values_view)  # Output: dict_values([1, 2, 3])
print("###############################################################################################")

#pop(key[, default]): Removes and returns the value associated with the specified key. If the key is not found, it returns the default value (or raises KeyError if default is not provided).
value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}
print("###############################################################################################")

#popitem(): Removes and returns the last inserted (key, value) pair as a tuple.
key, value = my_dict.popitem()
print(key, value)  # Output: c 3
print(my_dict)  # Output: {'a': 1, 'b': 2}
print("###############################################################################################")

#update([other]): Updates the dictionary with the key-value pairs from another dictionary or iterable.
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
print("###############################################################################################")

#setdefault(key[, default]): Returns the value associated with the specified key. If the key is not found, it inserts the key with the specified default value (None by default) and returns the default value.
my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('c', 3)
print(value)  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
print("###############################################################################################")

#fromkeys(seq[, value]): Creates a new dictionary with keys from seq and values set to value (None by default).
new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
