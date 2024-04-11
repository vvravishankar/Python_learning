# Using input() function: The input() function allows you to prompt the user for input. It reads input from the keyboard as a string.
name = input("Enter your name: ")

#Using command-line arguments: You can pass arguments to your Python script from the command line and access them using sys.argv if you import the sys module.
import sys
name = sys.argv[1]
age = int(sys.argv[2])
print("Hello,", name)
print("You are", age, "years old.")
#CLI COMMAND :- python script.py Alice 25
#sys.argv[0] would be 'script.py'
#sys.argv[1] would be 'Alice'
#sys.argv[2] would be '25'

#Using specific conversion functions: You can convert input to a specific type using functions like int(), float(), etc., after reading the input using input().
age = int(input("Enter your age: "))

#Using file input: You can read input from a file using file I/O operations like open(), read(), readline(), etc.
with open("input.txt", "r") as file:
    data = file.read()

#Using GUI frameworks: If you're building a graphical application, you can use GUI frameworks like Tkinter, PyQt, or PyGTK to create input fields where users can enter data.

#Using web-based forms: In web applications built with frameworks like Flask or Django, you can create HTML forms to accept user input, which is then processed by the server-side Python code.
