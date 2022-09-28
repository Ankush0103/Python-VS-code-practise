# Guessing number Project
import random
randNumber =random.randint(1, 100)
# print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
           print("You guessed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enter a larger number.")
    guesses += 1

print(f"You guessed the number in {guesses} guesses")