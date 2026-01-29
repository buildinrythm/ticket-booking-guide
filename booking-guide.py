from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, custName, price, quantity):
        self.custName = custName
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def printSummary(self):
        pass

    @abstractmethod
    def calcTotal(self):
        pass


class Sale(Transaction):
    def __init__(self, custName, price, quantity, eventName):
        super().__init__(custName, price, quantity)

        self.eventName = eventName

    def calcTotal(self):
        total = (self.price * self.quantity) * 1.005
        return total

    def printSummary(self):
        total = self.calcTotal()
        print("\n=== Sale Summary ===")
        print(f"Customer name: {self.custName}")
        print(f"Event name:  {self.eventName}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print(f"Total: {self.total:.2f}")
        print("============================\n")
    

class Return(Transaction):
    def __init__(self, custName, price, quantity, returnDate):
        super().__init__(custName, price, quantity)

        self.returnDate = returnDate

    def calcTotal(self):
        total = (self.price * self.quantity)
        return total

    def printSummary(self):
        total = self.calcTotal()
        print("\n=== Return Summary ===")
        print(f"Customer name: {self.custName}")
        print(f"Event name:  {self.eventName}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print(f"Return date: {self.returnDate}")
        print(f"Total: {self.total:.2f}")
        print("============================\n")


def main():
    
    


if __name__ == "__main__":
    main()