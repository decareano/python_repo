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

singers = []
for i in sorted(songs.values()):
    singers.append(i)

print(singers)

for h in sorted(songs.keys()):
  print(h)


singerset = set(singers)
print(singerset)
singerset1 = list(singerset)
print(singerset1)

for h in singerset1:
    print("{}: ".format(h))
    for eachsong, a_band in songs.items():
           if a_band == h:
               print("      {} ".format(eachsong))           
    






# for t, (k, v) in enumerate(songs.items()):
#    print(" {}, {}".format(k, v))

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
