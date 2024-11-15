"""
Program name : Jeu de Dames
Author : Cédric Jankiewicz et Thierry Perroud
Date : 08.11.2024
"""

import pygame

def display_grid():
    location_y = 5
    for i in range(0,5):
        location_x = 5
        for j in range(0,5):
                pygame.draw.rect(screen, (255, 255, 255), (location_x, location_y, 100, 100), 0)
                location_x +=100
                pygame.draw.rect(screen, (150, 150, 150), (location_x, location_y, 100, 100), 0)
                location_x +=100

        location_y += 100
        location_x = 5
        for j in range(0,5):
                pygame.draw.rect(screen, (150, 150, 150), (location_x, location_y, 100, 100), 0)
                location_x +=100
                pygame.draw.rect(screen, (255, 255, 255), (location_x, location_y, 100, 100), 0)
                location_x +=100

        location_y += 100

def move_right():
        global x
        if x < 905:
            x+=100
            screen.fill((0, 0, 0))
            display_grid()
            screen.blit(pawn, (x, y))

def move_left():
        global x
        if x > 5:
            x-=100
            screen.fill((0, 0, 0))
            display_grid()
            screen.blit(pawn, (x, y))


def move_up():
    global y
    if y > 5:
        y -= 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_down():
    global y
    if y < 905:
        y += 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_up_left():
    global x,y
    if x > 5 and y > 5:
        x -= 50
        y -= 50
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_up_right():
    global x,y
    if x < 905 and y > 5:
        x += 50
        y -= 50
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_down_left():
    global x,y
    if x > 5 and y < 905:
        x -= 50
        y += 50
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_down_right():
    global x,y
    if x < 905 and y < 905:
        x += 50
        y += 50
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

#variable
x=5
y=5
#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

#création de la grille
display_grid()

#affichage du pion
pawn = pygame.image.load(".resources\\MA-24_pion.png")
pawn = pygame.transform.scale(pawn, (100,100))
screen.blit(pawn, (x, y))

running=True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                btn_pressed = pygame.key.get_pressed()
                if btn_pressed[pygame.K_RIGHT]:
                        move_right()
                elif btn_pressed[pygame.K_LEFT]:
                        move_left()
                elif btn_pressed[pygame.K_UP]:
                        move_up()
                elif btn_pressed[pygame.K_DOWN]:
                        move_down()
                elif btn_pressed[pygame.K_q]:
                        move_up_left()
                elif btn_pressed[pygame.K_e]:
                        move_up_right()
                elif btn_pressed[pygame.K_a]:
                        move_down_left()
                elif btn_pressed[pygame.K_d]:
                        move_down_right()
                elif btn_pressed[pygame.K_ESCAPE]:
                    running = False
        pygame.display.update()
pygame.quit()