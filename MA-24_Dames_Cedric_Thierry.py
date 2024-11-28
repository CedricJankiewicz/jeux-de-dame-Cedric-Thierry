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
    captured = 0

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
            if self.captured == 1:
                return

            if self.selected == 0:
                draw_board()
                pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)
                unselect_all()
                self.selected = 1
            else:
                draw_board()
                self.selected = 0

    def move_pawn(self):
        global turn
        if self.selected:
            if self.x - 100 <= event.pos[0] <= self.x and self.y - 100 <= event.pos[1] <= self.y:
                can_capture = check_if_pawn_can_capture_directly(self, "up_left")
                can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "up_left")
                has_captured = 0

                if self.color == "black":
                    if not can_capture:
                        return

                    elif can_capture:
                        for i in range (20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                white_pawn[i].captured = 1
                                self.selected = 0
                                self.move_up_left()
                                self.move_up_left()
                                turn += 1
                        return

                elif self.color == "white":
                    if can_capture:
                        for i in range(20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                has_captured = 1
                                black_pawn[i].captured = 1
                                self.selected = 0
                                self.move_up_left()
                                self.move_up_left()
                                turn += 1

                            if has_captured == 1:
                                return

                    elif not can_capture:
                        if can_capture_elsewhere:
                            return

                        for i in range(20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                return

                self.selected = 0
                self.move_up_left()
                turn += 1

            if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y - 100 <= event.pos[1] <= self.y:
                can_capture = check_if_pawn_can_capture_directly(self, "up_right")
                can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "up_right")
                has_captured = 0

                if self.color == "black":
                    if not can_capture:
                        return

                    elif can_capture:
                        for i in range (20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                white_pawn[i].captured = 1
                                self.selected = 0
                                self.move_up_right()
                                self.move_up_right()
                                turn += 1
                        return

                elif self.color == "white":
                    if can_capture:
                        for i in range(20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                has_captured = 1
                                black_pawn[i].captured = 1
                                self.selected = 0
                                self.move_up_right()
                                self.move_up_right()
                                turn += 1

                            if has_captured == 1:
                                return

                    elif not can_capture:
                        if can_capture_elsewhere:
                            return

                        for i in range(20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                return

                self.selected = 0
                self.move_up_right()
                turn += 1

            if self.x - 100 <= event.pos[0] <= self.x and self.y + 100 <= event.pos[1] <= self.y + 200:
                can_capture = check_if_pawn_can_capture_directly(self, "down_left")
                can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "down_left")
                has_captured = 0

                if self.color == "white":
                    if not can_capture:
                        return

                    elif can_capture:
                        for i in range (20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                black_pawn[i].captured = 1
                                self.selected = 0
                                self.move_down_left()
                                self.move_down_left()
                                turn += 1
                        return

                elif self.color == "black":
                    if can_capture:
                        for i in range(20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                has_captured = 1
                                white_pawn[i].captured = 1
                                self.selected = 0
                                self.move_down_left()
                                self.move_down_left()
                                turn += 1

                            if has_captured == 1:
                                return

                    elif not can_capture:
                        if can_capture_elsewhere:
                            return

                        for i in range(20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                return

                self.selected = 0
                self.move_down_left()
                turn += 1

            if self.x + 100 <= event.pos[0] <= self.x + 200 and self.y + 100 <= event.pos[1] <= self.y + 200:
                can_capture = check_if_pawn_can_capture_directly(self, "down_right")
                can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "down_right")
                has_captured = 0

                if self.color == "white":
                    if not can_capture:
                        return

                    elif can_capture:
                        for i in range (20):
                            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                black_pawn[i].captured == 0):

                                black_pawn[i].captured = 1
                                self.selected = 0
                                self.move_down_right()
                                self.move_down_right()
                                turn += 1
                        return

                elif self.color == "black":
                    if can_capture:
                        for i in range(20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                has_captured = 1
                                white_pawn[i].captured = 1
                                self.selected = 0
                                self.move_down_right()
                                self.move_down_right()
                                turn += 1

                            if has_captured == 1:
                                return

                    elif not can_capture:
                        if can_capture_elsewhere:
                            return

                        for i in range(20):
                            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                white_pawn[i].captured == 0):

                                return

                self.selected = 0
                self.move_down_right()
                turn += 1

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
    for i in range (20):
        if black_pawn[i].captured == 0:
            screen.blit(black_pawn[i].pawn, (black_pawn[i].x, black_pawn[i].y))

    for i in range (20):
        if white_pawn[i].captured == 0:
            screen.blit(white_pawn[i].pawn, (white_pawn[i].x, white_pawn[i].y))

def unselect_all():
    for i in range (20):
        black_pawn[i].selected = 0

    for i in range (20):
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
    if turn % 2 == 0:
        for i in range (20):
            black_pawn[i].select_pawn()
    if turn % 2 == 1:
        for i in range (20):
            white_pawn[i].select_pawn()

def move_pawns():
    for i in range (20):
        black_pawn[i].move_pawn()

    for i in range (20):
        white_pawn[i].move_pawn()

def check_if_pawn_can_capture_directly(pawn, attempted_move):
    can_capture = False

    for i in range(20):
        if pawn.color == "black":
            if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                if attempted_move == "up_left":
                    can_capture = check_if_pawn_can_capture(-100, -100)
                    break
                elif attempted_move == "up_right":
                    can_capture = check_if_pawn_can_capture(100, -100)
                    break
                elif attempted_move == "down_left":
                    can_capture = check_if_pawn_can_capture(-100, 100)
                    break
                elif attempted_move == "down_right":
                    can_capture = check_if_pawn_can_capture(100, 100)
                    break

        elif pawn.color == "white":
            if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                if attempted_move == "up_left":
                    can_capture = check_if_pawn_can_capture(-100, -100)
                    break
                elif attempted_move == "up_right":
                    can_capture = check_if_pawn_can_capture(100, -100)
                    break
                elif attempted_move == "down_left":
                    can_capture = check_if_pawn_can_capture(-100, 100)
                    break
                elif attempted_move == "down_right":
                    can_capture = check_if_pawn_can_capture(100, 100)
                    break

    return can_capture

def check_if_pawn_can_capture_elsewhere(pawn, attempted_move):
    can_capture = False

    if attempted_move == "up_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -100)
                    break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300)
                    break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 300)
                    break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -100)
                    break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300)
                    break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 300)
                    break

    if not can_capture and attempted_move == "up_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100)
                    break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300)
                    break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, 300)
                    break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100)
                    break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300)
                    break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, 300)
                    break

    if not can_capture and attempted_move == "down_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300)
                    break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -300)
                    break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 100)
                    break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300)
                    break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -300)
                    break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 100)
                    break

    if not can_capture and attempted_move == "down_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300)
                    break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, -300)
                    break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100)
                    break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300)
                    break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, -300)
                    break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100)
                    break

    return can_capture

def check_if_pawn_can_capture(pos_x, pos_y):
    blocked = 0

    for i in range(20):
        if (not (5 <= event.pos[0] + pos_x <= 1005) or not (5 <= event.pos[1] + pos_y <= 1005) or
            black_pawn[i].x <= event.pos[0] + pos_x <= black_pawn[i].x + 100 and
            black_pawn[i].y <= event.pos[1] + pos_y <= black_pawn[i].y + 100 and black_pawn[i].captured == 0 or
            white_pawn[i].x <= event.pos[0] + pos_x <= white_pawn[i].x + 100 and
            white_pawn[i].y <= event.pos[1] + pos_y <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

            blocked += 1
            break

    if blocked == 0:
        return True
    else:
        return False

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1010,1010))

black_pawn = [Pawn] * 20
white_pawn = [Pawn] * 20

turn = 1

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