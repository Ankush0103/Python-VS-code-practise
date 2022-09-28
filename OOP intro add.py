class Number:  # a and b are variable which are associated with number
    def sum(self):
        return self.a + self.b

num = Number() # Object Instantiation
num.a = 12   # Memory is allocated only after object Instantiation.
num.b = 34
s = num.sum()
print(s)

# a = 12
# b = 34
# print("The sum of and b is ", a+b)
'''
PascalCase
EmployeeName -->PascalCase

camelCase
isNumeric, isFloatorInt -->camelCase
'''