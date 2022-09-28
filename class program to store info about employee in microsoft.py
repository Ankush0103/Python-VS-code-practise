class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of {self.company} programmer is {self.name} and product is \
             {self.product}")

Ankur = Programmer("Ankur", "Skype")
Ankush = Programmer("Ankush", "GitHub")    
Ankur.getInfo()
Ankush.getInfo()