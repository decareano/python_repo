names = ['ron', 'tyler', 'dani']
msg = "Hello, " + names[0].title() + "!"
print(msg)

for name in names:
    print(name)

guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(name + ", please come to dinner")
del(guests[1])
guests.insert(1, 'gary snyder')
print(guests)
locations = ['buenos aires', 'montevideo', 'asuncion', 'santiago', 'lima']
print(locations)
print(sorted(locations))

print(sorted(locations, reverse=True))
locations = ['buenos aires', 'montevideo', 'asuncion', 'santiago', 'lima']
locations.sort()
print(locations)

print(sorted(locations, reverse=True))
