# Day2 Lists and tuples
#1 List swap
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))

#2 element exist or not
list = [1, 2, 3, 'Ankur', 5]
n = int(input("Enter the number you want to check: "))
s = input("Enter the string you want to check: ")
if(n in list):
    print(f"{n} exists")
else:
    print(f"{n} does not exist")
if(s in list):
    print(f"{s} exists")
else:
    print(f"{s} does not exist")

#3 Greatest element in list
list = []
n = int(input("Enter number of elements in list: "))
print("Elements in list are: ")
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print(list)

print("Maximum number in list is: ", max(list))
print("Minimum number in list is: ", min(list))

#Tuples
t = (1, 2, 4, 5)

t1 = (1,) #Tuple with single elemnt
print(t1)
print(t) # Printing the tuple.
# Printing the element of a tuple.
print(t[0])

#4 Size of tuple
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple 1: ",  Tuple1.__sizeof__(), "bytes")
print("Size of Tuple 2: ",  Tuple2.__sizeof__(), "bytes")
print("Size of Tuple 3: ",  Tuple3.__sizeof__(), "bytes")

#5 max and min of tuple
tup = (5, 20, 3, 7, 6, 8)
# printing original tuple
print(tup)

# initializing K
# K = 2
K = int(input("Enter size of K: "))
testtup = list(tup)
temp = sorted(testtup)
restup = tuple(temp[:K] + temp[-K:])

print(restup)

#6 Combination of tuple
tup1 = (1,2)
tup2 = (3,4)
print(tup1)
print(tup2)

restup =  [(a, b) for a in tup1 for b in tup2]
restup = restup +  [(a, b) for a in tup2 for b in tup1]
  
print(restup)

#ADP 1 clear list in python
list = [1, 2, 3, 4]
print(list)
print(list.clear())

#ADP2 to find n largest elementin list
l = []
n = int(input("enter size of list: "))
print("elements in list are: ")
for i in range(0, n):
    ele = int(input())
    l.append(ele)
print(l)
m = int(input("Enter the m largest element: "))
l.sort()
print(l[-m:])

#ADP3 Empty List
l = [1, 45, 2, [], 65, []]
print(l)
#reslist = [a for a in l if a!=[]]
reslist = list(filter(None, l))
print(reslist)

#ADP4 Add tuple to list
list = [1, 2, 3]
tuple = (3, 9, 7)
list += tuple
print(list)

#ADP5 Removing tuples of length from list
l =  [(12, 13, 14), (14, 15), (16, 17), (18, 19)]
#  original list
print(l)
# initializing K
K = int(input("enter size of tuple to be removed: "))
reslist = [a for a in l if len(a) != K]
print(reslist)

#ADP 6
l = [1, 2, 5, 6] 
#reslist = [(val, val**3) for val in l]
reslist = [(val, pow(val, 3))for val in l]
 
# print the result
print(reslist)



