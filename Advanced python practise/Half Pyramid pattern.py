def pypart(n):
    # Number of rows handled by n.
    for i in range(0, n):
        # Inner loop to handle number of columns
        for j in range (0, i+1):
            print("*", end="")

        print("\n") # Ending line after eaach row

n = int(input("enter the number of rows of pyramid: \n"))
pypart(n)