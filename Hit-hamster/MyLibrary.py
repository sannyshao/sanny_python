# MyLibrary.py

import sys, time, random, math, pygame
from pygame.locals import *


# Print the words on screen 
"""
font : the font where the words will be 
x,y  : the position where the words will be 
text : the word which you want to write
color: the color which the word will be
"""
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color,font) # draw text on a new Surface
    screen = pygame.display.get_surface() # Get a reference to the currently set display surface
    screen.blit(imgText, (x,y)) #draw one image onto another

def is_occupied(cur_hole, new_hole, width, height):
    if new_hole[0] >= cur_hole[0] - width and new_hole[0] <= cur_hole[0] + width and new_hole[1] >= cur_hole[1] - height and new_hole[1] <= cur_hole[1] + height:
        return True
    else:
        return False




class MySprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #Simple base class for visible game objects.
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0

    #X property
    def _getx(self): 
        return self.rect.x
    def _setx(self,value): 
        self.rect.x = value
    X = property(_getx,_setx)

    #Y property
    def _gety(self): 
        return self.rect.y
    def _sety(self,value): 
        self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): 
        return self.rect.topleft
    def _setpos(self,pos): 
        self.rect.topleft = pos
    position = property(_getpos,_setpos)
        
    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.image = self.master_image.subsurface(rect)
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

