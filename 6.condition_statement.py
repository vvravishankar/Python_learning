'''
Condition:
A condition is an expression that evaluates to either True or False.
It's used to control the flow of a program by executing certain blocks of code based on whether the condition is True or False.
Conditions are typically used in control flow statements such as if, elif (else if), and while loops.

Statement:
A statement is a complete instruction that performs some action.
In Python, statements can be simple (like assigning a value to a variable) or compound (like control flow statements or function definitions).
Examples of statements include variable assignments, function calls, loops, and conditional statements.
'''

'''
if statement:
The if statement is used to execute a block of code if a specified condition evaluates to True.
If the condition is true, the code block indented under the if statement is executed.
If the condition is false, the code block is skipped.
It can be followed by an optional elif or else block.

elif statement:
The elif (short for "else if") statement is used to check multiple conditions after the initial if statement.
It allows you to check additional conditions if the condition of the preceding if or elif statements evaluate to False.
It can appear multiple times in an if-elif-else block, and only the block corresponding to the first true condition is executed.

else statement:
The else statement is used in conjunction with an if statement to execute a block of code if the condition of the if statement evaluates to False.
It follows an if block and executes when the condition of the if block is false.
An else block cannot exist without an if block preceding it.
'''
x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#If x is greater than 0, the first print statement will execute.
#If x is equal to 0, the second print statement will execute.
#If x is less than 0, the third print statement will execute.

print("#################################################################################################################")
'''
while loop in Python is a control flow statement that allows you to repeatedly execute a block of code as long as a specified condition is true. It's often used when you need to iterate over a block of code until a certain condition is met.
'''
# Initialize a variable
count = 0
# Execute the loop as long as the condition (count < 5) is true
while count < 5:
    print("Count is:", count)
    # Increment the count variable by 1 in each iteration
    count += 1
print("Loop ended")

print("#################################################################################################################")
'''
for loop is a control flow statement used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence. 
for element in sequence:
    {}
Sequence: The sequence can be any iterable object in Python. It could be a list, tuple, string, range, or any other iterable data type.
Iteration: During each iteration of the loop, the for loop assigns the next element from the sequence to the variable element.
Loop Body: The block of code indented under the for statement is the loop body. It's executed once for each element in the sequence.
Termination: The loop terminates automatically after all elements in the sequence have been processed.
'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# for loop with range()
#range(stop):
#When you call range(stop), it generates a sequence of numbers from 0 up to, but not including, the stop value.
#The stop parameter specifies the end value of the range.
#If you only provide one argument to range(), it will assume that start is 0.
for i in range(5):
   print(i)
'''
outPut:-
  1
  2
  3
  4
'''
print("#################################################################################################################")
#range(start, stop):
#When you call range(start, stop), it generates a sequence of numbers from start up to, but not including, the stop value.
#The start parameter specifies the start value of the range, and the stop parameter specifies the end value.
#It will increment by 1 by default.
for i in range(1, 5):
    print(i)
    print(i)
'''
outPut:-
  1
  2
  3
  4
'''
print("#################################################################################################################")
#range(start, stop, step):
#When you call range(start, stop, step), it generates a sequence of numbers from start up to, but not including, the stop value, with a specified step value between each number.
#The start parameter specifies the start value of the range, the stop parameter specifies the end value, and the step parameter specifies the step size.
#It will increment by 1 by default if step is not provided.

for i in range(1, 5, 2):
   print(i)
'''
outPut:-
  1
  3
'''
print("#################################################################################################################")
#Negative step in range():
#You can also use a negative step value to generate a sequence in reverse order.
for i in range(5, 0, -1):
    print(i)
'''
outPut:-
  5
  4
  3
  2
  1
'''
print("#################################################################################################################")
#Using range() with other functions:
#range() is commonly used with for loops to iterate over a sequence of numbers.
#It can also be used in conjunction with other functions like list() to generate a list of numbers from the range
numbers = list(range(5))
print(numbers)  # Output: [0, 1, 2, 3, 4]





