def make_shirt(size):
  print("my shirt is " + size + " and it has written: I love python")

make_shirt('large')

def make_shirt(message, size = "large"):
  print("\n"
    " my shirt is " + size + " and the label is " + message)
make_shirt("I love c")
make_shirt("I love python", size = "medium")
make_shirt("I dislike perl", size = "any")

def describe_city(city_name, country_name):
  print("\t" + city_name + " is in " + country_name)

describe_city("buenos aires", "argentina")

def describe_city(city_name, country_name = "argentina"):
  print("\t" + city_name + " is in " + country_name)

describe_city("buenos aires", "argentina")
describe_city("la paz", "bolivia")
describe_city("buenos aires")

def get_formatted_name(first_name, last_name):
  full_name = first_name + ' ' + last_name
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
  if middle_name:
    full_name = first_name + ' ' + middle_name + ' ' + last_name
  else:
    full_name = first_name + ' ' + last_name
  return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('john', 'wayne')
print(musician)
