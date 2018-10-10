class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")

my_dog = Dog('Willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "  + str(my_dog.age) + " years old")

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("the name of this restaurant is " + self.restaurant_name)

    def describe_cuisine(self):
        print("type of cuisine: " + self.cuisine_type)

    def open_restaurant():
        print("the restaurant is now " + self.open_restaurant)

restaurant = Restaurant("Marcelo's", "mexican cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


