class Employee:
    company = "Google"

    def getSalary(self,signature): # self is parameter that is passed when a object is call.
        print(f"Salary for this employee working in {self.company} is {self.Salary}\n{signature}")
    
    @staticmethod # decorator to mark grret as a static method
    def greet(): # Under static method no need to write self as it will show positional argument self is missing.
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("Time is 9am in the morning")

harry = Employee()
harry.Salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
harry.greet() # Empoloyee.greet()
harry.time()