# Importing the library
import pygame
import time
import random
import sys

# Initializing the pygame
pygame.init()

# window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CAR RACING")

# Loading all images
c1_img = pygame.image.load("car1.jpeg")
clock = pygame.time.Clock()
grass = pygame.image.load("grass.jpeg")
y_strip = pygame.image.load("y_strip.jpeg")
strip = pygame.image.load("strip.jpeg")
start = pygame.image.load("start.jpeg")

# Function for getting all images
def background():
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(y_strip, (400, 0))
    screen.blit(y_strip, (400, 100))
    screen.blit(y_strip, (400, 200))
    screen.blit(y_strip, (400, 300))
    screen.blit(y_strip, (400, 400))
    screen.blit(y_strip, (400, 500))
    screen.blit(y_strip, (400, 600))
    screen.blit(strip, (120, 0))
    screen.blit(strip, (680, 0))

# Getting the car on screen
def car(x, y):
    screen.blit(c1_img, (x, y))

x_change = 0
x = 400
y = 470
car_width = 56
op_speed = 10
obs = 0
y_change = 0
obs_x = random.randrange(200, 650)
obs_y = -750
op_width = 56
op_height = 125
car_passed = 0
score = 0
level = 0

# Function to display score
def sc(car_passed, score):
    s_font = pygame.font.SysFont(None, 35)
    passed = s_font.render("Passed:" + str(car_passed), True, (0, 0, 0))
    score = s_font.render("Score:" + str(score), True, (0, 0, 0))
    screen.blit(passed, (0, 30))
    screen.blit(score, (0, 70))

# Game loop
def game_loop():
    global op_speed, x, car_passed, level, x_change, y_change, y, obs_y, obs_x, obs, score, font
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUIT event
                running = False
            if event.type == pygame.KEYDOWN:  # KEYDOWN event
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_s:  # Increase speed
                    op_speed += 2
                if event.key == pygame.K_b:  # decrease speed
                    op_speed -= 2
            if event.type == pygame.KEYUP:  # KEYUP event
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill((119, 119, 119))
        background()
        obs_y -= (op_speed / 4)
        obstacle(obs_x, obs_y, obs)
        obs_y += op_speed
        car(x, y)
        sc(car_passed, score)

        if obs_y > 600:
            obs_y = 0 - op_height
            obs_x = random.randrange(170, 600)
            obs = random.randrange(0, 6)
            car_passed += 1
            score = car_passed * 10
            if int(car_passed) % 10 == 0:
                level += 1
                op_speed += 2

        pygame.display.update()
        clock.tick(60)

# Function for enemy cars
def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_img = pygame.image.load("car2.jpeg")
    elif obs == 1:
        obs_img = pygame.image.load("car3.jpeg")
    elif obs == 2:
        obs_img = pygame.image.load("car4.jpeg")
    elif obs == 3:
        obs_img = pygame.image.load("car5.jpeg")
    elif obs == 4:
        obs_img = pygame.image.load("car6.jpeg")
    elif obs == 5:
        obs_img = pygame.image.load("car7.jpeg")
    screen.blit(obs_img, (obs_x, obs_y))

game_loop()
pygame.quit()
