# Creating a tuple using ()
t = (1, 2, 4, 5)

# t1 = () # Empty Tuple
# t1 = (1) # Wrong way to declare a Tuple with single element.
t1 = (1,) #Tuple with single elemnt
print(t1)
print(t) # Printing the tuple.
# Printing the element of a tuple.
print(t[0])

# Cannot update the values of a tuple.
t[0] = 11
print(t[0])
# A tuple is an immutable data type in python i.e. we cannot change its element just like in list.