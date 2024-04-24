
#Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). OOP allows developers to structure code in a more modular and reusable way by organizing it around objects that represent real-world entities or abstract concepts. Here are some key concepts of OOP:

#Classes and Objects:
#A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that all objects of that class will have. An object is an instance of a class. It represents a specific instance of the class and can access the attributes and methods defined in the class.
# To use varibale in method/object we need permission of self to do it.

class MyClass:
    def method1(self):
        print("This is method 1")

    def method2(self):
        print("This is method 2")

    def method3(self):
        print("This is method 3")

# Creating an instance of MyClass
obj = MyClass()

# Calling multiple methods
obj.method1()
obj.method2()
obj.method3()

# Constructor
#A constructor in Python is a special method within a class that is automatically called when a new instance of the class is created. It's used to initialize the object's attributes or perform any setup tasks that are necessary before the object can be used. In Python, the constructor method is always named __init__().
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Creating an instance of the Car class
car = Car("Toyota", "Corolla")

# Accessing attributes initialized in the constructor
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Corolla


#Encapsulation:
#Encapsulation is the bundling of data and methods that operate on that data within a single unit (i.e., a class). It hides the internal state of an object and only exposes a public interface for interacting with it.Encapsulation helps to prevent external code from directly modifying the internal state of an object, promoting data integrity and reducing coupling between different parts of a program.

class BankAccount:
    # methods
    def deposit(self, balance, amount):
        balance += amount
        return balance

    def withdraw(self, balance, amount):
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds")
        return balance

    def get_balance(self, balance):
        return balance

# Creating an object of the BankAccount class
account = BankAccount()

# Accessing and modifying balance through methods
balance = 1000
balance = account.deposit(balance, 500)
balance = account.withdraw(balance, 200)
print(account.get_balance(balance))  # Output: 1300

#Inheritance:
#Inheritance is a mechanism that allows a class (subclass) to inherit attributes and methods from another class (superclass).Subclasses can extend or override the behavior of their superclass, allowing for code reuse and the creation of hierarchical relationships between classes.

# Single level Inheritance
# Create a class
class A:
    def displayA(self):
        print("I am from class:A")
# inherit the class A in to class B
class B(A):
    def displayB(self):
        print("I am from class:B")

# create objects of classB
obj = B()
obj.displayB()
# we can call methods of class A from object of B because class A is Inherited by class B
obj.displayA()

# Multiple level  Inheritance
# Create a class
class A:
    def displayA(self):
        print("I am from class:A")
# inherit the class A in to class B
class B(A):
    def displayB(self):
        print("I am from class:B")

# inherit the class A in to class B
class C(B):
    def displayC(self):
        print("I am from class:C")

# create objects of classC
obj = C()
obj.displayC()
# we can call methods of class B from object of C because class C is Inherited by class B
obj.displayB()
# we can call methods of class A from object of C because class C is Inherited by class B abd class B inherit Class A
obj.displayA()


#Polymorphism:
#Polymorphism refers to the ability of different classes to be treated as instances of a common superclass.It allows objects of different classes to be used interchangeably, as long as they share a common interface or inheritance hierarchy.Polymorphism enables more flexible and modular code by allowing methods to operate on objects of different types without needing to know their specific class.

# Create a class
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function that accepts any object with a speak method
def make_sound(animal):
    return animal.speak()

# Creating objects of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the make_sound function with different objects
print(make_sound(animal))  # Output: Animal speaks
print(make_sound(dog))     # Output: Woof!
print(make_sound(cat))     # Output: Meow!


# Function Overloading
# create the class which excepts the variable
class A:
    def displayinfo(self,name = ""):
        print("welcome to " + name)

# Create object of class
obj= A()
# calling the method without passing variable.
obj.displayinfo()
# passing the variable
obj.displayinfo("Ravi")

# Function Overriding
# create the class
class A:
    def displayinfo(self):
        print("welcome to RAVI")

class B(A):
    def displayinfo(self): # same method name in both class
        print("welcome to NEHA")
    # to call the method of parent class
        super().displayinfo()

# Create object of class
obj= B()
# calling the method
obj.displayinfo()



#Abstraction:
#Abstraction is the process of simplifying complex systems by focusing on essential properties while hiding unnecessary details.In OOP, abstraction is achieved through the use of abstract classes and interfaces, which define a common interface for a group of related classes without specifying their implementation details.
# we cant create the object of Abstract class
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 5 * 4  # Simplified for demonstration

# Creating an object of the Rectangle class
rectangle = Rectangle()

# Calling the area method
print(rectangle.area())  # Output: 20





