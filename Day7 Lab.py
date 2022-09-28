# Class and Objects
''' 1. Write a Rectangle class in Python language, allowing you to build a rectangle with length
and width attributes.
i. Create a Perimeter() method to calculate the perimeter of the rectangle and anArea()
method to calculate the area of the rectangle.
ii. Create a method display() that displays the length, width, perimeter, and area of an
object created using an instantiation on rectangle class.
iii. Create a Parallelepiped child class inheriting from the Rectangle class and with a
height attribute and another Volume() method to calculate the volume of the
Parallelepiped.'''

# __init__ = It is initializer and is invoked at time of construction of object.
# Class is blueprint of creating objects
# Object is instance of class created.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width =  width
    # i
    def Perimeter(self):
        return 2*(self.length + self.width)
    def Area(self):
        return (self.length*self.width)
    # ii
    def display(self):
        print("Length of rectangle is: ", self.length)
        print("Breadth of rectangle is: ", self.width)
        print("Perimieter of rectangle is: ", self.Perimeter())
        print("Area of rectangle is: ", self.Area())
        
#iii
class Parallelopiped(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height
        
    def volume(self):
        return self.length*self.width*self.height

print("Questions i. and ii.")
myRectangle = Rectangle(8, 6)
myRectangle.display()
print("Heading towards iii.")
myParallelopiped = Parallelopiped(8, 6, 4)
print("Volume of given Parallelepiped is: ", myParallelopiped.volume())


''' 2. Create a Python class called BankAccount which represents a bank account, having as
attributes: accountNumber (numeric type), name (name of the account owner as string
type), and balance.
i. Create a constructor with parameters: accountNumber, name, balance.
ii. Create a Deposit() method which manages the deposit actions.
iii. Create a Withdrawal() methodwhich manages withdrawal actions.
iv. Create a bankFees() method to apply the bank fees with a percentage of 5% of the
balance account.
v. Create a display() method to display account details.'''

class BankAccount:
    # i.
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    # ii.
    def Deposit(self, d):
        self.balance = self.balance + d
    # iii.
    def Withdrawl(self, w):
        self.balance = self.balance - w
    # iv.
    def bankFees(self):
        self.balance = (95/100)*self.balance
    # v.
    def display(self):
        print("Account Number: ", self.accountNumber)
        print("Account Name: ", self.name)
        print("Account Balance: ", self.balance, 'Rupees')

newAccount = BankAccount(217854, "Ankur", 2500)
print("Initial account details: ")
newAccount.display()
newAccount.Deposit(500)
print("Account details after depositing: ") 
newAccount.display()
newAccount.Withdrawl(300)
print("Account details after withdrawl: ")
newAccount.display()



''' ADP1. Write a Python program to create a Vehicle class with name, max_speed and mileage
instance attributes.
i. Create a child class Bus that will inherit all of the variables and methods of the
Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of
50.
ii. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus
instance, we need to add an extra 10% on full fare as a maintenance charge. So the
total fare for the bus instance will become the final amount = total fare + 10% of the
total fare.
iii. Determine which class a given Bus object belongs to.
iv. Determine if School_bus, an object of Bus class, is also an instance of the Vehicle
class.'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
# i.
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        Vehicle.__init__(self, name, max_speed, mileage)
        self.seating_capacity = 50
        

    
    
    
    
    
    
    
    

    
    
    
    
    
    
'''ADP 2. Write a Program to create a class by name Staff, and initialize attributes like role, dept, and salary while creating an object.
i.	Create a child class Teacher that will inherit the properties of Parent class Staff and initialize with attributes name and age.
ii.	Create an object of the class Teacher and using the class instance print all the writable attributes of that object.
iii.	overloads the operator + to add salary of Teachers.'''

class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
# i
class Teacher(Staff):
    def __init__(self, role, dept, salary, name, age):
        Staff.__init__(self, role, dept, salary)
        self.name = name
        self.age = age
    
    def display(self):
        print("Name of teacher: ", self.name)
        print("Age of teacher: ", self.age)
        print("Salary of teacher: ", self.salary)
        print("Dept of teacher: ", self.dept)
        print("Role of teacher: ", self.role)
     
    def udSalary(self, sal):
        self.salary  = self.salary + sal
      

# ii        
myTeacher = Teacher('Teaching', 'CSBS', 50000, 'ABC', 40)
myTeacher.display()
# iii
myTeacher.udSalary(5000)
print("Printing information of teacher after salary upgradation")
myTeacher.display()#Salary would be upgraded to 55000
        

        