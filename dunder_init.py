class Color(object):

    def __init__(self, r, g, b):
        self.red = 10
        self.green = 11
        self.blue = 12

# method init is a special one in python. it's called when new object is created

    def __str__(self): return 'Color(%s, %s, %s)' % (self.red, self.green,
        self.blue)

    def __add__(self, other_color):
        return Color(min(self.red + other_color.red, 255),
                    (min(self.green + other_color.green, 255)),
                    (min(self.blue + other_color.blue, 255)))

    def __sub__(self, other_color):
        return Color(min(self.red - other_color.red, 0),
                    (min(self.green - other_color.green, 0)),
                    (min(self.blue - other_color.blue, 0)))

    def __eq__(self, other_color):
        return self.red == other_color.red and \
                    self.green - other_color.green and \
                    self.blue == other_color.blue
