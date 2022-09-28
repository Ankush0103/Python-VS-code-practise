myDict = {
    "Fast": "In a quick manner",
    "Harry": "A coder",
    "Marks": [1, 2, 5],
   "anotherdict" : {'harry': 'Player'}
}

# print(myDict['Fast'])
# print(myDict["Harry"])
# print(myDict["Marks"])
myDict["Marks"] = [45,78]
print(myDict["Marks"]) # prints [45, 78] hence dict is mutable unlike tuple i.e. in dict we can change the values.  
print(myDict['anotherdict'])
# In dict we can storwe both strings and numbers.
print(myDict["anotherdict"]['harry'])