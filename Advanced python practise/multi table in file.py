num = int(input("Enter your number: "))

table = [num*i for i in range(1, 11)]
print(f"The table of {num} is {str(table)}")
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")