# In Python, the print() function is quite versatile and can be used in various ways to display output


#Printing a String:
print("Hello, world!")

#Printing Variables:
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)

#Printing Multiple Values with Formatting:    
x = 10
y = 20
print("x =", x, "and y =", y)

#Printing with String Formatting:
name = "Bob"
age = 25
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")

#Printing with Named Arguments:
print(name="Alice", age=30)

#Printing to a File:
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)

#Printing with Escape Characters:
print("This is a newline.\nThis is a tab:\t")


