while(True):
    print("Press q to quit")
    a = input(("Enter a number: \n"))
    if a == 'q':
        break;
    try:
        print("Trying..\n")
        a = int(a)
        if a>6:
            print("You enterad a number greater than 6\n")
        else:
            print("Number not greater than 6\n")
    except Exception as e:
        print(f"Your input resulted in error: {e}")
print("Thanks for playing this game")