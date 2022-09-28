# Class method is bound to class and not object of the class
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
        # self.__class__.salary = sal # Creats an instance attribute without chanf=ging its class.
    
    @classmethod # Decorator is a fucntion which takes input and modifies it.
    def changeSalary(cls, sal):
        cls.salary = sal # Changes class attribute hence print(Employee.salary) returns 455

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)