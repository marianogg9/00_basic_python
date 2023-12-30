import pygame,random
from pygame import Rect

# new class shapeFactory (to generate a shape)

# shape class: all attributes of a given shape

# Shape
class Shape: 
    height: float
    width: float
    left: float
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
        self.rect_list = []
    
    @classmethod
    def new_shape(cls):
        # print("this is the Shape.new_shape method")
        types = {"bar": ShapeBar, "square": ShapeSquare, "u": ShapeU, "square": ShapeSquare, "s": ShapeS}
        # type = random.choice(list(types))
        type = "bar"
        shape_class = types[type]
        name = str(type)

        shape = shape_class(type)
        # print(f'{shape.rect_list=}')
    
        return shape

# ShapeBar
class ShapeBar(Shape):

    type: str = "bar"
    name: str = "bar"

    def __init__(self,type):
        self.rect_list = [
            Rect(50,50,50,50),
            Rect(100,50,50,50),
            Rect(150,50,50,50),
            Rect(200,50,50,50),
            Rect(250,50,50,50),
        ]

# ShapeSquare
class ShapeSquare(Shape):

    type: str = "square"
    name: str = "square"
    
    def __init__(self,type):
        self.rect_list = [
            Rect(40,40,40,40),
            Rect(80,40,40,40),
            Rect(80,80,40,40),
            Rect(40,80,40,40),
        ]

# ShapeS
class ShapeS(Shape):

    type: str = "s"
    name: str = "s"
    
    def __init__(self,type):
        self.rect_list = [
            Rect(50,50,50,50),
            Rect(100,50,50,50),
            Rect(150,50,50,50),
            Rect(150,100,50,50),
            Rect(150,150,50,50),
            Rect(100,150,50,50),
            Rect(50,150,50,50),
            Rect(50,200,50,50),
            Rect(50,250,50,50),
            Rect(100,250,50,50),
            Rect(150,250,50,50)
        ]

# ShapeU
class ShapeU(Shape):

    type: str = "u"
    name: str = "u"
    
    def __init__(self,type):
        self.rect_list = [
            Rect(150,150,50,50),
            Rect(150,100,50,50),
            Rect(150,50,50,50),
            Rect(100,150,50,50),
            Rect(50,50,50,50),
            Rect(50,100,50,50),
            Rect(50,150,50,50),
        ]