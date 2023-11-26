import pygame,random
from pygame import Rect

# Shape
class Shape:
    height: float = 50
    width: float = 50
    left: float = 50
    top: float
    type: str
    name: str

    def __init__(self,name,type,height,width,left,top):
        self.height = height
        self.width = width
        self.left = left
        self.top = top
        self.name = name
        self.type = type
    
    @classmethod
    def new_shape(cls):
        print("this is the Shape.new_shape method") # this is not printed.. but if add a print and return False, pytest works.
        # return False
        try:
            types = {"bar": ShapeBar, "u": ShapeU, "square": ShapeSquare, "s": ShapeS}
            type = "bar" # random.choice(list(types))
            shape_class = types[type]
            print(shape_class)
            name = str(type)
            width,height,left,top = 0,0,0,0

            shape = shape_class(type,name,width,height,left,top)
            
        except KeyError:
            return False
    
        return shape

# ShapeBar
class ShapeBar(Shape):
    type: str = "bar"
    name: str = "bar"
    left: float = 0
    top: float = 0
    width: float = 50
    height: float = 50

    print("this is the ShapeBar class")

    def get_name(self):
        return self.name

    # Rect(left,top,width,height)    

    # def new_shape_bar(self,left,top,width,height):
    #     b = Rect(left,top,width,height)

    #     return b

# ShapeS
class ShapeS(Shape):
    type: str = "s"
    name: str = "s"
    left: float = 0
    top: float = 0
    width: float = 50
    height: float = 50

    print("this is the ShapeS class")

    def get_name(self):
        return self.name

# ShapeSquare
class ShapeSquare:
    left: float
    top: float
    width: float
    height: float

    def __init__(self,left,top,width,height):
        Rect(left,top,width,height)

# ShapeU
class ShapeU:
    left: float
    top: float
    width: float
    height: float

    def __init__(self,left,top,width,height):
        Rect(left,top,width,height)