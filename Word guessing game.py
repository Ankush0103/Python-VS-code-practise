import random

name = input("Guess the word: \n") # It gives the name of yours Good Luck 

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'maths', 'water', 'board']
word = random.choice(words)
print("Guess the characters: \n") # Actual question is about character
guesses = ''
# any number of turns can be used here
turns = 12
while turns>0:
    fails = 0 # Count the number of times user fails

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

            fails += 1

    if fails == 0:
        print("You win")

        print("The word is: \n", word)
        break
    guess = input("Guess a character: \n")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong\n")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You loose\n")