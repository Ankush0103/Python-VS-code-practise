# Snake Water Gun project via python
def gameWin(player1, player2):
    # If two values are equal declare the tie
    if player1 == player2: 
        return None

    # Checking for possibilities if player1 choses s
    elif player1 == 's':
        if player2 == 'w':
            return False
        elif player2 == 'g':
            return True

    # Checking for possibilities if player1uter choses w
    elif player1 == 'w':
        if player2 == 'g':
            return False
        elif player2 == 's':
            return True

    # Checking for possibilities if player1uter choses w       
    elif player1 == 'g':
        if player2 == 's':
            return False
        elif player2 == 'w':
            return True        


player1 = input("player1 Turn: Snake(s) Water(w) or Gun(g)?")
player2 = input("player2 Turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(player1, player2)

print(f"player1 chose {player1}")
print(f"player2 chose {player2}")

if a == None:
    print("The game is a tie!")
elif a:
    print("player2 Win!")
else:
    print("player1 Win!")
