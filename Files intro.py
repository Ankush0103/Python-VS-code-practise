
# f = open('Hello Ankush.txt', 'r')
f = open('Hello Ankush.txt') # if we dont give any notation then also file will run in read mode only(r).
data = f.read()
# data = f.read(5) # Return "Hello" only as it reads first 5 characters
print(data)
f.close()
# Use open function to read content of a file!