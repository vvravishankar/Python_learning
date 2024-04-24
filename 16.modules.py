#In Python, a module is a file containing Python code. It can define functions, classes, and variables, and can also include runnable code. Modules allow you to organize your Python code into reusable units, making it easier to manage and maintain.

#Creating Modules: To create a module, you simply write Python code in a .py file. The name of the file (without the .py extension) becomes the name of the module.

# module.py
def greet(name):
    print("Hello, " + name)

#Importing Modules: Once you've created a module, you can use the import statement to make its functionality available in other Python scripts or modules. There are several ways to import modules, including import module_name, from module_name import ..., and import module_name as alias.

# main.py
import module

#Module Namespace: When you import a module, its contents become available in a namespace associated with the module's name. You can then access functions, classes, and variables defined in the module using dot notation (e.g., module_name.function_name).

module.greet("Alice")  # Output: Hello, Alice

#Standard Library Modules: Python comes with a rich standard library, which includes a wide range of modules for performing various tasks, such as file I/O, networking, data manipulation, and more. You can use these modules in your Python programs without needing to install any additional packages. The Python Standard Library provides a vast array of modules covering a wide range of functionalities. Here are some examples of commonly used standard library modules along with a brief description of their purposes:

#os: Provides operating system interfaces, allowing you to interact with the operating system, such as managing files and directories, and executing system commands.
import os
os.listdir('.')  # List files in the current directory

#sys: Provides access to some variables used or maintained by the Python interpreter, as well as functions that interact with the interpreter.
import sys
sys.version  # Get the Python version

#math: Provides mathematical functions and constants for performing mathematical operations.
import math
math.sqrt(25)  # Calculate the square root of 25

#random: Generates pseudo-random numbers for various distributions.
import random
random.randint(1, 10)  # Generate a random integer between 1 and 10

#datetime: Provides classes for manipulating dates and times.
import datetime
current_time = datetime.datetime.now()

#json: Provides functions for encoding and decoding JSON data.
import json
data = {'name': 'John', 'age': 30}

#json_string = json.dumps(data)  # Convert dictionary to JSON string
re: Provides support for working with regular expressions.
import re
pattern = r'\b\w{4}\b'  # Match 4-letter words
re.findall(pattern, 'Hello world')  # Output: ['Hello', 'world']

#urllib: Provides functions for working with URLs, making HTTP requests, and handling HTTP responses.
import urllib.request
response = urllib.request.urlopen('https://www.example.com')

#collections: Provides additional data structures beyond the built-in types, such as dictionaries, lists, and tuples.
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

#csv: Provides classes for reading and writing CSV files.
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#Third-party Modules: In addition to the standard library, there are thousands of third-party modules available for Python, which you can install using package managers like pip. These modules provide additional functionality for tasks such as web development, scientific computing, machine learning, and more.

#Requests: A versatile HTTP library for making HTTP requests in Python, with support for various HTTP methods, headers, cookies, and authentication.
import requests
response = requests.get('https://api.github.com/user')

#Pandas: A powerful data analysis and manipulation library built on top of NumPy. It provides data structures like DataFrame and Series, as well as functions for reading and writing data in various formats.
import pandas as pd
data = pd.read_csv('data.csv')

#NumPy: A fundamental package for scientific computing in Python. It provides support for multidimensional arrays, mathematical functions, linear algebra operations, and random number generation.
import numpy as np
array = np.array([[1, 2], [3, 4]])

#Matplotlib: A plotting library for creating static, interactive, and animated visualizations in Python. It supports a wide variety of plot types and customization options.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()

#Scikit-learn: A machine learning library that provides simple and efficient tools for data mining and data analysis. It includes various algorithms for classification, regression, clustering, and dimensionality reduction.
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#Django: A high-level web framework for building web applications in Python. It follows the MVC (Model-View-Controller) pattern and provides features like URL routing, template engine, and database ORM.
# Django commands, e.g., creating a new project
django-admin startproject myproject

#Flask: A lightweight web framework for building web applications in Python. It is designed to be simple and easy to use, with support for routing, templates, and web server integration.
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

#TensorFlow: An open-source machine learning framework developed by Google for building and training neural networks. It provides APIs for both high-level and low-level model building.
import tensorflow as tf

#Pygame: A set of Python modules designed for writing video games. It provides functions for graphics rendering, event handling, sound playback, and more.
import pygame

#Beautiful Soup: A library for parsing HTML and XML documents, extracting data, and navigating the parse tree. It is commonly used for web scraping tasks.
from bs4 import BeautifulSoup
