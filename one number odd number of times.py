from functools import reduce
def oddTimes(input):
    print(reduce(lambda a, b: a^b, input))

# Driver Program
if __name__ == "__main__":
    input = [1, 2, 3, 2, 3, 1, 3]
    oddTimes(input) # 3 has occured 3 i.e odd number of times so it will return 3