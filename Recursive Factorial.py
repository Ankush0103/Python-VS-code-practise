def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if i == 1 or n == 0:
        return 1 
    return n * factorial_recursive(n-1)

f = factorial_iter(5)
print(f)

# recursion is a function which call itself and is used directly as a mathematical formula.