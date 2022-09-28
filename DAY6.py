# Day 6 Function and Recursion
'''1.Write a function calculation() such that it can accept two variables and calculate the
addition and subtraction of them. And also it must return both addition and subtraction in a
single return call.'''
def calculation(a, b):
    print("Addition of numbers are: ", a+b, "and subtraction of numbers are: ", a-b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calculation(a,b)

# 2. Write a Python function to find the Maximum of three numbers.
def maximum(a, b, c):
    print("Maximum of 3 numbers are: ", max(a,b,c))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("enter third number: "))
maximum(a,b,c)

# 3. Write a Python function to sum all the numbers in a List.
def sum(l):
    sum= 0
    for i in l:
         sum+= i
    return sum
list=[1,2,3,4]
print(list)
print("Sum of list is: ", sum((list)))

# 4. Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(num):
    if (num<=1):
        return False
    elif (num==2):
        return True
    else:
        for x in range(2, num):
            if(num % x==0):
                return False
        return True
n = int(input("Enter a number: "))             
print("Number is prime, TRUE OR FALSE: ", prime(n))

# 5. Write a recursive function to calculate the sum of numbers from 0 to N.
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
a = int(input("enter a number: "))
if a < 0:
   print("Incorrect input, Enter a positive number")
else:
   print("The sum is: ",recur_sum(a))
# Method 2
def recur_sum(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum 
a = int(input("enter a number: "))
if a < 0:
   print("Incorrect input, Enter a positive number")
else:
   print("The sum is: ",recur_sum(a))

# 6. Write a recursive function in Python to calculate the geometric sum of n-1
def geosum(n):
    if n<0:
        return 0
    else:
        return 1/(pow(2,n)) + geosum(n-1)
a = int(input("enter a number: "))
print("Geometric sum is: ", geosum(a))

# ADP 1. Write a Python function to check whether a number is perfect or not.
# Perfect number is that number whose divisors(except the number itself) sum = Original number
def perfect(n):
    sum = 0
    for i in range(1, n):
        if n%i==0:
            sum += i
    return sum == n
n = int(input("Enter a number: "))
print("Number is Perfect Number, True or False: ", perfect(n))


# ADP 2. Write a Python function that prints out the first n rows of Pascal's triangle.
def fact(num):
  f = 1
  for i in range(1, num+1):
    f = f*i
  return f
n = int(input("Enter number of rows: "))
for i in range(n):
  for col in range(n-1, i, -1):
    print(end=" ")
  for col in range(i+1):
    val = int(fact(i)/(fact(col)*fact(i-col)))
    print(val, end=" ")
  print()

# ADP 3. Write a Python function to count the even, odd numbers in a given array of integers using Lambda
array = [1,2,3,4,5,6,7]
print(array)
even_arr = len(list(filter(lambda x: (x%2==0), array)))
odd_arr = len(list(filter(lambda x: (x%2!=0), array)))
print("Even integers in array are: ", even_arr)
print("Odd integers in array are: ", odd_arr)

# ADP 4. Write a python function to sort list of dictionaries by values using lambda function
ld = [{"name" : "Ankur", 'roll': 100, 'Stream':'CSBS'},
      {"name" : "Ruchita", 'roll': 102, 'Stream':'IT'},
      {"name" : "Rohit", 'roll': 101, 'Stream':'ME'},
      {"name" : "Ankit", 'roll': 103, 'Stream':'CSE'}]
print(ld)
sort_ld = sorted(ld, key = lambda x : x['name'])
print("Sorted list of dictionary: ")
print(sort_ld)

# ADP 5. Write a recursive function in Python to calculate the value of 'a' to the power 'b'.
# we evaluate a^b
def power(a, b):
    if(b==1 or a==1):
        return a
    if(b!=1 and a!=1):
        return(a*power(a, b - 1))
a = int(input("Enter the base number: "))
b = int(input("Enter the exponential number: "))
print("a^b is: ", power(a, b))

# ADP 6. Write a recursive function in Python to find the greatest common divisor (gcd) of two integers.
# we evaluate gcd(a, b)
def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Greatest Common divisor of a and b is: ", gcd(a, b))

# ADP 7. Write a recursive function in Python to evaluate nCr = n! / r! * (n – r)!
def comb(n, r):
    if(n<r):
        return 0
    if(r==1):
        return n
    if(r==n):
        return 1
    if(n==1):
        return 1
    return comb(n-1, r-1) + comb(n-1, r)

n = int(input("Enter the n number: "))
r = int(input("Enter the r number: "))
print("nCr is: ", comb(n, r))