import pygame
import math
class cell:

    def __init__(self,x, y, size, color, screen):
        
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.screen = screen
        self.block = False
        self.start = False
        self.end = False;
        self.step =0
        self.row = int((y )/size)
        self.column = int((x)/size)
        self.h = 1.8 *math.sqrt(pow(30 - self.column, 2) +pow( 20 - self.row,2))
        self.f = self.h + self.step 
        self.pre = None

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x+2,self.y+2,self.size-4,self.size-4));

    def SetBlock(self):
        self.color = (255,0,0)
        self.block = True

    def SetStart(self):
        self.color = (0,255,0)
        self.start = True

    def SetEnd(self):
        self.color = (0,0,255)
        self.end = True
    def SetPre(self,  pre):
        self.pre = pre
        self.step = pre.step +1
        self.f = self.h + self.step
