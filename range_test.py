aliens = []

for alien_number in range(30):
    new_alien = { 'color': 'green', 'points': 5, 'speed': 'slow' }
    aliens.append(new_alien)


for a in aliens[:7]:
    print(a)
    print("...")

print("total aliens: " + str(len(aliens)))

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("you ordered a " + pizza["crust"] + " -crust pizza " +
      " with the following toppings")

for t in pizza['toppings']:
      print(t)
