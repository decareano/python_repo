user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thanks for taking the poll.")

print("the following languages have been mentioned:")
for l in set(favorite_languages.values()):
	print(l.title())


