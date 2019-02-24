sentence = "The quick brown fox jumps over the lazy dog"
vowels = {'a', 'e', 'i', 'o', 'u'}
for x in range(1000000):
    blah = [i for i in sentence if i in vowels]

print(blah)