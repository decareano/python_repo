def separate_string(sentence):
    l = list(sentence)
    list_even = list()
    list_odd = list()
    index = 0
    for letter in l:
        if index % 2 != 0:
            list_even.append(letter)
        else:
            list_odd.append(letter)
        index += 1
    evens = "".join(list_even)
    odds = "".join(list_odd)

    print(evens)
    print(odds)

separate_string('abcedfg')
