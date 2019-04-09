numbers = [4, 2, 1, 6, 9, 7]
def square(x):
  return x*x + 1

def is_odd(x):
    return bool(x%2)


# map(funtion, iterable, ...) it applies function to every member of iter and returns a result

def get_name_and_decades(name, age):
    print("my name is {name} and I am {age /10:.5f} decades old")



def approximate_size(size, a_kilobyte_is_1024_bytes=True): 
    if size < 0: 
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]: 
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    raise ValueError('number too large')

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

#import unittest

def reverse(list_of_chars):

        left_index = 0
        right_index = len(list_of_chars) - 1
        #import pdb; pdb.set_trace()

              
        while left_index < right_index:
                list_of_chars[left_index], list_of_chars[right_index] = list_of_chars[right_index], list_of_chars[left_index]

                left_index += 1
                right_index -= 1

