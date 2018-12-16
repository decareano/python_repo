favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")

numbers = list(range(1, 21))
for i in numbers:
    print(i)

threes = list(range(4, 40, 4))
for n in threes:
    print(n)

cubes = []

for a in range(1, 10):
    cube = a**3
    cubes.append(cube)
    

for cube in cubes:
    print(cube)

#with cube comprehension

cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)
    
