# Stone Paper Scissors project via python
def gameWin(player1, player2):
    # If two values are equal declare the tie
    if player1 == player2: 
        return None

    # Checking for possibilities if player1 choses stone(st)
    elif player1 == 'st':
        if player2 == 'sc':
            return False
        elif player2 == 'pa':
            return True

    # Checking for possibilities if player1 choses paper(pa)
    elif player1 == 'pa':
        if player2 == 'st':
            return False
        elif player2 == 'sc':
            return True

    # Checking for possibilities if player1 choses scissors(sc)       
    elif player1 == 'sc':
        if player2 == 'pa':
            return False
        elif player2 == 'st':
            return True        

player1 = input("player1 Turn: Stone(st) Paper(pa) or Scissors(sc)?")
player2 = input("player2 Turn: Stone(st) Paper(pa) or Scissors(sc)?")

a = gameWin(player1, player2)

print(f"player1 chose {player1}")
print(f"player2 chose {player2}")

if a == None:
    print("The game is a tie!")
elif a == True:
    print("player2 Win!")
else:
    print("player1 Win!")