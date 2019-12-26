class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
	
    def describe_restaurant(self):
        print("this restaurant name is " + self.restaurant_name + " and it serves " +
              self.cuisine_type + " food")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open for business ")

    def set_number_served(self, number_served):
        """customers served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant(" maria maria", "mexican")

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("\nNumber served: " + str(restaurant.number_served))

restaurant.increment_number_served(55)
print("new number served: " + str(restaurant.number_served))


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


#restaurant = Restaurant(" maria maria", "mexican")




print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
print(restaurant.restaurant_name)
restau1 = Restaurant("mefisto", "oriental")
print(restau1.describe_restaurant())

class User:
    def __init__(self, first_name, last_name, address, username, email, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.user_id = user_id
        self.login_attempts = 0

    def describe_user(self):
        print("this user's first name is " + self.first_name + " and his last name is " +
              self.last_name + " and he lives at " + self.address)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        "reset logins to zero"
        self.login_attempts = 0

    
a_new_user = User("marcelo", "gobelli", "123 Main St", "pinga", "mg@someisp.net", "reydelcompas")
print(a_new_user.describe_user())
a_new_user.increment_login_attempts()
a_new_user.increment_login_attempts()
a_new_user.increment_login_attempts()
print("Login attempts: " + str(a_new_user.login_attempts))
print("resetting login attempts...")
a_new_user.reset_login_attempts()
print("Resetting. Now we have: " + str(a_new_user.login_attempts))


class Admin(User):
    def __init__(self, first_name, last_name, address, username, email, user_id):
        """initialize the admin"""
        super().__init__(first_name, last_name, address, username, email, user_id)
        self.privileges = []

    def show_privileges(self):
        """display the admin's privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

eric = Admin("marcelo", "gobelli", "321 atalaya st", "test", "e_matthes@example.com", "pindonga")
eric.describe_user()

eric.privileges = [
    'can reset pwds',
    'can moderate discussions',
    'can suspend accounts',
    ]
        
eric.show_privileges()
