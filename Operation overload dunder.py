class Number:
    def __init__(self, num): # it is known as dunder method since __init.
        self.num = num
    
    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __sub__(self, num2):
        print("Lets substract")
        return self.num - num2.num
    
    def __truediv__(self, num2):
        print("Lets divide")
        return self.num / num2.num

    def __truediv__(self, num2):
        print("Lets divide")
        return self.num / num2.num

    def __floordiv__(self, num2):
        print("Lets floordivide")
        return self.num // num2.num   

n1 = Number(8)
n2 = Number(6)

sum = n1 + n2
print(sum)

mul = n1 * n2
print(mul)

sub = n1 - n2
print(sub)

div = n1 / n2
print(div)

floordiv = n1//n2
print(floordiv)

