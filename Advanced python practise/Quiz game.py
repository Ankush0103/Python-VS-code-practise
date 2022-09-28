# Quiz Game
print("Welcome to quiz game")
score = 0
total_questions = 5
question = input("What does FOSS stands for?: \n")
if question.lower()=='free open source software':
    score += 1
    print('Correct')
else:
    print('Wrong answer')

question = input("Which tech company has the latest data leak?: \n")
if question.lower()=='facebook':
    score += 1
    print('Correct')
else:
    print('Wrong answer')

question = input("What invented C?: \n")
if question.lower()=='dennis ritchie':
    score += 1
    print('Correct')
else:
    print('Wrong answer')

question = input("What technology is used to record cryptocurrency transactions?: \n")
if question.lower()=='blockchain':
    score += 1
    print('Correct')
else:
    print('Wrong answer')

question = input("Which of the following is an important step towards the paperless concept?: \n")
if question.lower()=='digitizing':
    score += 1
    print('Correct')
else:
    print('Wrong answer')

print("Thanks for playing!, you attempted", score, "questions correctly")
marks=(score/total_questions)*100
print("Marks obtained: ", marks)
print("THANK YOU! WILL SEE YOU AGAIN")