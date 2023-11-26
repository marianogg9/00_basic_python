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

    @classmethod
    def generate_new_shape(cls):
        s = Shape.new_shape() # models.shape.new_shape
        print(s.name) # this is not printed..
        return s