def farh(cel):
    return (cel *(9/5)) + 32

c = int(input("Enter celsius temperature: \n"))
f = farh(c)
print("Fahrenheit Temperatiure is " + str(f))