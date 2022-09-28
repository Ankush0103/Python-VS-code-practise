for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Loop terminated successfully")
    # Due to break else statement will not printed be ause loop is not succesfully terminated.