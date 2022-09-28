class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person..\n")
    
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Emoloyee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I aa An Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__() # If this command is commented out then pr.Programmer() will show only Initialising Programmer.. because we did not instructed superclass constructor to be called. 
        print("Initializing Programmer..\n")

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        super().takeBreath() # Calls constructor of base class
        print("I am programmer so I am breathing++..")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath() # prints super class and then its own string.

pr = Programmer()
# pr.takeBreath() # prints super class string and then its superclass's superclass and the its own string

