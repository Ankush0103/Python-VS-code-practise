def game():
    return 44
    
score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

# If our game function returns more than highscore it overwrites the text file else it will remain intact.
