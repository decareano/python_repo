def describe_pet(animal_type, pet_name):
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

def make_shirt(size):
	print("my shirt is " + size + " and it has written: I love python")

make_shirt('large')

def make_shirt(message, size="large"):
        print("\n" " my shirt is " + size + " and the label is " + message)
make_shirt("I love c")
make_shirt("I love python", size="medium")
make_shirt("I dislike perl", size="any")

def describe_city(city_name, country_name):
	print("\t" + city_name + " is in " + country_name)

describe_city("buenos aires", "argentina")

def describe_city(city_name, country_name="argentina"):
	print("\t" + city_name + " is in " + country_name)

describe_city("buenos aires", "argentina")
describe_city("la paz", "bolivia")
describe_city("buenos aires")


