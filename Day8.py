# File Handling
# 1. Write a Python program to read the content from a text file line by line, word by word, character by character.
f = open('File1.txt')
#data = f.read(20)# reads upto 20 string length
data = f.read()
print(data)
f.close()

# 2. Write a Python Program to append the content of one text file to another
f = open('File1.txt', 'a')
f.write("\nI am appending")
f = open('File1.txt')
dt = f.read()
print(dt)
f.close()

# 3. Write a Python program to create a file with 100 random numbers less than 1000. then create another 2 files to store even and odd numbers from the first file
import random
for i in range (100):
    y = random.randrange(1000)
print(y)

import random
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)
f = open('File3.txt', 'a')
f.write('randomlist')
f = open('File3.txt')
data = f.read()
print(data)
f.close()

# 4.Write a Python program to convert from JSON to Python 
import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
python_dict =  json.loads(jobj_dict)
python_list = json.loads(jobj_list)
python_str =  json.loads(jobj_string)
python_int =   json.loads(jobj_int)
python_float = json.loads(jobj_float)

print("Python dictionary: ", python_dict)
print("Python list: ", python_list)
print("Python string: ", python_str)
print("Python integer: ", python_int)
print("Python float: ", python_float)

# 5. Write a Python program to read each row from a given CSV file and print a list of strings
import csv
with open('annual-enterprise-survey-2021-financial-year-provisional-csv.csv') as file:
    read = csv.reader(file)
    for row in read:
        print(row)

# ADP1. Write a Python program to convert Python objects into JSON strings.
import json

python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)

print("json dict : ", json_dict)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true : ", json_t)
print("json false : ", json_f)
print("json null ; ", json_n)

# ADP 2. Write a Python program to read specific columns of a given CSV file and print the content of the columns.
import csv
with open('annual-enterprise-survey-2021-financial-year-provisional-csv.csv') as file:
    read = csv.DictReader(file)
    for column in read:
        print(column['Year'], column['Value'])

# ADP3. Write a Python program to write a Python list of lists to a CSV file. After writing the CSV file read the CSV file and display the content.
import csv
# data to be written row-wise in csv file
data = [['Hello'], [10], ['World']]
# opening the csv file in 'w+' mode
file = open('ADP3.csv', 'w+', newline ='')
# writing the data into the file
with file:   
    write = csv.writer(file)
    write.writerows(data)