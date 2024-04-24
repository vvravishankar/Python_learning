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

###################################################################################################################################################
# You are given a string. Your task is to count the occurrences of each character in the string and store them in a dictionary where the keys are the characters and the values are their respective counts.

string = "ANAND"
char_count = {}

for alphabet in string:
    if alphabet in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
###################################################################################################################################################
#You are given a text string containing words separated by spaces. Your task is to create a Python script to analyze the frequency of each word in the text and generate a dictionary that maps each unique word to its count.
text = "hi he hi he he hoo hoo"
words = text.lower().split()
print(words)
word_count_dict = {}
for ele in words:
    if ele in word_count_dict:
        word_count_dict[ele] += 1
    else:
         word_count_dict[ele] = 1

print(word_count_dict)

####################################################################################################################################################
#You are given a string string. Your task is to write a Python script to determine the length of the string using a loop-based approach and not the built-in len() function.
string = 'Ravi'
count = 0
for ele in string:
    count = count+1
print(f"length of string is : {count}")

# in build function
print(len(string))

###################################################################################################################################################
#You are given a positive integer n. Your task is to write a Python script to compute the factorial of n using a recursive function.
def factorial(num):
    if num == 0:
        return 0
    else:
        result = 1
        for i in range(1,num+1):
           result =  i * result
        return result
print(f"The factorical of number is :- {factorial(6)}")

###################################################################################################################################################
#You are given a string string. Your task is to write a Python function to determine whether the given string is a palindrome or not.
def palindrom(string):
    if string  == string[::-1]:
        print(f'{string} is a plaindrom ')
    else:
        print(f'{string} is not a plaindrom ')
palindrom("NITIN")

###################################################################################################################################################
#You are given the first two numbers of a Fibonacci sequence: [0, 1]. Your task is to write a Python script to generate the next n numbers of the Fibonacci sequence and store them in a list.
fib_seq = [0,1]
for i in range(2,5):
    next = fib_seq[i-2] + fib_seq[i-1]
    fib_seq.append(next)
print(fib_seq)




