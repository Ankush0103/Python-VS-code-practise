a = 54 # Global variable
def func1():
    global a
    print(f"Printing statement 1: {a}") # 54
    a = 8 # Local variable
    print(f"Printing statement 2: {a}") # 8

func1()
print(f"Printing statement 3: {a}") # 8