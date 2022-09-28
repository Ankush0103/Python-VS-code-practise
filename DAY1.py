# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt


print("Hello World")
#1 SUM
a=5
b=8
print(a+b)
sum=a+b
print(sum)
a=int((input("Enter first number: \n")))
b=int((input("Enter second number: \n")))
sum=a+b
print("Sum of a and b is", sum)

#2 Max and Min
a=int((input("Enter first number: \n")))
b=int((input("Enter second number: \n")))
c=int((input("Enter third number: \n")))
if a>b and a>c:
    print("a is max of 3 numbers")
elif b>a and b>c:
    print("b is max of 3 numbers")
elif c>a and c>b:
    print("c is max of 3 numbers")
else:
    print("Either of 3 number are equal")
    
if a<b and a<c:
    print("a is min of 3 numbers")
elif b<a and b<c:
    print("b is min of 3 numbers")
elif c<a and c<b:
    print("c is min of 3 numbers")
else:
    print("Either of 3 number are equal")

#3 Factorial
n=int(input("Enter the number you want to find out factorial for: ")) 
factorial = 1
for i in range(1, n+1):
    factorial = factorial*i
    fact = factorial
print("Factorial of the number is ", fact)    

#4 Triangle
a=int((input("Enter first side: \n")))
b=int((input("Enter second side: \n")))
c=int((input("Enter third side: \n")))
if (a+b>=c or a+c>=b or b+c>=a):
    print("It is sides of triangle")
else:
    print("it is not a triangle")
    

if (a==b==c):
    print("Equilateral Triangle")
elif (a==b or b==c or c==a):
    print("Isosceles Triangle")
elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2 ):
    print("Right Triangle")
else:
    print("Scalene Triangle")
s = (a+b+c)/2
area = ((s)*(s-a)*(s-b)*(s-c))**0.5
print(f"Area of triangle is {area}" )    

#AD1 Prime interval
lower = int(input("Enter lower bound of number: "))
upper = int(input("Enter upper bound of number: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
                
#AD2 Prime
n=int(input("Enter a number: "))
if n<=0:
    print("Incorrect Input")
elif n%2==0:
    print("Not Prime")
else:
    print("Prime")
    
#AD3 Fibonacci
def Fibonacci_Series(n):    
    if n < 0:  
        print("Incorrect input")  
    # First Fibonacci number is 0  
    elif n == 0:   
        return (0)   
    # Second Fibonacci number is 1   
    elif n == 1:  
        return (1)  
    else:  
        return (Fibonacci_Series(n - 1) + Fibonacci_Series(n - 2))   
n=int(input("Enter the nth number you want to find: "))
print("nth Element of the Fibonacci Series:", Fibonacci_Series(n))

#AD4 Detect Fibonacci Sequence
n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes it is Fibonacci")
    else:
        print("Not Fibonacci")

#AD5 Sum of square
def squaresum(n):
    sum=0
    for i in range(1, n+1):
        sum += i*i
        # sum = sum + i*i
    return sum
n=int(input("Enter a number: "))
print(squaresum(n))

