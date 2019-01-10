import timeit

min(timeit.repeat(lambda: greet_users([], 0)))
