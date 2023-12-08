#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
     

    #getter and setter for size
    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        if kwargs:
            #size will be provided instead of width
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'id' in kwargs:
                self.id = kwargs['id']

        
    def to_dictionary(self):
        n = dict()

        n = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return n


        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
