# Day 5 String
# 1. Write a python program to check whether the string is Symmetrical or Palindrome.
def issymmetrical(s):
  return str(s) == str(s)[::-1]
s = input("Enter the required string: ")
print("String is symmetrical: ", issymmetrical(s))

# Palindrome function
def isPalindrome(s):
    return s == s[::-1]
ans = isPalindrome(s)
if ans:
    print("Yes it is palindrome")
else:
    print("Not palindrome")

# 2. Write a python program to reverse words in a given String.
string = input("Enter the word: ")
words = list(reversed(string))
print("".join(words))

# 3. Write a python program to remove ith character from a String.
string1 = "Hello"
print(string1)
string2 = string1.replace('e', '')
print(string2)

# 4. Write a python program to check whether a substring is present in a given String or not.
string = "Hello my name is Ankush!"
substring = input("Enter string ypu want to check: ")
if substring in string:
    print("Substring is present in the given string: ", substring)
else:
    print("Substring not present")

# 5. Write a python program to find the frequency of the words in a String.
string = "Hello my name is xyz Hello what is your name Hello"
sl = []
sl = string.split()
sfreq = [sl.count(s) for s in sl]
print(dict(zip(sl, sfreq)))

# 6. Write a python program to print even-length words in a string.
string = input("Enter the string: ")
s1 = string.split()
print("Even length string: ")
for i in s1:
    if len(i) % 2 == 0:
        print(i)

# ADP1. Write a python program to remove all duplicates from a given String.
from collections import OrderedDict
def remove_duplicate(s):
    return "".join(OrderedDict.fromkeys(s))
s = input("Enter the string: ")
print(s)
print("After removing duplicates: ", remove_duplicate(s))

# ADP2. Write a python program to find the maximum frequency character in String.
str = "HelloWorld"
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxfreqchar = max(freq, key=freq.get)
print(str)
print(maxfreqchar, "is the maximum frequency character with frequency of",
      freq[maxfreqchar])

# ADP3. Write a python program to generate random strings until a given string is generated.
import string
import time
import random
# all possible characters including lowercase, uppercase and punctuations
possibleChar = string.ascii_lowercase + \
    string.digits + string.ascii_uppercase + ' ., !?;:'
t = "test"
attemptThis = ''.join(random.choice(possibleChar) for i in range(len(t)))
attemptNext = ''

done = False
iteration = 0

while done == False:
    print(attemptThis)

    attemptNext = ''
    done = True

    # if matches with string  change index
    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            done = False
            attemptNext += random.choice(possibleChar)
        else:
            attemptNext += t[i]

    # increase iteration
    iteration = iteration + 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched after ", iteration, " iterations")

# ADP4. Write a python program to find the permutation of a given string using built-in function.
from itertools import permutations
s = input("Enter the string you want to have permuations on: ")
words = [''.join(p) for p in permutations(s)]
print("Permutated words are: ", words)

# ADP5. Write a python program to check whether a string can become empty by recursive deletion using String slicing.
def str_empty(str, pattern):
    if len(str) == 0 and len(pattern) == 0:
        return 'true'
    if len(pattern) == 0:
        return 'true'
    while (len(str) != 0):
        pos = str.find(pattern)
        if(pos == (-1)):
            return 'false'
        str = str[0:pos] + str[pos + len(pattern):]
    return 'true'
   
str = input("Enter the string : ")
pattern = input("Enter the sub-string : ")
print("Returns true if sring can become empty, else false")
print(str_empty(str, pattern))

# ADP6. Write a python program to find all duplicate characters in string.
string = "HelloWorld"
# initializing a list to append all the duplicate characters
duplicates = []
for char in string:
    # checking whether the character have a duplicate or not str.count(char) returns the frequency of a char in the str
    if string.count(char) > 1:
        # appending to the list if it's already not present
        if char not in duplicates:
            duplicates.append(char)

print("Duplicate characters are: ", duplicates)
