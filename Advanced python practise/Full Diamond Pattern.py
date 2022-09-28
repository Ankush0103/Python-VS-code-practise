def Diamond(rows):
    n = 0
    for i in range(1, rows + 1):
        for j in range(1, (rows - i) + 1):
            print(end = " ")

        # Loop to print star
        while n != (2*i - 1):
            print("*", end = "")
            n = n + 1
        n = 0

        # line break
        print()
    k = 1
    n = 1
    for i in range(1, rows):
        # Loop to print spaces
        for j in range(1, k + 1):
            print(end = " ")
        k = k + 1
        # loop to print star
        while n<= (2 * (rows - i) - 1):
            print("*", end = "")
            n = n + 1
        n = 1
        print()

rows = int(input("enter the number of rows: \n"))
Diamond(rows) 