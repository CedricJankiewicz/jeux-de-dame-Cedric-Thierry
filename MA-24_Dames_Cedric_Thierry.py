"""
Program name : Jeu de Dames
Author : Cédric Jankiewicz et Thierry Perroud
Date : 18.11.2024
"""

import pygame

class Pawn:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.selected = 0
        if self.color == "black":
            self.pawn = pygame.image.load(".resources\\MA-24_pion.png")
        elif self.color == "white":
            self.pawn = pygame.image.load(".resources\\MA-24_pion.png")
        self.pawn = pygame.transform.scale(self.pawn, (100, 100))

    def move_right(self):
        if self.x < 905:
            self.x += 100
            draw_board()

    def move_left(self):
        if self.x > 5:
            self.x -= 100
            draw_board()

    def move_up(self):
        if self.y > 5:
            self.y -= 100
            draw_board()

    def move_down(self):
        if self.y < 905:
            self.y += 100
            draw_board()

    def move_up_left(self):
        if self.x > 5 and self.y > 5:
            self.x -= 100
            self.y -= 100
            draw_board()

    def move_up_right(self):
        if self.x < 905 and self.y > 5:
            self.x += 100
            self.y -= 100
            draw_board()

    def move_down_left(self):
        if self.x > 5 and self.y < 905:
            self.x -= 100
            self.y += 100
            draw_board()

    def move_down_right(self):
        if self.x < 905 and self.y < 905:
            self.x += 100
            self.y += 100
            draw_board()

    def select_pawn(self):
        if self.x <= event.pos[0] <= self.x + 100 and self.y <= event.pos[1] <= self.y + 100:
            if self.selected == 0:
                draw_board()
                pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)
                unselect_all()
                self.selected = 1
            else:
                draw_board()
                self.selected = 0

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

def unselect_all():
    pawn1.selected = 0
    pawn2.selected = 0

def draw_board():
    screen.fill((0, 0, 0))
    display_grid()
    display_pawns()

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

pawn1 = Pawn(5,5, "black")
pawn2 = Pawn(105,5, "black")

#création de la grille
draw_board()

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pawn1.select_pawn()
            pawn1.move_pawn()
            pawn2.select_pawn()
            pawn2.move_pawn()
    pygame.display.update()

pygame.quit()