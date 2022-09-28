a = {}
print(type(a)) # This creates an empty dictionary and not an empty set.

# An empty set can be create dusing below syntax.
b = set()
print(type(b))
b.add(4)
b.add(5)

print(b) # return {4, 5} since 4 and 5 is added.
b.add((4, 5 ,6)) 
print(b) # Tuples is add in output but we cannot add list [] and dictionar{} because it is not hasheable.
print(len(b))
b.remove(5) # removes the given number from set.
print(b)

print(b.pop()) # Randomly picks an arbitrary element and removes it.
print(b)