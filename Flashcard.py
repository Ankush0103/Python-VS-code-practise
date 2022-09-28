# Create flashcard having word and its meaning

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        # We returned a string
        return self.word + ' ( '+self.meaning+' ) '

flash = []
print("Welcome to flashboard application")

while(True):
    word = input("Enter name you want to add to flashcard: \n")
    meaning = input("Enter meaning of word: \n")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard: \n"))

    if(option):
        break

print("Your flashcards\n")
for i in flash:
    print(">", i)