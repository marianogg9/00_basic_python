import pygame
from pygame import Rect
from oop_5.exercise_2.models import Shape,ShapeBar,ShapeS,ShapeU,ShapeSquare

# ShapeFactory

class ShapeFactory:
    colors: list = ["green","red","yellow","blue"]
    shapes: list = [ShapeBar,ShapeS,ShapeU,ShapeSquare]
    name: str
    type: str

    def __init__(self,name):
        self.name = name

    # debug
    @classmethod
    def generate_new_shape(cls):
        return Shape.new_shape() # models.shape.new_shape

    # def generate_combined_shape(shape1,shape2):
    #     return Shape.generate_combined_shape(shape1,shape2)
    
    @classmethod
    def new_shape(cls):
        # debug
        # print("this is the Shape.new_shape method")
        
        types = {"bar": ShapeBar, "u": ShapeU, "square": ShapeSquare, "s": ShapeS}
        type = random.choice(list(types))
        shape_class = types[type]
        # print(shape_class)
        name = str(type)
        width,height,left,top = 0,0,0,0

        shape = shape_class(type,name,width,height,left,top)
    
        return shape

    def generate_combined_shape(shape1,shape2):
        shape = shape1
        shape.name = "custom"
        for rect in shape2.rect_list:
            shape.rect_list.append(rect)

        return shape