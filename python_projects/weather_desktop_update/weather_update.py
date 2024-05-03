# use to read url from web
import requests
# use to parse html
from bs4 import BeautifulSoup
# use for desktop notifier
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()

# URL to fetch weather information
url = 'https://weather.com/en-IN/weather/today/l/21.25,81.63?par=google'

# Fetch the HTML content from the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the location and temperature tags
tag1 = soup.find_all("h1", class_="CurrentConditions--location--1YWj_")
tag2 = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")

# Print the type and content of the tags
print(type(tag1))
print(tag1)

print(type(tag2))
print(tag2)

# Convert tags to strings for easy manipulation
temp1 = str(tag1)
temp2 = str(tag2)

# Extract city, state, and temperature from the strings use slicing
city = temp1[48:61]
print(city)
state = temp1[63:73]
print(state)
temp = temp2[82:84]
print(temp)

# Prepare the result string
#result = f"City = {city}\nState = {state}\nTemp = {temp} degreeCel"
result = "City = " + city + "\nState = " + state + "\nTemp = " + temp + " degreeCel"

# Display the notification
n.show_toast("Live Weather Update",
             result, duration=10)
