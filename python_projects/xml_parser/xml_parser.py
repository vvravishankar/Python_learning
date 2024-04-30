import xml.etree.ElementTree as ET
import pandas as pd

# read the XML
mytree = ET.parse(r"C:\Users\VVRAVISH\Downloads\sample2.xml")
myroot = mytree.getroot()

# get the root
print(myroot)
# get the length of element
print(len(myroot))


# define the list for DF creation
data = []

def xml_parser(element, item):
    if len(list(element)) == 0:
        item[element.tag] = element.text
        #print(item[element.tag] )
    else:
        for child in list(element):
            xml_parser(child,item)

# itrate through XMl elements

for child in myroot:
    item = {}
    xml_parser(child,item)
    data.append(item)
#print(data)
df = pd.DataFrame(data)
print(df)
