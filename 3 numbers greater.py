num1 = int(input("Enter number1: \n"))
num2 = int(input("Enter number2: \n"))
num3 = int(input("Enter number3: \n"))


if(num1>num2):
    if(num1>num3):
        print("num1 is greatest")
    else:
        print("num3 is greatest")

elif(num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")