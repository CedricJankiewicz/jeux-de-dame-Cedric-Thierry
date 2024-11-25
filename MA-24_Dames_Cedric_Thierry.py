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
            self.pawn = pygame.image.load(".resources\\MA-24_pion_black.png")
        elif self.color == "white":
            self.pawn = pygame.image.load(".resources\\MA-24_pion_white.png")
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
    for i in range (1, 41):
        screen.blit(black_pawn[i].pawn, (black_pawn[i].x, black_pawn[i].y))

    for i in range (1, 41):
        screen.blit(white_pawn[i].pawn, (white_pawn[i].x, white_pawn[i].y))

    """
    screen.blit(black_pawn1.pawn, (black_pawn1.x, black_pawn1.y))
    screen.blit(black_pawn2.pawn, (black_pawn2.x, black_pawn2.y))
    screen.blit(black_pawn3.pawn, (black_pawn3.x, black_pawn3.y))
    screen.blit(black_pawn4.pawn, (black_pawn4.x, black_pawn4.y))
    screen.blit(black_pawn5.pawn, (black_pawn5.x, black_pawn5.y))
    screen.blit(black_pawn6.pawn, (black_pawn6.x, black_pawn6.y))
    screen.blit(black_pawn7.pawn, (black_pawn7.x, black_pawn7.y))
    screen.blit(black_pawn8.pawn, (black_pawn8.x, black_pawn8.y))
    screen.blit(black_pawn9.pawn, (black_pawn9.x, black_pawn9.y))
    screen.blit(black_pawn10.pawn, (black_pawn10.x, black_pawn10.y))

    screen.blit(black_pawn11.pawn, (black_pawn11.x, black_pawn11.y))
    screen.blit(black_pawn12.pawn, (black_pawn12.x, black_pawn12.y))
    screen.blit(black_pawn13.pawn, (black_pawn13.x, black_pawn13.y))
    screen.blit(black_pawn14.pawn, (black_pawn14.x, black_pawn14.y))
    screen.blit(black_pawn15.pawn, (black_pawn15.x, black_pawn15.y))
    screen.blit(black_pawn16.pawn, (black_pawn16.x, black_pawn16.y))
    screen.blit(black_pawn17.pawn, (black_pawn17.x, black_pawn17.y))
    screen.blit(black_pawn18.pawn, (black_pawn18.x, black_pawn18.y))
    screen.blit(black_pawn19.pawn, (black_pawn19.x, black_pawn19.y))
    screen.blit(black_pawn20.pawn, (black_pawn20.x, black_pawn20.y))

    screen.blit(black_pawn21.pawn, (black_pawn21.x, black_pawn21.y))
    screen.blit(black_pawn22.pawn, (black_pawn22.x, black_pawn22.y))
    screen.blit(black_pawn23.pawn, (black_pawn23.x, black_pawn23.y))
    screen.blit(black_pawn24.pawn, (black_pawn24.x, black_pawn24.y))
    screen.blit(black_pawn25.pawn, (black_pawn25.x, black_pawn25.y))
    screen.blit(black_pawn26.pawn, (black_pawn26.x, black_pawn26.y))
    screen.blit(black_pawn27.pawn, (black_pawn27.x, black_pawn27.y))
    screen.blit(black_pawn28.pawn, (black_pawn28.x, black_pawn28.y))
    screen.blit(black_pawn29.pawn, (black_pawn29.x, black_pawn29.y))
    screen.blit(black_pawn30.pawn, (black_pawn30.x, black_pawn30.y))

    screen.blit(black_pawn31.pawn, (black_pawn31.x, black_pawn31.y))
    screen.blit(black_pawn32.pawn, (black_pawn32.x, black_pawn32.y))
    screen.blit(black_pawn33.pawn, (black_pawn33.x, black_pawn33.y))
    screen.blit(black_pawn34.pawn, (black_pawn34.x, black_pawn34.y))
    screen.blit(black_pawn35.pawn, (black_pawn35.x, black_pawn35.y))
    screen.blit(black_pawn36.pawn, (black_pawn36.x, black_pawn36.y))
    screen.blit(black_pawn37.pawn, (black_pawn37.x, black_pawn37.y))
    screen.blit(black_pawn38.pawn, (black_pawn38.x, black_pawn38.y))
    screen.blit(black_pawn39.pawn, (black_pawn39.x, black_pawn39.y))
    screen.blit(black_pawn40.pawn, (black_pawn40.x, black_pawn40.y))
    """

