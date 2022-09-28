class Employee:
    company = "Google" # Specific to each class
    salary = 100000

harry = Employee() # Object Instantiation
rajni = Employee() # Object Instantiation

# Creating instance attributes for both objects
# harry.salary = 300000
# rajni.salary = 150000
# We have commented out instance attribute so only class attribute of 100000 in both case will be shown

print(harry.company)
print(rajni.company)
Employee.company = "YouTube" # changing class atrtribute
print(harry.company) # Company changes to YouTube
print(rajni.company)
harry.salary = 450000 # Harry instance attributew is present so that salary will be printed but in case of rajni claas attribute salary of 100000 will be printed.
print(harry.salary)
print(rajni.salary)

# print(rajni.address) throws an error because address is not present in instance/class attributes