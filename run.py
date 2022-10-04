import pygame
import random
import time
from pygame.locals import *
from pygame import mixer

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))  

BACKGROUND_IMAGE = pygame.image.load('pictures/background.jpg')

pygame.init()
point_sound = pygame.mixer.Sound('audio/point.wav')
wing_sound = pygame.mixer.Sound('audio/wing.wav')
die_sound = pygame.mixer.Sound('audio/die.wav')

song = pygame.mixer.music.load('audio/song.wav')
pygame.mixer.music.play(-1)

BIRD_IMAGE = pygame.image.load('pictures/bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (10, 82, 14)
OBSTACE_X_CHANGE = -6
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 200  
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))


def collision_detection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,248,0))
    SCREEN.blit(display, (200, 10))


startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    
    display = startFont.render(f"SPACE BAR TO PLAY", True, (255, 255, 255))
    SCREEN.blit(display, (20, 200))

CreditFont = pygame.font.Font('freesansbold.ttf', 32)
def credit():

    display = CreditFont.render(f"Made By Wuttichai", True, (255, 248, 0))
    SCREEN.blit(display, (500, 0))
    pygame.display.update()

score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():

    maximum = max(score_list)
 
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))

    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
   
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        SCREEN.blit(display3, (80, 100))

running = True

waiting = True

collision = False

clock = pygame.time.Clock()

while running:

    clock.tick(60)

    SCREEN.fill((0, 0, 0))


    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

 
    while waiting:
        if collision:
          
            game_over()
            start()
            credit()
        else:
        
            start()
            credit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                   
                    waiting = False

            if event.type == pygame.QUIT:
               
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                    bird_y_change = 3
            
            wing_sound.play()
             


    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571


    obstacle_x += OBSTACE_X_CHANGE


    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 200)

    if collision:
      
        die_sound.play()
        score_list.append(score)
        waiting = True
    
    display_obstacle(OBSTACLE_HEIGHT)


    display_bird(bird_x, bird_y)


    score_display(score)
    

    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
        point_sound.play()
         
    pygame.display.update()

pygame.quit()