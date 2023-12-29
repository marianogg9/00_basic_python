#!/usr/bin/python3
import random

import pygame
from pygame.locals import *
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
    
    def rotation90_list(self):
        for rect in self.shape_list:
            temp = rect.y - 20
            rect.y = rect.x
            rect.x = temp    

    # def rotation90(self,rect):
    #     temp = rect.y
    #     rect.y = rect.x
    #     rect.x = temp

    def draw_current_shape(self,shape_color):

        for rect_sh in self.shape_list:
            if ((rect_sh.y + rect_sh.height) <= self.bg_rect.height):
                rect_sh.y += 20
            
            pygame.draw.rect(self.screen, shape_color, rect_sh)

    def run(self):
        mainloop = True
        shape_color = "red"
        while mainloop:
            self.clock.tick(1)
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.bg, self.bg_rect)

            if self.shape_list is None:

                self.shape_list = Shape.new_shape().rect_list
            
                # for shape in self.shape_list:
                #     shape.x = 300 - shape.width / 2 - shape.x

            if self.shape_list is not None:
                # check for user entry (keyboard)
                # call the rotation function
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                            self.rotation90_list()

                self.draw_current_shape(shape_color)

                for shape in self.shape_list:
                    if shape.y + shape.height >= self.scr_height:
                        self.shape_list = None
                        break
                    
            pygame.display.flip()