def unselect_all():
    for i in range (1, 41):
        black_pawn[i].selected = 0

    for i in range (1, 41):
        white_pawn[i].selected = 0

    """
    black_pawn1.selected = 0
    black_pawn2.selected = 0
    black_pawn3.selected = 0
    black_pawn4.selected = 0
    black_pawn5.selected = 0
    black_pawn6.selected = 0
    black_pawn7.selected = 0
    black_pawn8.selected = 0
    black_pawn9.selected = 0
    black_pawn10.selected = 0

    black_pawn11.selected = 0
    black_pawn12.selected = 0
    black_pawn13.selected = 0
    black_pawn14.selected = 0
    black_pawn15.selected = 0
    black_pawn16.selected = 0
    black_pawn17.selected = 0
    black_pawn18.selected = 0
    black_pawn19.selected = 0
    black_pawn20.selected = 0

    black_pawn21.selected = 0
    black_pawn22.selected = 0
    black_pawn23.selected = 0
    black_pawn24.selected = 0
    black_pawn25.selected = 0
    black_pawn26.selected = 0
    black_pawn27.selected = 0
    black_pawn28.selected = 0
    black_pawn29.selected = 0
    black_pawn30.selected = 0

    black_pawn31.selected = 0
    black_pawn32.selected = 0
    black_pawn33.selected = 0
    black_pawn34.selected = 0
    black_pawn35.selected = 0
    black_pawn36.selected = 0
    black_pawn37.selected = 0
    black_pawn38.selected = 0
    black_pawn39.selected = 0
    black_pawn40.selected = 0
    """

def draw_board():
    screen.fill((0, 0, 0))
    display_grid()
    display_pawns()

def init_black_pawns(x, y, low_range, high_range):
    for i in range(low_range, high_range):
        black_pawn[i] = Pawn(x, y, "black")
        x += 100

    return black_pawn

def init_white_pawns(x, y, low_range, high_range):

    for i in range(low_range, high_range):
        white_pawn[i] = Pawn(x, y, "white")
        x += 100

def init_pawns():

    init_black_pawns(5, 5, 0, 10)
    init_black_pawns(5, 105, 10, 20)
    init_black_pawns(5, 205, 20, 30)
    init_black_pawns(5, 305, 30, 40)

    init_white_pawns(5, 605, 0, 10)
    init_white_pawns(5, 705, 10, 20)
    init_white_pawns(5, 805, 20, 30)
    init_white_pawns(5, 905, 30, 40)

def select_pawns():
    for i in range (1, 41):
        black_pawn[i].select_pawn()

    for i in range (1, 41):
        white_pawn[i].select_pawn()
    """
    black_pawn1.select_pawn()
    black_pawn2.select_pawn()
    black_pawn3.select_pawn()
    black_pawn4.select_pawn()
    black_pawn5.select_pawn()
    black_pawn6.select_pawn()
    black_pawn7.select_pawn()
    black_pawn8.select_pawn()
    black_pawn9.select_pawn()
    black_pawn10.select_pawn()

    black_pawn11.select_pawn()
    black_pawn12.select_pawn()
    black_pawn13.select_pawn()
    black_pawn14.select_pawn()
    black_pawn15.select_pawn()
    black_pawn16.select_pawn()
    black_pawn17.select_pawn()
    black_pawn18.select_pawn()
    black_pawn19.select_pawn()
    black_pawn20.select_pawn()

    black_pawn21.select_pawn()
    black_pawn22.select_pawn()
    black_pawn23.select_pawn()
    black_pawn24.select_pawn()
    black_pawn25.select_pawn()
    black_pawn26.select_pawn()
    black_pawn27.select_pawn()
    black_pawn28.select_pawn()
    black_pawn29.select_pawn()
    black_pawn30.select_pawn()

    black_pawn31.select_pawn()
    black_pawn32.select_pawn()
    black_pawn33.select_pawn()
    black_pawn34.select_pawn()
    black_pawn35.select_pawn()
    black_pawn36.select_pawn()
    black_pawn37.select_pawn()
    black_pawn38.select_pawn()
    black_pawn39.select_pawn()
    black_pawn40.select_pawn()
    """

