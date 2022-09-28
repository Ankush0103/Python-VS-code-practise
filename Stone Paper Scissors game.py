# Stone Paper Scissors project via python
import random # random module has function wich prints a random value

def gameWin(comp, you):
    # If two values are equal declare the tie
    if comp == you: 
        return None

    # Checking for possibilities if computer choses st
    elif comp == 'st':
        if you == 'sc':
            return False
        elif you == 'pa':
            return True

    # Checking for possibilities if computer choses pa
    elif comp == 'pa':
        if you == 'st':
            return False
        elif you == 'sc':
            return True

    # Checking for possibilities if computer choses sc       
    elif comp == 'sc':
        if you == 'pa':
            return False
        elif you == 'st':
            return True        

print("Comp Turn: Stone(st) Paper(pa) or Scissors(sc)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'st'
elif randNo == 2:
    comp = 'pa'
elif randNo == 3:
    comp = 'sc'

you = input("Your Turn: Stone(st) Paper(pa) or Scissors(sc)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You Win!")
else:
    print("You Lose!")