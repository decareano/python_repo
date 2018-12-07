class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]
        

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

        

buf = RingBuffer(4)
for i in xrange(10):
    buf.append(i)
    print buf.get()


# a ringbuffer instance is created
# it has two methods append and get
# not sure what they do
# Capitalized names refer to classes
# __init__ has two parameters (self, size)
# self required. python needs it to create the instance.
# methods prefix with self are available to every method in the class.
# variables accessed through instances are called attributes