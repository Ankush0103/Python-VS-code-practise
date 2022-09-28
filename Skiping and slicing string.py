# name = "Harry"
# d = name[1:4:1]
# print(d) # Output is arr i.e. no character skipped since 3rd argument of slicing value is 1.

Name = "Ankush"
a = Name[1:4:2]
print(a) # Output is nu because it skips k and prints each second character between index [1,4)

name = "Harryisgood"
b = name[0::2]
print(b) # Output is Hrysod because it prints every second value starting from index zero to the end. b = name[0:10:2] similar

naam = "Ankushisgood"
# c = naam[0::3]
c = naam[0:11:3]
print(c) #output is Auio because it prints every third value starting from index zero to the end. c = naam[0:11:3] similar