import random

class Bicycle():
    """the bike class"""
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = float(weight)
        self.cost = round(float(cost), 2)

class BikeShop():
    """the shop class"""
    def __init__(self, name):
        self.name = name
        self.inventory = ()
        self.profit = 0

    def sell_bike(self, inventory_index, retail_margin):
        del self.inventory_index[inventory_index]
        self.profit += retail_margin * self.profit

    def return_profit(self):
        return self.profit

class Customer():
    """ customer is sacred  """
    def __init__(self, name, cash):
        self.name = name
        self.cash = round(float(cash), 2)
        self.bikes = []

def print_customer_list(customers, shop):
    inventory ={}
    for bike in shop.inventory:
        inventory[bike.model] = bike.cost
        print("list inventory: ", inventory)
        print("customers and bikes at %s. " % (shop.name))

        for names in customers:
            for x, y in inventory.items():
                if y <= names.cash: print("%s can affors a %s for %i." % (names.name, x, y))

def print_shop_inventory(shop):
    inventory = {}
    for bike in shop.inventory:
        inventory[bike.model] = bike.cost
        print("inventory for shop %s: "  % (shop.name))
        for model, cost in inventory.items():
            print("Bike model %s at initial cost of $%i." % (model, cost))


def main():
    bikeshop1 = BikeShop('I bike your pardon')
    bikeshop1.profit = 1.5
    bike_brands = ['Trek', 'Salsa', 'Jamis', 'Specialized', 'Surly', 'Giant', 'Bianchi',
	'Cannondale', 'Soma', 'Cervelo']
    bikes = []
    for x in range(7):
        bikebrand = random.choice(bike_brands)
        bikeweight =random.randint(19, 23)
        bikecost = random.randint(100, 1200)
        bikes.append(Bicycle(bikebrand, bikeweight, bikecost))

    bikeshop1.inventory = [x for x in bikes]

    Mike = Customer('Mike', 200)
    Joe = Customer('Joe', 500)
    Sam = Customer('Sam', 1000)
    customers = [Mike, Joe, Sam]

    print_customer_list(customers, bikeshop1)
    print_shop_inventory(bikeshop1)

main()
