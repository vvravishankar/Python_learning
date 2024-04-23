# Common method used with set


#add(element): Adds a single element to the set. If the element is already present, it does nothing.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
print("#####################################################################################################################")

#update(iterable): Adds elements from an iterable (such as a list or another set) to the set.
my_set = {1, 2, 3}
my_set.update([4, 5])
print(my_set)
print("#####################################################################################################################")

#remove(element): Removes a specified element from the set. Raises a KeyError if the element is not present.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
print("#####################################################################################################################")

#discard(element): Removes a specified element from the set if it is present. If the element is not present, it does nothing.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)
print("#####################################################################################################################")

#pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
my_set = {1, 2, 3}
popped_element = my_set.pop()
print(my_set)
print("#####################################################################################################################")

#clear(): Removes all elements from the set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)
print("#####################################################################################################################")

#copy(): Returns a shallow copy of the set.
my_set = {1, 2, 3}
new_set = my_set.copy()
print(my_set)
print("#####################################################################################################################")

#difference(set): Returns a new set containing elements that are present in the first set but not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)
print("#####################################################################################################################")

#intersection(set): Returns a new set containing elements that are present in both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)
print("#####################################################################################################################")

#union(set): Returns a new set containing all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
