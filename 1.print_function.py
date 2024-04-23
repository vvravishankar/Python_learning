# In Python, the print() function is quite versatile and can be used in various ways to display output

#Printing a String:
print("Hello, world!")
print("#######################################################################################################")

#Printing Variables:
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)
print("#######################################################################################################")

#Printing Multiple Values with Formatting:
x = 10
y = 20
print("x =", x, "and y =", y)
print("#######################################################################################################")

#Printing with String Formatting:
name = "Bob"
age = 25
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")
print("#######################################################################################################")

#Printing to a File:
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)

print("#######################################################################################################")

#Printing with Escape Characters:
print("This is a newline.\nThis is a tab:\t")
print("#######################################################################################################")
