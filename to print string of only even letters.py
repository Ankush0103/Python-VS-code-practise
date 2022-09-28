def printWords(s):
    # Split the string
    s = s.split(' ')

    # iterate in words of string
    for word in s:
        if len(word)%2 == 0:
            print(word)

# Driver code
s = "i am Ankush"
printWords(s)