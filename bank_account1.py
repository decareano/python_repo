class BankAccount:
     def __init__(self):
        self.balance = 0
        self.price_per_share = 15

     def __call__(self):
        pass

     def stock(self, name, price, num_shares, availability=1):
        self.name = name
        self.price = price
        self.num_shares = num_shares
        self.availability = availability

print(callable(BankAccount))

class User:
    def __init__(self, name, bank_account, budget=10000):
        self.name = name
        self.bank_account = bank_account
        self.budget = budget
        self.stocks = []
        #self.bank_account = bank_account

    def buy_stock(self):
        self.bank_account.stock("ibm", 50, 100)
        print(self.bank_account.name)
        #BankAccount.stock(self, "hd", 50, 100, availability=1) \
        print(f"Marcelo has bot {self.bank_account.num_shares} \
        shares of {self.bank_account.name} stock for \
        {self.bank_account.price} dollars a share")


s1 = BankAccount()  #shorthand for: object.__call__()
u1 = User("Marcelo", bank_account=s1, budget=10000)
print(callable(s1))
#s1()
print(u1.name)
u1.buy_stock()

