objects = {'python', 'coding', 'tips', 'for', 'beginners'}
""" set is unordered, unique and immutable
"""
print(objects)
print(len(objects))

if 'tips' in objects:
    print("good python tips")

if 'java tips' not in objects:
    print("these are python tips not java tips")

items = set()

items.add('python')
items.add('coding')
items.add('tips')

print("my list is: " + str(items))
