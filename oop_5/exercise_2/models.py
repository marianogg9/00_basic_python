import pygame,random
from pygame import Rect

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
        print("this is the Shape.new_shape method") # this is not printed.. but if add a print and return False, pytest prints this.
        # return False
        types = {"bar": ShapeBar, "u": ShapeU, "square": ShapeSquare, "s": ShapeS}
        type = random.choice(list(types))
        shape_class = types[type]
        print(shape_class)
        name = str(type)
        width,height,left,top = 0,0,0,0

        shape = shape_class(type,name,width,height,left,top)
    
        return shape

    def generate_combined_shape(shape1,shape2):
        shape = Rect.unionall_ip(shape1,shape2)
        return shape

# ShapeBar
class ShapeBar(Shape): 
    ## bar: 4 in the same column:
    # (0,0,0,0)
    # (1,0,0,0)
    # (2,0,0,0)
    # (3,0,0,0)

    type: str = "bar"
    name: str = "bar"

    def get_name(self):
        return self.name

    def new_bar():
        rect_list = []
        for i in range(4):
            rect_list.append(Rect(i,0,0,0))
        
        return rect_list

# ShapeS
class ShapeS(Shape): 
    ## s: 
    #           (0,1,0,0),(0,2,0,0)
    #           (1,0,0,0)
    # (2,0,0,0),(2,1,0,0)

    type: str = "s"
    name: str = "s"

    def new_s():
        rect_list = []
        for i in range(1,3):
            rect_list.append(Rect(0,i,0,0))
        rect_list.append(Rect(1,0,0))
        for i in range(0,2):
            rect_list.append(Rect(2,i,0,0))
        
        return rect_list
    
# ShapeSquare
class ShapeSquare(Shape):
    ## square:
    # (0,0,0,0),(0,1,0,0)
    # (1,0,0,0),(1,1,0,0)

    type: str = "square"
    name: str = "square"

    def new_square():
        rect_list = []
        rect_list.append(Rect(0,0,0,0))
        rect_list.append(Rect(0,1,0,0))
        rect_list.append(Rect(1,0,0,0))
        rect_list.append(Rect(1,1,0,0))
        
        return rect_list

# ShapeU
class ShapeU(Shape):
    ## u:
    # (0,0,0,0),          (0,2,0,0)
    # (1,0,0,0),(1,1,0,0),(1,2,0,0)

    left: float
    top: float
    width: float
    height: float

    type: str = "u"
    name: str = "u"

    def new_u():
        rect_list = []
        rect_list.append(Rect(0,0,0,0))
        rect_list.append(Rect(0,2,0,0))
        rect_list.append(Rect(1,0,0,0))
        rect_list.append(Rect(1,1,0,0))
        rect_list.append(Rect(1,2,0,0))
        
        return rect_list