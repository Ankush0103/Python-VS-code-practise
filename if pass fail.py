sub1 = int(input("Enter number1: \n"))
sub2 = int(input("Enter number2: \n"))
sub3 = int(input("Enter number3: \n"))

if(sub1< 33 or  sub2< 33 or sub3< 33):
    print("You are Fail due to less than 33% in any one of the subject\n")

elif(sub1 + sub2 + sub3)/3 < 40:
    print("You are fail due to less than 40%\n")

else:
    print("You passed this exam\n")