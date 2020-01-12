import pygame
class cell:

    """Docstring for cell. """

    def __init__(self,x, y, size, color, screen):
        """TODO: to be defined. """
        
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.screen = screen
        

    def draw():
        pygame.rect.draw(screen, color, (x,y,size,size));
