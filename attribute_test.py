"""
    python pushes the envelope on OOP
    in python an attribute is anything contained inside an object
    so in example below we have three attributes: title, author and method
    get_entry

    basic attributes access:

"""



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "{0} by {1}".format(self.title, self.author)




    
