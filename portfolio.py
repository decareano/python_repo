class Portfolio:

	def __init__(self, owner):
        self.owner = owner
        self.cash = 0
        self.stocks = {}   # a mapping of Stock --> quantity

	def stock(self, name, price, num_shares, availability=1):
        self.name = name
        self.price = price
        self.num_shares = num_shares
        self.availability = availability

    def buy_stock(self):
        self.bank_account.stock("ibm", 50, 100)
        #print(self.bank_account.name)
        #BankAccount.stock(self, "hd", 50, 100, availability=1) \
        print(f"Marcelo has bot {self.bank_account.num_shares} \
        shares of {self.bank_account.name} stock for \
        {self.bank_account.price} dollars a share")

    def sell(self, stock, quantity):
        assert quantity > 0
        try:
            if self.stocks[stock] < quantity:
                print('Not enough', stock.ticker, 'inventory to sell', str(quantity), stock)
                return
            self.stocks[stock] -= quantity * stock.price
            self.cash += quantity * stock.price
        except KeyError:
            print('No', stock.ticker, 'inventory to sell')


p1 = Portfolio()  #shorthand for: object.__call__()
u1 = User("Marcelo", portfolio_account=p1, budget=10000)
print(callable(p1))
#s1()
print(u1.name)
u1.buy_stock()