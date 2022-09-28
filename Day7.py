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

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    # i.
    def Perimeter(self):
        return 2*(self.length + self.breadth)
    
    def Area(self):
        return self.length*self.breadth

    # ii.
    def display(self):
        print("Length of rectangle is: ", self.length)
        print("Breadth of rectangle is: ", self.breadth)
        print("Perimieter of rectangle is: ", self.Perimeter())
        print("Perimieter of rectangle is: ", self.Area())
    
# iii.
class Parallelepiped(Rectangle):
    def __init__(self, length, breadth, height):
        Rectangle.__init__(self, length, breadth)
        self.height = height

    # Volume method
    def volume(self):
        return self.length*self.breadth*self.height
print("Questions i. and ii.")
myRectangle = Rectangle(8, 6)
myRectangle.display()
print("Heading towards iii.")
myParallelepiped = Parallelepiped(8, 6, 4)
print("Volume of given Parallelepiped is: ", myParallelepiped.volume())

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
        print("Account Nzme: ", self.name)
        print("Account Balance: ", self.balance, "$")

newAccount = BankAccount(217854, "Ankur", 2500)
print("Initial account details: ")
print( newAccount.display())
newAccount.Deposit(500)
print("Account details after depositing: ") 
print(newAccount.display())
newAccount.Withdrawl(300)
print("Account details after withdrawl: ")
print(newAccount.display())

''' 3. Write a Python program to create a Vehicle class with name, max_speed and mileage
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
    