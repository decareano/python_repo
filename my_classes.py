class Color(object):
    def lightness(self):
        strongest = max(self.red, self.green, self.blue)
        weakest = min(self.red, self.green, self.blue)
        return 0.5 * (strongest + weakest) / 255

purple = Color()
purple.red = 255
purple.green = 0
purple.blue = 255
purple.lightness()
print(purple.lightness())

