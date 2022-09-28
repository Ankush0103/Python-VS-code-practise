n = int(input("Enter the number of rows: \n"))
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')

# i is going to be enabled to
# range between n-i t 0 with a
# decrement of 1 with each iteration.
# and in print function, for each iteration,
# ” ” is multiplied with n-i and ‘*’ is
# multiplied with i to create correct
# space before of the stars.