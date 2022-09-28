class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("******")
        print(f"The name of train is {self.name}")
        print(f"The seats availabe in train are {self.seats}")
        print("******")

    def fareInfo(self):
        print(f"The price of ticket is: Rs. {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full. Kindly try in Tatkal")


intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()