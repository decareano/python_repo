class Dog():
	def __init__(self, name, age):
        self.name = name
    	self.age = age

    def sit(self):
    	""" simulate a dog sitting in response to a command """
    	print(self.name.title() + " is now sitting")

    def roll_over(self):
    	""" simulate rolling over """
    	print(self.name.title() + "is now sitting"

my_dog = Dog('willie', 7)
print("dog name is " + my_dog.name() + ".")
