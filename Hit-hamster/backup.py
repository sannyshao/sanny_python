# -*- coding: utf-8 -*-
import sys, time, random, math, pygame, threading
from pygame.locals import *
from MyLibrary import *

#Define the butten
class Button(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.game_start = False
    def click(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()
        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y
    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        if self.click():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
    def is_start(self):
        if self.click():
            b1,b2,b3 = pygame.mouse.get_pressed()
            if b1 == 1:
                self.game_start = True
                start_sound.play_sound()

class Music():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound     
    def play_sound(self):
        self.channel = pygame.mixer.find_channel(True) #find an unused channel
        self.channel.set_volume(0.5) #set the volume of a playing channel
        self.channel.play(self.sound)#play a Sound on a specific Channel
    def play_pause(self):
        self.channel.set_volume(0.0) 
        self.channel.play(self.sound)

#interface image
pygame.init() #Initialize a window or screen for display
screen = pygame.display.set_mode((800,600)) #Set the current window caption
pygame.display.set_caption("Hithamster")
font   = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 10)

# button image 
upImageFilename = 'game_start_up.jpg'
downImageFilename = 'game_start_down.jpg'

# sound
pygame.mixer.init() #initialize the mixer module  
start_sound = Music(pygame.mixer.Sound("background.ogg"))#Create a new Sound object from a file or buffer object
hit_sound = Music(pygame.mixer.Sound("beat.wav"))

interface = pygame.image.load("interface.jpg").convert_alpha()
button = Button(upImageFilename,downImageFilename, (400,550))

# background color
bg_color = 153,204,51

# init timer 
timer = pygame.time.Clock()

#opensound
#start_sound.play_sound()

#init the hole group
hole_group = pygame.sprite.Group()
hamster_group = pygame.sprite.Group()

# init mouse
pygame.mouse.set_visible(True)
mouse_x = mouse_y = 0
pos_x = 0
pos_y = 0

#load hammer image
hammer_up = pygame.image.load("hammer_up.jpg")
hammer_down = pygame.image.load("hammer_down.png")

score = 0
Round =1
clock_start = 0
game_over = 1

# Draw the holes 
hole_numbers = 20
hamster_numbers = 5
hole_width = 90
hole_height = 31
hammer_width = 113
hammer_height = 84

def init_background():
    print "calm"
    pygame.mouse.set_visible(False)
    screen.fill(bg_color)
    hole_group.draw(screen)

def init_round(current_round):
    print "sanny"
    print current_round
    # Inital current round
    if current_round == 1:
        hamster_numbers = 1
    elif current_round == 2:
        hamster_numbers = 3
    elif current_round == 3:
        hamster_numbers = 6
    elif current_round == 4:
        hamster_numbers = 10
    elif current_round == 5:
        hamster_numbers = 15
    draw_hamster(hole_array, hole_numbers, hamster_numbers)
    hamster_group.draw(screen)

# def play_round(current_round):
    # Play current round


def is_occupied(cur_hole, new_hole, width, height):
    if new_hole[0] >= cur_hole[0] - width and new_hole[0] <= cur_hole[0] + width and new_hole[1] >= cur_hole[1] - height and new_hole[1] <= cur_hole[1] + height:
        return True
    else:
        return False
#hole_array = draw_hole(hole_numbers)
#draw_hammer(hole_array, hamster_numbers)
#def draw_hole(hole_numbers):
hole_array = []
while hole_numbers > 0:
    hole = MySprite()
    hole.load("hole.png", hole_width, hole_height, 1)
    hole.position = random.randint(0,710),random.randint(50,510)
    # Iterate through all positions in the hole array
    hole_occupied = False
    for cur_hole in hole_array:
        if is_occupied(cur_hole, hole.position, hammer_width, hammer_height):
            hole_occupied = True
            break
    if hole_occupied == False:
        hole_numbers -= 1
        hole_group.add(hole)
        hole_array.append(hole.position)
#return hole_array

# Draw the hammer 
#def draw_hammer(hole_array, hamster_numbers):
hamster_array = set()
while hamster_numbers > 0:
    select_hole_index = random.randint(0, hamster_numbers-1)
    if select_hole_index not in hamster_array:
        hamster = MySprite()
        hamster.load("hamster.png", 113, 84, 1)
        hamster_numbers -= 1
        hamster_array.add(select_hole_index)
        hamster.position = hole_array[select_hole_index]
        hamster_group.add(hamster)
    
        hole_occupied = pygame.sprite.spritecollideany(hamster, hole_group)
        if hole_occupied != None:
            if pygame.sprite.collide_circle_ratio(0.65)(hamster,hole_occupied):
                hole_group.remove(hole_occupied)

#main function
while True:
    #timer.tick(30)
    #ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
            width,height=hammer_up.get_size()
            pic=pygame.transform.scale(hammer_up,(width,height))
        elif event.type == MOUSEBUTTONUP:
            width,height = hammer_up.get_size()
            pic = pygame.transform.scale(hammer_down,(width,height))

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(interface, (0,0))

    button.render()
    button.is_start()
    if button.game_start == True:
        pygame.mouse.set_visible(False)
        screen.fill(bg_color)
       #hole_group.draw(screen)
       #hamster_group.draw(screen)
       #hole_group.update(ticks, 500)
       #hamster_group.update(ticks, 10)
       
       #set hammer position
        pos_x = mouse_x
        pos_y = mouse_y
        if pos_x < -30:
            pos_x = -30
        elif pos_x > 710:
            pos_x = 710
        if pos_y < -60:
            pos_y = -60
        elif pos_y > 530:
            pos_y = 530
        screen.blit(pic,(pos_x,pos_y))


        
    pygame.display.update()
        
        
        
"""
        Countdown = 11
        for i in range(11): 
            Countdown = 11-i
            clock = "Countdown: %s " % Countdown
            print clock
            print_text(font, 0, 0, clock)
"""        