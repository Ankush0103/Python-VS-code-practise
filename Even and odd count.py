# list1 = [10, 21, 4, 45, 66, 93, 11]
# even_count, odd_count = 0, 0
# num = 0

# while(num<len(list1)):
#     if list1[num] % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

#     # increementing num
#     num += 1

# print("Number of Even numbers in the list: \n", even_count)
# print("Number of Odd numbers in the list: \n", odd_count)

list1 = [10, 21, 4, 45, 66, 93, 11]
odd_count = len(list(filter(lambda x: (x%2 != 0), list1)))
even_count = len(list(filter(lambda x: (x%2 == 0), list1)))

print("Even numbers in the list: \n", even_count)
print("Odd numbers in the list: \n", odd_count)