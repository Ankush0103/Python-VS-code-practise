class Person:
    country = "India"
    
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I aa An Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

p = Person()
p.takeBreath() # I am breathing..
print(p.country) # India but print(p.company) will throw an error.
e = Employee()
e.takeBreath() # I am an Employee so I am luckily breathing..
print(e.company) # Honda
pr = Programmer()
pr.takeBreath() # I am an Employee so I am luckily breathing..  It takes from employee so it return sam eas above program.
print(pr.company) # Fiverr
print(pr.country) # It is derived from employee which is derived from person so returns India.