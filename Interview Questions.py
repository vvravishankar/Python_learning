# Python Interview Question




# Given a list of words: list_of_words = ["flower", "flow", "flight"], write a Python script that finds and prints the common letters among these words.
list_of_words = ["flower", "flow", "flight"]
# you loop through each word in the list and convert it into a set of characters:
list = []
for ele in list_of_words:
    #converted to set
    list.append(set(ele))
# You print both list and the unpacked version of list
print(list)
print(*list)
# Next, you find the intersection of all sets in list:
comm = set.intersection(*list)
print(comm)