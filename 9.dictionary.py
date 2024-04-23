#In Python, there is essentially only one type of dictionary, which is the built-in dict type. However, there are various ways to create dictionaries or variations of dictionaries to suit different needs or use cases

#Standard Dictionary (dict):
#This is the standard built-in dictionary type in Python, which stores key-value pairs. It is mutable, unordered, and does not allow duplicate keys.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)
print("#########################################################################################################################")

#OrderedDict (collections.OrderedDict):
#OrderedDict is a dictionary subclass available in the collections module. It maintains the order of insertion of key-value pairs, which means the order of elements in the dictionary is preserved.

from collections import OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered_dict)
print("#########################################################################################################################")


#DefaultDict (collections.defaultdict):
#defaultdict is another dictionary subclass available in the collections module. It is a subclass of the standard dictionary (dict) that provides a default value for keys that have not been set yet.

from collections import defaultdict
# Default value for missing keys is set to int()
default_dict = defaultdict(int)
print(default_dict)
print("#########################################################################################################################")


#FrozenDict (types.MappingProxyType):
#MappingProxyType is a wrapper class available in the types module. It creates a read-only view of a dictionary, preventing modifications to the original dictionary while still allowing access to its contents.

from types import MappingProxyType
original_dict = {'a': 1, 'b': 2}
frozen_dict = MappingProxyType(original_dict)
print(frozen_dict)

