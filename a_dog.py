class Dog():
  def __init__(self, name, age):
    self.name = name
    self.age = age

my_dog = Dog('Willie', 6)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog age is " + str(my_dog.age)
