songs = {                       
        'material girl': 'madonna',
	'oh my': 'madonna',
	'billie jean': 'michael jackson',
	'thriller': 'michael jackson',
	'hey jude': 'beatles',
	'imagine': 'beatles',
	'purple haze': 'jimi hendrix',
	'red house': 'jimi hendrix',
}

for t in enumerate(songs):
    print(t)

print(" ")


for t, (k, v) in enumerate(songs.items()):
    print(" key: {}, value: {}".format(k, v))

"""
Explanations:

enumerate returns an iterator object which contains tuples in the format: [(index, list_element), ...]
dict.items() returns an iterator object (in Python 3.x. It returns list in Python 2.7) in the format: [(key, value), ...]
On combining together, enumerate(dict.items()) will return an iterator object containing tuples in the format: [(index, (key, value)), ...]

"""
a = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(str.join(" ", (a)))

print('\n')

for t in range(9):
    print(a[t])

print('\n')

for t in reversed(a):
    print(t)
