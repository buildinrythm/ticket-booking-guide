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
        print(f"Total: {total:.2f}")
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
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print(f"Return date: {self.returnDate}")
        print(f"Total: {total:.2f}")
        print("============================\n")


def main():
    """Main program to handle transactions"""
    print("=== TRANSACTION SYSTEM ===\n")
    
    # Get transaction type and shared values
    transType = input("Enter transaction type (1 = Sale, 2 = Return): ")
    custName = input("Enter customer name: ")
    price = float(input("Enter ticket price: "))
    quantity = int(input("Enter quantity: "))


    # Process based on transaction type
    if transType == "1":
        eventName = input("Enter event name: ")
        trans = Sale(custName, price, quantity, eventName)
        trans.printSummary()
    elif transType == "2":
        returnDate = input("Enter return date (YYYY-MM-DD): ")
        trans = Return(custName, price, quantity, returnDate)
        trans.printSummary()
    else:
        print("Invalid transaction type")

# --- Unit Tests ---

# Test 1: Sale total calculation (with 0.5% tax)
saleTest = Sale("Alice", 10, 5, "Concert")  
assert abs(saleTest.calcTotal() - 50.25) < 1e-6, "Sale total calculation failed"

# Test 2: Sale summary prints (just check it runs)
saleTest.printSummary()  

# Test 3: Return total calculation (no tax)
returnTest = Return("Bob", 20, 3, "2026-01-29")  # 20*3 = 60
assert abs(returnTest.calcTotal() - 60) < 1e-6, "Return total calculation failed"

# Test 4: Return summary prints
returnTest.printSummary()  

print("All tests passed successfully!")



    


if __name__ == "__main__":
    main()