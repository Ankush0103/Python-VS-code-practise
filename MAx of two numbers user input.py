def maximum(a, b):
    if a> b:
        return a
    elif b> a:
        return b
    else:
        return None

a = int(input("Enter a number: \n"))
b = int(input("Enter b number: \n"))

print(f"Maximum of the a and b is {maximum(a, b)}")
