favorite_numbers = {
	'mandy': 42,
	'micah': 23,
	'gus':  7,
	'hank': 1000000,
	'maggie': 0,
	}
num = favorite_numbers['mandy']
print("Mandy favorite number is " + str(num) + ".")

for name, number in enumerate(favorite_numbers):
	print("the favorite numbers for my friends are: " + str(name), str(number))

grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
	print(item)
print('\n')
for count, item in enumerate(grocery):
	print(count, item)
print('\n')
for count, item in enumerate(grocery, 100):
	print(count, item)


