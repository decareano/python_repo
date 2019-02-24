def linear_search(v):
    """ return the index of the first ocurrence of v in list L, or return len(L)
        if v is not in L

    """
    i = 0
    l = range(1, 101)
    while i != len(l) and l[i] != v:
        i = i + 1
    return i
     
print(linear_search(5))

