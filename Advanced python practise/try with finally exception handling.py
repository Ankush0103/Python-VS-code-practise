try:
    i = int(input("Enter a number: "))
    c = 1/i
    
except Exception as e:
    print(e)
    exit()

finally: # it will be execute irrespective the program is going to exit or not.
    print("We are done")