def move_pawns():
    for i in range (1, 41):
        black_pawn[i].move_pawn()

    for i in range (1, 41):
        white_pawn[i].move_pawn()
    """
    black_pawn1.move_pawn()
    black_pawn2.move_pawn()
    black_pawn3.move_pawn()
    black_pawn4.move_pawn()
    black_pawn5.move_pawn()
    black_pawn6.move_pawn()
    black_pawn7.move_pawn()
    black_pawn8.move_pawn()
    black_pawn9.move_pawn()
    black_pawn10.move_pawn()

    black_pawn11.move_pawn()
    black_pawn12.move_pawn()
    black_pawn13.move_pawn()
    black_pawn14.move_pawn()
    black_pawn15.move_pawn()
    black_pawn16.move_pawn()
    black_pawn17.move_pawn()
    black_pawn18.move_pawn()
    black_pawn19.move_pawn()
    black_pawn20.move_pawn()

    black_pawn21.move_pawn()
    black_pawn22.move_pawn()
    black_pawn23.move_pawn()
    black_pawn24.move_pawn()
    black_pawn25.move_pawn()
    black_pawn26.move_pawn()
    black_pawn27.move_pawn()
    black_pawn28.move_pawn()
    black_pawn29.move_pawn()
    black_pawn30.move_pawn()

    black_pawn31.move_pawn()
    black_pawn32.move_pawn()
    black_pawn33.move_pawn()
    black_pawn34.move_pawn()
    black_pawn35.move_pawn()
    black_pawn36.move_pawn()
    black_pawn37.move_pawn()
    black_pawn38.move_pawn()
    black_pawn39.move_pawn()
    black_pawn40.move_pawn()
    """

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

black_pawn = 40 * []
white_pawn = 40 * []

init_pawns()

"""
#première ligne de pions noirs
black_pawn1 = Pawn(5,5, "black")
black_pawn2 = Pawn(105,5, "black")
black_pawn3 = Pawn(205,5, "black")
black_pawn4 = Pawn(305,5, "black")
black_pawn5 = Pawn(405,5, "black")
black_pawn6 = Pawn(505,5, "black")
black_pawn7 = Pawn(605,5, "black")
black_pawn8 = Pawn(705,5, "black")
black_pawn9 = Pawn(805,5, "black")
black_pawn10 = Pawn(905,5, "black")

#deuxième ligne de pions noirs
black_pawn11 = Pawn(5,105, "black")
black_pawn12 = Pawn(105,105, "black")
black_pawn13 = Pawn(205,105, "black")
black_pawn14 = Pawn(305,105, "black")
black_pawn15 = Pawn(405,105, "black")
black_pawn16 = Pawn(505,105, "black")
black_pawn17 = Pawn(605,105, "black")
black_pawn18 = Pawn(705,105, "black")
black_pawn19 = Pawn(805,105, "black")
black_pawn20 = Pawn(905,105, "black")

#troisième ligne de pions noirs
black_pawn21 = Pawn(5,205, "black")
black_pawn22 = Pawn(105,205, "black")
black_pawn23 = Pawn(205,205, "black")
black_pawn24 = Pawn(305,205, "black")
black_pawn25 = Pawn(405,205, "black")
black_pawn26 = Pawn(505,205, "black")
black_pawn27 = Pawn(605,205, "black")
black_pawn28 = Pawn(705,205, "black")
black_pawn29 = Pawn(805,205, "black")
black_pawn30 = Pawn(905,205, "black")

#quatrième ligne de pions noirs
black_pawn31 = Pawn(5,305, "black")
black_pawn32 = Pawn(105,305, "black")
black_pawn33 = Pawn(205,305, "black")
black_pawn34 = Pawn(305,305, "black")
black_pawn35 = Pawn(405,305, "black")
black_pawn36 = Pawn(505,305, "black")
black_pawn37 = Pawn(605,305, "black")
black_pawn38 = Pawn(705,305, "black")
black_pawn39 = Pawn(805,305, "black")
black_pawn40 = Pawn(905,305, "black")
"""

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