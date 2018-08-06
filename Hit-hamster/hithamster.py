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

class Hammer():
    def __init__(self, image,(pos_x,pos_y)):
        self.image = image
        self.position = (pos_x,pos_y)
        self.rect = self.image.get_rect()
    def click(self):
        pos_x, pos_y = self. position
        if pos_x < -30:
            pos_x = -30
        elif pos_x > 710:
            pos_x = 710
        if pos_y < -60:
            pos_y = -60
        elif pos_y > 530:
            pos_y = 530
    def render(self):
        screen.blit(self.image,(pos_x,pos_y))

def specific_hole(width, height):
    hole = MySprite()
    hole.load("hole.png", hole_width, hole_height, 1)
    hole.position = width, (height + (hamster_height - hole_height))
    hole_group.add(hole)
        
def draw_hole(hole_numbers):
    i = 0
    hole_array = []
    while i < hole_numbers:
        hole = MySprite()
        hole.load("hole.png", hole_width, hole_height, 1)
        hole.position = random.randint(0,710),random.randint(50,510)
        # Iterate through all positions in the hole array
        hole_occupied = False
        for cur_hole in hole_array:
            if is_occupied(cur_hole, hole.position, hamster_width, hamster_height):
                hole_occupied = True
                break
        if hole_occupied == False:
            i += 1
            hole_group.add(hole)
            hole_array.append(hole.position)
    return hole_array
    
def draw_hamster(hole_array, hole_numbers, hamster_numbers):
    i = 0
    hamster_array = set()
    while i < hamster_numbers:
        select_hole_index = random.randint(0, hole_numbers-1)
        if select_hole_index not in hamster_array:
            hamster = MySprite()
            hamster.load("hamster.png", 113, 84, 1)
            i += 1
            hamster_array.add(select_hole_index)
            hamster.position = hole_array[select_hole_index]
            hamster_group.add(hamster)

            hole_occupied = pygame.sprite.spritecollideany(hamster, hole_group)
            if hole_occupied != None:
                if pygame.sprite.collide_circle_ratio(0.65)(hamster,hole_occupied):
                    hole_group.remove(hole_occupied)
    print hamster_array
    
def data_read():
    data = open("data.txt","r")
    best_score = data.read()
    data.close()
    return best_score

def data_write(best_score):
    data = open("data.txt","w+")
    data.write(str(best_score))
    data.close()


        
#interface image
pygame.init() #Initialize a window or screen for display
screen = pygame.display.set_mode((800,600)) #Set the current window caption
pygame.display.set_caption("Hithamster")
font1   = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 10)

# button image 
upImageFilename = 'game_start_up.jpg'
downImageFilename = 'game_start_down.jpg'
restart_up_button_image = 'game_restart_up.jpg'
restart_down_button_image = 'game_restart_down.jpg'

# sound
pygame.mixer.init() #initialize the mixer module  
start_sound = Music(pygame.mixer.Sound("background.ogg"))#Create a new Sound object from a file or buffer object
hit_sound = Music(pygame.mixer.Sound("beat.wav"))

interface = pygame.image.load("interface.jpg").convert_alpha()

# start button
start_button = Button(upImageFilename,downImageFilename, (400,550))

# restart button
restart_button = Button(restart_up_button_image,restart_down_button_image, (400,550))

# background color
bg_color = 153,204,51

#opensound
#start_sound.play_sound()

# init mouse
pygame.mouse.set_visible(True)
mouse_x = mouse_y = 0
pos_x = 0
pos_y = 0

#load hammer image
hammer_up = pygame.image.load("hammer_up.jpg")
hammer_down = pygame.image.load("hammer_down.png")

#init the hole group
hole_group = pygame.sprite.Group()
hamster_group = pygame.sprite.Group()

# init the parameter of holes and hammers
hole_numbers = 20
hamster_numbers = 5
hole_width = 90
hole_height = 31
hamster_width = 113
hamster_height = 84
hole_array = draw_hole(hole_numbers)


