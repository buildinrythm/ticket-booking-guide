class Transaction:
    def __init__(self, custName, price, quantity):
        self.custName = name
        self.price = price
        self.quantity = quantity

    def printSummary():
        pass

    def calculateTotal():
        pass


class Sale(transaction):
    def __init__(self, custName, price, quantity, eventName):
        super().__init__(custName, price, quantity)

        self.eventName

    def calculateTotal():
        pass

    def printSummary():
        pass
    

class Return(Transaction):
    def __init__(self, custName, price, quantity, returnDate):
        super().__init__(custName, price, quantity)

        self.returnDate = returnDate

    def calculateTotal():
        pass

    def printSummary():
        pass


main():