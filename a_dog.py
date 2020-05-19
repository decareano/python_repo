class Dog():
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def sit(self):
       """ simulate a dog sitting in response to a command """
       print(self.name.title() + " is now sitting")

    def roll_over(self):
       """ simulate rolling over """
       print(self.name.title() + " is now rolling")

my_dog = Dog('willie', 7)
your_dog = Dog('lucy', 3)
print("dog name is " + my_dog.name.title() + ".")
print("dog age is " + str(my_dog.age) + ".")
my_dog.sit()
my_dog.roll_over()
print("\nYour dog's name is " + your_dog.name.title() + ".")
your_dog.sit()