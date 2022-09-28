'''Write a python program which will keep adding stream of numbers inputted by the user.
The adding stops as soon as user press the q key on keyboard.'''

sum = 0
sumMaterial = ' \0 '
while(True):
    userMaterial = input("Enter the material you want to buy: \n")
    if(userMaterial!='q'):
        sumMaterial = sumMaterial + str((userMaterial))
        print(f"You have buyed {userMaterial}")
    userInput = input("Enter the price\n")
    if(userInput!='q'):
        sum = sum + int(userInput)
        print(f"Your order total so far is {sum}\n")
    else:
        print(f"Your Bill of  {sumMaterial} is {sum}\n")
        print("Thanks for shopping with us.\n")
        break