restart_game = False
game_over = False
round_start = True
score = 0
best_score = data_read()
game_round =1

# init the interface and button
screen.blit(interface, (0,0))
start_button.render()

game_over_counter = 0
restart_game_clicked = False

pygame.time.set_timer(pygame.USEREVENT, 1000)

#main function
while True:
    if game_over is False:
        if score == 0:
            if round_start is True:
                game_round = 1
                second = 8
                draw_hamster(hole_array, hole_numbers, hamster_numbers)
                round_start = False
        elif score >= 5 and score < 10:
            if round_start is True:
                game_round = 2
                second = 5
                draw_hamster(hole_array, hole_numbers, hamster_numbers)
                round_start = False
        elif score >= 10 and score < 15:
            if round_start is True:
                game_round = 3
                second = 3
                draw_hamster(hole_array, hole_numbers, hamster_numbers)
                round_start = False
        elif score == 15:
            game_over = True
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x,mouse_y = event.pos
                move_x,move_y = event.rel
                width,height=hammer_up.get_size()
                pic = pygame.transform.scale(hammer_up,(width,height))
            elif event.type == MOUSEBUTTONUP:
                width,height = hammer_up.get_size()
                pic = pygame.transform.scale(hammer_down,(width,height))
            elif event.type == pygame.USEREVENT:
                if second >= 1:
                    second = second - 1 
                elif second == 0:
                    game_over_counter += 1
                    print "Game Over! %s" % game_over_counter
                    game_over = True
                    
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        
        start_button.is_start()
        if start_button.game_start is True:
            pygame.mouse.set_visible(False)
            screen.fill(bg_color)
            hole_group.draw(screen)
            hamster_group.draw(screen)
            pos_x = mouse_x
            pos_y = mouse_y
            hammer = Hammer(pic, (pos_x, pos_y))
            hammer.click()
            hammer.render()
            for hamster in hamster_group:
                if is_occupied(hammer.position, hamster.position, hamster_width, hamster_height):
                    if event.type == MOUSEBUTTONUP:
                        hamster_group.remove(hamster)
                        specific_hole(hamster.position[0], hamster.position[1])
                        score = score + 1 
                        if score == 5 * game_round:
                            round_start = True

            #draw the score    
            print_text(font1, 280, 0, "score: " + str(score))   
            #draw the Round
            print_text(font1, 0, 0, "Round: " + str(game_round))
            #draw the time 
            print_text(font1, 560, 0, "second: " + str(second)) 
        
    elif game_over is True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                move_x, move_y = event.rel

        pygame.mouse.set_visible(True)
        if score < 5 * game_round:
            if score > int(best_score):
                best_score = score
                data_write(best_score)
            best_score = data_read()
            screen.fill((200, 200, 200))
            print_text(font1, 270, 150, "Sorry, you failed!", (240, 20, 20))
            print_text(font1, 320, 250, "Best Score:", (120, 224, 22))
            print_text(font1, 370, 290, str(best_score), (255, 0, 0))
        elif score == 15:
            if score > int(best_score):
                best_score = score
                data_write(best_score)
            best_score = data_read()
            screen.fill((200, 200, 200))
            print_text(font1, 270, 150, "YOU WIN THE GAME!", (240, 20, 20))
            print_text(font1, 320, 250, "Best Score:", (120, 224, 22))
            print_text(font1, 370, 290, str(best_score), (255, 0, 0))

        if True:
            restart_button.render()  
            restart_button.is_start()
            if not hamster_group.empty():
                for hamster in hamster_group:
                    hamster_group.remove(hamster)
                    specific_hole(hamster.position[0], hamster.position[1])
            if restart_button.game_start is True:
                print "Restart game..."
                score = 0
                best_score = data_read()
                game_round = 1
                game_over = False
                round_start = True
                start_button.is_start()
                restart_button.game_start = False
    pygame.display.update()  


