def power(n, p):
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return(n*power(n, p-1))

# source Code
n = int(input("Enter a number: \n"))
p = int(input("Enter the power: \n"))

print(power(n,p))