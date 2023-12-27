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
    
    @classmethod
    def new_shape(cls):
        print("this is the Shape.new_shape method")
        types = {"bar": ShapeBar, "square": ShapeSquare} #, "u": ShapeU, "square": ShapeSquare, "s": ShapeS}
        type = "square"
        shape_class = types[type]
        name = str(type)

        shape = shape_class(type)
        print(f'{shape.rect_list=}')
    
        return shape

# ShapeBar
class ShapeBar(Shape):

    type: str = "bar"
    name: str = "bar"

    rect_list = [
            Rect(50,50,50,50),
            Rect(100,50,50,50),
            Rect(150,50,50,50),
            Rect(200,50,50,50),
        ]

    def __init__(self,type):
        super().__init__(self.name,self.type,0,0,0,0)
        rect_list = []

# ShapeSquare
class ShapeSquare(Shape):

    type: str = "square"
    name: str = "square"

    rect_list = [   
            Rect(50,50,50,50),
            Rect(100,50,50,50),
            Rect(100,100,50,50),
            Rect(50,100,50,50),
        ]
    
    def __init__(self,type):
        super().__init__(self.name,self.type,0,0,0,0)
        rect_list = []