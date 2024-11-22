"""
Program name : Jeu de Dames
Author : Cédric Jankiewicz et Thierry Perroud
Date : 18.11.2024
"""

import pygame

class Pawn:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.selected = 0
        self.pawn = pygame.image.load(".resources\\MA-24_pion.png")
        self.pawn = pygame.transform.scale(self.pawn, (100, 100))

    def move_right(self):
        if self.x < 905:
            self.x += 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_left(self):
        if self.x > 5:
            self.x -= 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_up(self):
        if self.y > 5:
            self.y -= 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_down(self):
        if self.y < 5:
            self.y += 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_up_left(self):
        if self.x > 5 and self.y > 5:
            self.x -= 100
            self.y -= 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_up_right(self):
        if self.x < 905 and self.y > 5:
            self.x += 100
            self.y -= 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_down_left(self):
        if self.x > 5 and self.y < 905:
            self.x -= 100
            self.y += 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def move_down_right(self):
        if self.x < 905 and self.y < 905:
            self.x += 100
            self.y += 100
            screen.fill((0, 0, 0))
            display_grid()
            display_pawns()

    def select_pawn(self):
        if self.x <= event.pos[0] <= self.x + 100 and self.y <= event.pos[1] <= self.y + 100:
            pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)
            self.selected = 1

    def move_pawn(self):
        if self.x <= event.pos[0] <= self.x + 100 and self.y + 100 <= event.pos[1] <= self.y + 200 and self.selected == 1:
            self.selected = 0
            self.move_down()
        if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y + 100 <= event.pos[1] <= self.y + 200 and self.selected == 1:
            self.selected = 0
            self.move_down_right()
        if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y <= event.pos[1] <= self.y + 100 and self.selected == 1:
            self.selected = 0
            self.move_right()
        if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y - 100 <= event.pos[1] <= self.y and self.selected == 1:
            self.selected = 0
            self.move_up_right()
        if self.x <= event.pos[0] <= self.x + 100 and self.y - 100 <= event.pos[1] <= self.y and self.selected == 1:
            self.selected = 0
            self.move_up()
        if self.x - 100 <= event.pos[0] <= self.x and self.y - 100 <= event.pos[1] <= self.y and self.selected == 1:
            self.selected = 0
            self.move_up_left()
        if self.x - 100 <= event.pos[0] <= self.x and self.y <= event.pos[1] <= self.y + 100 and self.selected == 1:
            self.selected = 0
            self.move_left()
        if self.x - 100 <= event.pos[0] <= self.x and self.y + 100 <= event.pos[1] <= self.y + 200 and self.selected == 1:
            self.selected = 0
            self.move_down_left()

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

def display_pawns():
    screen.blit(pawn1.pawn, (pawn1.x, pawn1.y))
    screen.blit(pawn2.pawn, (pawn2.x, pawn2.y))

"""
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
        x -= 100
        y -= 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_up_right():
    global x,y
    if x < 905 and y > 5:
        x += 100
        y -= 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_down_left():
    global x,y
    if x > 5 and y < 905:
        x -= 100
        y += 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def move_down_right():
    global x,y
    if x < 905 and y < 905:
        x += 100
        y += 100
        screen.fill((0, 0, 0))
        display_grid()
        screen.blit(pawn, (x, y))

def select_pawn():
    global x,y,selected
    if x <= event.pos[0] <= x + 100 and y <= event.pos[1] <= y + 100:
        pygame.draw.rect(screen, (255, 0, 100), (x, y, 100, 100), 5)
        selected = 1

def move_pawn():
    global x,y,selected
    if x <= event.pos[0] <= x + 100 and y+100 <= event.pos[1] <= y+200 and selected == 1:
        selected = 0
        move_down()
    if x +100 <= event.pos[0] <= x + 200 and y+100 <= event.pos[1] <= y+200 and selected == 1:
        selected = 0
        move_down_right()
    if x +100 <= event.pos[0] <= x + 200 and y <= event.pos[1] <= y+100 and selected == 1:
        selected = 0
        move_right()
    if x +100 <= event.pos[0] <= x + 200 and y - 100 <= event.pos[1] <= y and selected == 1:
        selected = 0
        move_up_right()
    if x <= event.pos[0] <= x + 100 and y - 100 <= event.pos[1] <= y and selected == 1:
        selected = 0
        move_up()
    if x - 100 <= event.pos[0] <= x and y - 100 <= event.pos[1] <= y and selected == 1:
        selected = 0
        move_up_left()
    if x - 100 <= event.pos[0] <= x and y <= event.pos[1] <= y + 100 and selected == 1:
        selected = 0
        move_left()
    if x - 100 <= event.pos[0] <= x and y+100 <= event.pos[1] <= y+200 and selected == 1:
        selected = 0
        move_down_left()
"""

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

pawn1 = Pawn(5,5)
pawn2 = Pawn(105,5)

#création de la grille
display_grid()

display_pawns()

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            """
            if event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_q:
                move_up_left()
            elif event.key == pygame.K_e:
                move_up_right()
            elif event.key == pygame.K_a:
                move_down_left()
            elif event.key == pygame.K_d:
                move_down_right()
            elif event.key == pygame.K_ESCAPE:
                running = False
            """
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pawn1.select_pawn()
            pawn1.move_pawn()
            pawn2.select_pawn()
            pawn2.move_pawn()
    pygame.display.update()

pygame.quit()