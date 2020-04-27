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

    def stock(self, symbol, number_shares):
        self.symbol = symbol
        self.number_shares = number_shares
        return self.symbol

    def count_shares(self, cost):
        self.cost = cost
        number = cost /  self.price_per_share
        self.balance -= cost
        return self.balance
