def pypart(n):
    k = 2*n - 2 # Number of spaces
    for i in range(0,n): # n to handle number of rows
        # Inner Loop to handle number of  spaces
        # Values canging acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # Decreementing k after each loop
        k = k - 2

        for j in range(0, i+1): # i tohandle number of columns
            print("* ", end="")
        print("\n")

n = int(input("Eneter teh number of rows in pyramid: \n"))
pypart(n)