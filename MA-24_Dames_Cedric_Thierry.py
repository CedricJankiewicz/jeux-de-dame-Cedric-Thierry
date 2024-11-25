"""
Program name : Jeu de Dames
Author : Cédric Jankiewicz et Thierry Perroud
Date : 18.11.2024
"""

import pygame

class Pawn:
    x = 0
    y = 0
    color = ""
    selected = 0
    pawn = None

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if self.color == "black":
            self.pawn = pygame.image.load(".resources\\MA-24_pion_black.png")
        elif self.color == "white":
            self.pawn = pygame.image.load(".resources\\MA-24_pion_white.png")
        self.pawn = pygame.transform.scale(self.pawn, (100, 100))

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
        if self.x - 100 <= event.pos[0] <= self.x and self.y - 100 <= event.pos[1] <= self.y and self.selected == 1:
            if self.color == "black":
                return
            self.selected = 0
            self.move_up_left()
        if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y - 100 <= event.pos[1] <= self.y and self.selected == 1:
            if self.color == "black":
                return
            self.selected = 0
            self.move_up_right()
        if self.x - 100 <= event.pos[0] <= self.x and self.y + 100 <= event.pos[1] <= self.y + 200 and self.selected == 1:
            if self.color == "white":
                return
            self.selected = 0
            self.move_down_left()
        if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y + 100 <= event.pos[1] <= self.y + 200 and self.selected == 1:
            if self.color == "white":
                return
            self.selected = 0
            self.move_down_right()

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
    for i in range (0, 20):
        screen.blit(black_pawn[i].pawn, (black_pawn[i].x, black_pawn[i].y))

    for i in range (0, 20):
        screen.blit(white_pawn[i].pawn, (white_pawn[i].x, white_pawn[i].y))

def unselect_all():
    for i in range (0, 20):
        black_pawn[i].selected = 0

    for i in range (0, 20):
        white_pawn[i].selected = 0

def draw_board():
    screen.fill((0, 0, 0))
    display_grid()
    display_pawns()

def init_black_pawns(x, y, low_range, high_range):
    for i in range(low_range, high_range):
        black_pawn[i] = Pawn(x, y, "black")
        x += 200

def init_white_pawns(x, y, low_range, high_range):

    for i in range(low_range, high_range):
        white_pawn[i] = Pawn(x, y, "white")
        x += 200

def init_pawns():

    init_black_pawns(105, 5, 0, 5)
    init_black_pawns(5, 105, 5, 10)
    init_black_pawns(105, 205, 10, 15)
    init_black_pawns(5, 305, 15, 20)

    init_white_pawns(105, 605, 0, 5)
    init_white_pawns(5, 705, 5, 10)
    init_white_pawns(105, 805, 10, 15)
    init_white_pawns(5, 905, 15, 20)

def select_pawns():
    for i in range (0, 20):
        black_pawn[i].select_pawn()

    for i in range (0, 20):
        white_pawn[i].select_pawn()

def move_pawns():
    for i in range (0, 20):
        black_pawn[i].move_pawn()

    for i in range (0, 20):
        white_pawn[i].move_pawn()

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

black_pawn = [Pawn] * 20
white_pawn = [Pawn] * 20

init_pawns()

#création de la grille
draw_board()

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            select_pawns()
            move_pawns()
    pygame.display.update()

pygame.quit()