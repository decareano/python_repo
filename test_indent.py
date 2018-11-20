alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("sarah favorite language is " + favorite_languages['sarah'].title() +
      ".")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# for k, v in user_0.items():
  #  print("\nKey: " + k)
   # print("Value: " + v)

friends = ['phil', 'sarah']
for n in favorite_languages:
    print(n.title())

    if n in friends:
        print(" Hi " + n.title() + ", I see your fave lang is " +
              favorite_languages[n].title() + "!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

    
print("the following lang have been mentioned:")
for lang in favorite_languages.values():
    print(lang.title())

print("the following lang have been mentioned:")
for lang in set(favorite_languages.values()):
    print(lang.title())
