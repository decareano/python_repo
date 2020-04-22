favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],

    }

for n, lang in favorite_languages.items():
    print("\n" + n.title() + "'s favorite languages are:")
    for l in lang:
        print("\t" + l.title())
