# Day 4 Array and Matrix

# 1. Write a python program to find sum of all elements in an array.
arr = [1, 2, 3, 4, 5]
print("Sum of array element is ", sum(arr))

# 2. Write a python program to copy all elements of one array into another array.
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [None] * len(arr1)
'''arr2 = arr1.copy()
print(arr2)'''
for i in range(0, len(arr1)):
   arr2[i] = arr1[i]
print("The original array is : ")
for i in range(0, len(arr1)):
    print(arr1[i])
print("The new array is : ")
for i in range(0, len(arr2)):
   print(arr2[i])

# 3. Write a python program to sort the elements of an array in ascending order.
arr = [37, 45, 96, 87, 2]
print("original array: ", arr)
arr.sort()
print("Sorted array ", arr)

# 4 . Write a python program to create a matrix of order n × n.
n = int(input("Enter dimension(n) of matrix: "))
matrix = [list(range(1 + n*i, 1 + n*(i+1))) for i in range(n)]
print("Resultant matrix is: ")
for m in matrix:
    print(m)

# 5. Write a python program to add two matrices
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[10,11,12],
    [13,14,15],
    [16,17,18]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)

# 6. Write a python program to multiply two matrices

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]


# result is 3x3
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

# ADP 1. Write a python program to find the largest and smallest element in an array.
arr = [14, 18, 2, 36]
print("Maximum element of array: ", max(arr))
print("Minimum element of array: ", min(arr))

# ADP 2. Write a python program to print the elements of an array in reverse order.
arr = [45, 12, 78, 3]
print("Original array: ", arr)
arr.reverse()
print("Reversed array: ", arr)

# ADP 3. Write a python program to Split the array and add the first part to the end
def SplitArray(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x		
arr = [15, 40, 15, 16, 50, 36]
print("Original Array: ", arr)
n = len(arr)
position = 1
SplitArray(arr, n, position)
print("new array: ")
for i in range(0, n):
	print(arr[i], end = ' ')

# ADP 4. Write a python program to check if the given array is Monotonic.
# Monotonic menas either increasing or decreasing
def ismonotone(a):
    n=len(a) #size of array
    if n==1:
        return True
    else:
        #check for monotone behaviour
        if (all(a[i]>=a[i+1] for i in range(0,n-1)) or all(a[i]<=a[i+1] for i in range(0,n-1))):
            return True
        else:
            return False

A = [1, 2, 3, 4]
print("A is monotonic: ", ismonotone(A))
b = [4, 3, 2, 1]
print("B is monotonic: ", ismonotone(b))
c=[4,2,3, 5]
print("C is monotonic: ", ismonotone(c))
d=[1]
print("D is monotonic: ",ismonotone(d))

# ADP 5. Write a python program to get the kth column of the matrix.
matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]
k = int(input("K canc be 0, 1 or 2 ?: "))

ele = [i[k] for i in matrix]
print("Column elements are: ", ele)

# ADP 6. Write a python program to transpose a matrix.
X = [[1,2],
    [3 ,4],
    [5 ,6]]
print("Original matrix: ")
for e in X:
    print(e)
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
print("Transpose Matrix: ")
for r in result:
   print(r)


