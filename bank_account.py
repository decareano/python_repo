class BankAccount:
    def __init__(self):
        self.balance = 0
        self.price_per_share = 15
        self.investor_user = investor_user

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # def stock(self, symbol, number_shares):
    #     self.symbol = symbol
    #     self.number_shares = number_shares
    #     return self.symbol

    # def count_shares(self, cost):
    #     self.cost = cost
    #     number = cost /  self.price_per_share
    #     self.balance -= cost
    #     return self.balance


b1 = BankAccount()
u1 = User("Marcelo", investor_user=b1, budget=10000)
u1.deposit(5000)
print("user marcelo deposited 10000 dollars in his account")