# DAY 3 Sets and Dictionaries
# Sets are unordered, unidexed, unmutable and allows no duplicates.
set = {'apple', 'orange', 'cherry'}
print(set)
set.add("mango")
print(set)
print(len(set))

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# 1. Write a python program to add member(s) in a set.
set = {'apple', 'orange', 'cherry'}
print(set)
print("Adding a single member")
set.add("mango")
print(set)
print("Adding multiple members at once")
set.update(["banana", "pineapple"])
print(set)

# 2. Write a python program to add a list of elements to a given set.
set = {1, 2, 3}
print(set)
list = [4, 5, 6]
set.update(list)
print(set) 

# 3. Write a python program to find the length of a set.
set = {'Hello', 1, 2, 4, 'Ankur'}
a = len(set)

print("length of set is", a)

# 4. Write a python program to check if two given sets have no elements in common.
set1 = {1, 2, 3, 'Ankur'}
set2 = {4, 5, 6, 'Ankur'}
set3 = {7, 8, 1}

print("If disjoint returns true then no common elements, else false then common elements")
print("Comapring set1 and set2")
print(set1.isdisjoint(set2))

print("Comapring set2 and set3")
print(set2.isdisjoint(set3))

print("Comapring set3 and set1")
print(set2.isdisjoint(set3))

# Dictionaries are ordered, indexed, changeable, no duplicates.
a = {"name": "Ankur", "from": "India", "marks": [98, 97]}
print(a)
print(a.values())
print(a.keys())
a.update({"Address": "Kolkata"})
print(a)
print(a.get("name"))

# 5. Write a python program to extract unique values from a dictionary.
dict1 = {'A' : [1, 2, 3, 4],
             'B' : [4, 3, 5, 7],
             'C' : [7, 8, 4, 13],
             'D' : [10, 11, 2, 1]}

print(dict1)
result = list(sorted({ele for val in dict1.values() for ele in val}))   
print("The unique values list is : " , result)  

# 6. Write a python program to remove a key from dictionary
dict1 = {'A' : 1, 'B' : 4, 'C' : 7, 'D' : 6}

print(dict1)
# del dict1['A']
# print(dict1)
rem_val= dict1.pop('A')
print(dict1)

# 7. Write a python program to insert at the beginning in ordered dictionary.
from collections import OrderedDict  
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
dic1.update({"D": '400'})
print(dic1)
dic1.move_to_end("D", last=False)
print ("Resultant Dictionary :")
print(dic1)

# ADP 1. Write a python program to check if a set is a subset of another set.
set1 = {'Apple', 'Mango', 'Banana'}
set2 = {'Apple', 'Mango'}
set3 = {'Banana'}

print("If sets are subset of another then it will print true else false")
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set2.issubset(set3))
print(set3.issubset(set1))

# ADP 2. Write a python program to create a shallow copy of sets. 
set1 = {1, 2, 3, 4} 
set2 = set1.copy()  
print(set2)
# Shallow copy
set1 = {"Red", "Green"}
set2 = {"Green", "Red"}

#A shallow copy
set3 = set1.copy()
print(set3)

# ADP 3. Write a python program to clear a set.
set = {1, 2, 3}
print(set)
print(set.clear())

#ADP 4. Python Program to convert lists of tuples into dict.
listoftup = [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
dictres = {}

for (key, value) in listoftup:
    dictres.setdefault(key, []).append(value)

print(dictres)

#ADP 5. Write a python program to sort dictionaries by key or value.
color_dict = {'red':'apple',
          'green':'guava',
          'black':'jamun',
          'yellow':'mango'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
	
#ADP 6. Write a python program to sort dictionaries by key and values.
dic = {'Key2': [5, 3, 7], 
             'Key3': [11, 4, 2, 6], 
             'Key1': [10, 9]}
  
print(dic)
  
# Sort Dictionary key and value List Using sorted() and loop
sort_dict = {}
for key in sorted(dic):
    sort_dict[key] = sorted(dic[key])
 
print(sort_dict)