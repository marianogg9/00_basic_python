#!/usr/bin/python3
import random

import pygame
from pygame import Rect
from models import Shape

pygame.init()


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.size = self.scr_width, self.scr_height

        # Background Game
        self.bg = pygame.image.load("images/starsbackground.jpg")
        self.bg = pygame.transform.scale(self.bg, (500, 500))
        self.bg_rect = self.bg.get_rect()

        # Clock
        self.clock = pygame.time.Clock()

        self.shapes = []

        # Init Shapes

        # Time Variables
        self.timecount_m = 0
        self.timecount = 0

        # Init Variables
        self.shape_list = None

        self.init_queue_shape = True
        self.first_shape_creation = True

        self.created_id = 0

        self.score = 0

    def draw_current_shape(self):
        for rect_sh in self.shape_list:
            if ((rect_sh.y + rect_sh.height) <= self.bg_rect.height):
                print(f'{rect_sh.y =}')
                rect_sh.y += 5

            pygame.draw.rect(self.screen, "red", rect_sh)

    def run(self):
        mainloop = True
        while mainloop:

            self.clock.tick(40)
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.bg, self.bg_rect)

            if self.shape_list is None:
                print('now, shape == None')

                self.shape_list = Shape.new_shape().rect_list
                print('some new shape was generated')
                
                for shape in self.shape_list:
                    shape.x = 300 - shape.width / 2 - shape.x

            if self.shape_list is not None:

                self.draw_current_shape()
                
                for shape in self.shape_list:
                    if shape.y + shape.height >= self.scr_height:
                        print(f'reached bottom\n')
                        self.shape_list = None
                        break
                    
            pygame.display.flip()
