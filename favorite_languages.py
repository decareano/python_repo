from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

glossary = OrderedDict()

glossary['string'] = "a series of characters"
glossary['comment'] = "a note that is ignored by the interpreter"

for a, b in glossary.items():
    print("\n" + a.title() + ": " + b)
