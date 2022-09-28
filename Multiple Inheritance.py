class Employee:
    company = "Visa"
    eCode = 120
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
e = Employee()
p.upgradeLevel()
print(p.level)
print(e.company)
print(e.eCode)
print(p.company) # Employee Company will be printed because its class is wriiten first in class Programmer(Employee, Freelancer)
print(p.name)