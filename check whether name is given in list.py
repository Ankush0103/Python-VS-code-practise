# Program to check whether name is given in the lists or not
names = ["Ankush", "Ankur", "Ankit", "Messi", "CR7"]
name = input("Enter name to check\n")

if name in names:
    print("Given name is in the list")
else:
    print("given name is not in the list")