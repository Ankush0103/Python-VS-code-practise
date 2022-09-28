try:
    a = int(input("Enter a number: \n"))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please enter a valid value\n")
    print(e) # python gives value of e it does not show any error.

except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero\n")
    print(e) # python gives value of e it does not show any error.

print("Thanks for using this code!")