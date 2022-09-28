x = int(input("Enter the value of x: \n"))
square = lambda x: (x*x)
if(x>0):
    print(f"The square of x is {square(x)}\n")
else:
    None

a = int(input("Enter the value of a: \n"))
b = int(input("Enter the value of b: \n"))
max = lambda a, b: a if(a>b) else b

print(f"The max of a and b is {max(a, b)}\n")
