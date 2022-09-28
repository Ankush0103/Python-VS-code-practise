num = int(input("Enter the number: \n"))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial*i
print(f"The factorial of given number is {factorial}")