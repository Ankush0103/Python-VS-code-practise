# f = open('Hello Ankush.txt', 'r')
f = open('Hello Ankush.txt') # if we dont give any notation then also file will run in read mode only(r).
# First line
data = f.readline() # prints only first line.
print(data)
# Second Line
data = f.readline() # prints next line.
print(data)
# Third Line
data = f.readline()
print(data)
# Fourth Line 
data = f.readline()
print(data)
# Fifth Line
data = f.readline()
print(data)
f.close()
# Use open function to read content of a file!