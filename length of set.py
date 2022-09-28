s = set()
print(type(s))
s.add(20)
s.add(20.0)
s.add("20")
print(s) # Returns {20, '20'}
print(len(s)) # Retuns length = 2, float and int same. 
