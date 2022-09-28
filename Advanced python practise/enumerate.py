list1 = [3, 53, 2, False, 6.2, "Harry"]
# index = 0
# for item in list1:
#     print(index, item)
#     index += 1 # In python we cannot write as index++

for index, item in enumerate(list1):
    print(index, item)