l = [1, 2, 3, 4, 5, 10, 12, 13, 17, 180, 25, 66, 77]

a = filter(lambda a: a%5==0, l)
print(list(a))