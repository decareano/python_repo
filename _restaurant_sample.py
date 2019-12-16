class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
	
    def describe_restaurant(self):
        print("this restaurant name is " + self.restaurant_name + " and it serves " +
              self.cuisine_type + " food")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open for business ")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="ice_cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []
        

    def display_flavors(self):
        print("we have the following flavors: ")
        for flavor in self.flavors:
            print("-" + flavor.title())

heladeria = IceCreamStand("La heladeria de marcelo")
heladeria.flavors = ["strawberry", "vanilla", "frambuesa", "chocolate"]
heladeria.display_flavors()
heladeria.describe_restaurant()


restaurant = Restaurant(" maria maria", "mexican")


print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
print(restaurant.restaurant_name)
restau1 = Restaurant("mefisto", "oriental")
print(restau1.describe_restaurant())

class User:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = None
        self.email = None
        self.user_id = None

    def describe_user(self):
        print("this user's first name is " + self.first_name + " and his last name is " +
              self.last_name + " and he lives at " + self.address)

a_new_user = User("marcelo", "gobelli", "123 Main St")
print(a_new_user.describe_user())

        
