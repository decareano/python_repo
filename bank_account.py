class BankAccount:
    def __init__(self):
        self.balance = 0
        self.price_per_share = 15

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def stock(self, symbol, cost):
        self.symbol = symbol
        self.cost = cost
        return self.symbol

    def count_shares(self):
        number = 10000 / self.price_per_share
        return number
