class Sample:
    a = "Harry" # Class Attribute

obj = Sample()
obj.a = "Ankur" # Instance Attribute

print(Sample.a) # Harry. It does not change class attribute to change it we use--> Sample.a = "Ankur"
print(obj.a)    # Ankur