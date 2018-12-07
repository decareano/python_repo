favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for n , program in favorite_languages.items():
    print("\n " , n.title() + "'s favorite language is " +
            program.title())

friends = ['phil', 'sarah']
for n in favorite_languages.keys():
    print(n.title())


