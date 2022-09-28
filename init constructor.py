class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit): # init runs automatically and is called constructor because object is initialised.
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")


    def getSalary(self,signature): # self is parameter that is passed when a object is call.
        print(f"Salary for this employee working in {self.company} is {self.Salary}\n{signature}")
    
    @staticmethod # decorator to mark grret as a static method
    def greet(): # Under static method no need to write self as it will show positional argument self is missing.
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("Time is 9am in the morning")

harry = Employee("Harry", 100, "YouTube")
# harry = Employee() throws an error (missing 3 psitional arguments)
harry.getDetails()