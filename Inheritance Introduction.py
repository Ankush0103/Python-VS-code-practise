# This is also an examle of single inheritance
class Employee:   # Base Class
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):  # Derived Class
    language = "Python"
    # company = "YouTube"
    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails() # It will not show Details of base class i.e. employee but it will show its own details of programmer. Hence in Inheritance we can overwrite Data.
print(p.company) # It finds company from base class of employee and prints Google.

