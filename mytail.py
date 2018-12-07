#!/usr/bin/python
import sys

class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)


    def get(self, x):
        return self.data[x]

f = open(sys.argv[2], "r")
count = int(sys.argv[1])
buf = RingBuffer(count)
for x in f:
	buf.append(x)
for y in range(count):
	print(buf.get(y))


#class ringbuffer has two methods append and get.
#append has 1 variables data.pop and data.append