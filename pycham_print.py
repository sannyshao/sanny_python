import pygame
import math
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()

    screen.fill((0,200,200))
    
    pos_x += vel_x
    pos_y += vel_y
    
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y        
    
    color = 255,255,255
    #position = pos_x, pos_y
    #radius = 100
    start_point = (pos_x,pos_x)
    end_point = (pos_y,pos_y)
    width = 10
    #start_angle = math.radians(0)
    #end_angle = math.radians(180)
    pygame.draw.line(screen, color, start_point, end_point, width)
    
    pygame.display.update()