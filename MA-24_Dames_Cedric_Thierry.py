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
    queen = 0

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        if self.color == "black":
            self.pawn = pygame.image.load(".resources\\MA-24_pion_black.png")
        elif self.color == "white":
            self.pawn = pygame.image.load(".resources\\MA-24_pion_white.png")
        self.pawn = pygame.transform.scale(self.pawn, (100, 100))

    def change_to_queen(self):
        if self.color == "black":
            if 895 <= self.y <= 905:
                self.queen = 1
                self.pawn = pygame.image.load(".resources\\MA-24_pion_black_queen.png")
        if self.color == "white":
            if 0 <= self.y <= 10:
                self.queen = 1
                self.pawn = pygame.image.load(".resources\\MA-24_pion_white_queen.png")
        self.pawn = pygame.transform.scale(self.pawn, (100, 100))

    def move_up_left(self):
        if self.x > 5 and self.y > 5:
            self.x -= 100
            self.y -= 100
            change_to_queen()
            draw_board()

    def move_up_right(self):
        if self.x < 905 and self.y > 5:
            self.x += 100
            self.y -= 100
            change_to_queen()
            draw_board()

    def move_down_left(self):
        if self.x > 5 and self.y < 905:
            self.x -= 100
            self.y += 100
            change_to_queen()
            draw_board()

    def move_down_right(self):
        if self.x < 905 and self.y < 905:
            self.x += 100
            self.y += 100
            change_to_queen()
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

        has_captured = 0

        if self.selected:
            if self.queen == 0:
                if self.x - 100 <= event.pos[0] <= self.x and self.y - 100 <= event.pos[1] <= self.y:
                    can_capture = check_if_pawn_can_capture_directly(self, "up_left")
                    can_capture_elsewhere = check_if_pawn_can_capture_elsewhere(self, "up_left")

                    if self.color == "black":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    white_pawn[i].captured = 1
                                    self.move_up_left()
                                    self.move_up_left()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_left")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

                            return

                    elif self.color == "white":
                        if can_capture:
                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):

                                    black_pawn[i].captured = 1
                                    self.move_up_left()
                                    self.move_up_left()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_left")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

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

                    if self.color == "black":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    white_pawn[i].captured = 1
                                    self.move_up_right()
                                    self.move_up_right()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_right")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

                            return

                    elif self.color == "white":
                        if can_capture:
                            for i in range(20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):

                                    black_pawn[i].captured = 1
                                    self.move_up_right()
                                    self.move_up_right()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "up_right")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

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

                    if self.color == "white":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):

                                    black_pawn[i].captured = 1
                                    self.move_down_left()
                                    self.move_down_left()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_left")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

                            return

                    elif self.color == "black":
                        if can_capture:
                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    white_pawn[i].captured = 1
                                    self.move_down_left()
                                    self.move_down_left()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_left")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

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

                    if self.color == "white":
                        if not can_capture:
                            return

                        elif can_capture:
                            for i in range (20):
                                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and
                                    black_pawn[i].captured == 0):

                                    black_pawn[i].captured = 1
                                    self.move_down_right()
                                    self.move_down_right()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_right")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

                            return

                    elif self.color == "black":
                        if can_capture:
                            for i in range(20):
                                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and
                                    white_pawn[i].captured == 0):

                                    white_pawn[i].captured = 1
                                    self.move_down_right()
                                    self.move_down_right()
                                    has_captured = 1
                                    break

                            if has_captured == 1:
                                can_capture_again = check_if_pawn_can_capture_again(self, "down_right")

                                if can_capture_again:
                                    pygame.draw.rect(screen, (255, 0, 100), (self.x, self.y, 100, 100), 5)

                                elif not can_capture_again:
                                    self.selected = 0
                                    turn += 1

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

            if self.queen == 1:
                pos_x = self.x
                pos_y = self.y
                loops = 0

                if event.pos[0] <= self.x and event.pos[1] <= self.y:
                    while 0 <= pos_x - 100 and 0 <= pos_y - 100:
                        pos_x -= 100
                        pos_y -= 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:

                            if self.color == "black":
                                pass

                            if self.color == "white":
                                pass

                            self.selected = 0

                            for i in range(loops):
                                self.move_up_left()

                            turn += 1
                            break

                        if pawn_hit:
                            break

                if self.x + 100 <= event.pos[0] and event.pos[1] <= self.y:
                    while pos_x + 100 <= 1000 and 0 <= pos_y - 100:
                        pos_x += 100
                        pos_y -= 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.color == "black":
                                pass

                            if self.color == "white":
                                pass

                            self.selected = 0

                            for i in range(loops):
                                self.move_up_right()

                            turn += 1
                            break

                        if pawn_hit:
                            break

                if event.pos[0] <= self.x and self.y + 100 <= event.pos[1]:
                    while 0 <= pos_x - 100 and pos_y + 100 <= 1000:
                        pos_x -= 100
                        pos_y += 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.color == "black":
                                pass

                            if self.color == "white":
                                pass

                            self.selected = 0

                            for i in range(loops):
                                self.move_down_left()

                            turn += 1
                            break

                        if pawn_hit:
                            break

                if self.x + 100 <= event.pos[0] and self.y + 100 <= event.pos[1]:
                    while pos_x + 100 <= 1000 and pos_y + 100 <= 1000:
                        pos_x += 100
                        pos_y += 100
                        loops += 1
                        pawn_hit = check_for_pawn_in_the_way(pos_x, pos_y)

                        if pos_x <= event.pos[0] <= pos_x + 100 and pos_y <= event.pos[1] <= pos_y + 100:
                            if self.color == "black":
                                pass

                            if self.color == "white":
                                pass

                            self.selected = 0

                            for i in range(loops):
                                self.move_down_right()

                            turn += 1
                            break

                        if pawn_hit:
                            break

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

def timer():
    global global_mill_sec_time, global_sec_time, global_min_time, global_time,\
        black_mill_sec_time, black_sec_time, black_min_time, black_time,\
        white_mill_sec_time, white_sec_time, white_min_time, white_time,\
        turn

    pygame.time.delay(10)
    if global_mill_sec_time >= 99:
        global_mill_sec_time = 0
        global_sec_time += 1
        if global_sec_time > 59:
            global_sec_time = 0
            global_min_time += 1
    else:
        global_mill_sec_time += 1

    global_time = f"{global_min_time:02d}:{global_sec_time:02d}:{global_mill_sec_time:02d}"

    if turn % 2 == 0:
        if black_mill_sec_time >= 99:
            black_mill_sec_time = 0
            black_sec_time += 1
            if black_sec_time > 59:
                black_sec_time = 0
                black_min_time += 1
        else:
            black_mill_sec_time += 1

    black_time = f"{black_min_time:02d}:{black_sec_time:02d}:{black_mill_sec_time:02d}"

    if turn % 2 == 1:
        if white_mill_sec_time >= 99:
            white_mill_sec_time = 0
            white_sec_time += 1
            if white_sec_time > 59:
                white_sec_time = 0
                white_min_time += 1
        else:
            white_mill_sec_time += 1

    white_time = f"{white_min_time:02d}:{white_sec_time:02d}:{white_mill_sec_time:02d}"

def check_pawn_left_queen():
    global black_pawn_left,white_pawn_left,black_pawn_queen,white_pawn_queen
    black_pawn_left = 20
    white_pawn_left = 20
    for i in range(20):
        if white_pawn[i].captured == 1:
            white_pawn_left -= 1

        if black_pawn[i].captured == 1:
            black_pawn_left -= 1
    black_pawn_queen = 0
    white_pawn_queen = 0
    for i in range(20):
        if white_pawn[i].queen == 1 and not white_pawn[i].captured == 1:
            white_pawn_queen += 1

        if black_pawn[i].queen == 1 and not black_pawn[i].captured == 1:
            black_pawn_queen += 1

def display_info():
    #reset info side
    pygame.draw.rect(screen, (0, 0, 0), (1010, 10, 400, 1000))

    timer()
    check_pawn_left_queen()

    #text font
    font = pygame.font.Font(None, 36)

    #global info
    global_y = 305
    txt_turn = font.render(f"turn {turn}", True, (255, 255, 255))
    screen.blit(txt_turn, (1060, global_y))


    txt_timer = font.render(global_time , True, (255, 255, 255))
    screen.blit(txt_timer, (1060, (global_y + 30)))

    #black info
    blk_y = 55
    txt_black = font.render("black", True, (255, 255, 255))
    screen.blit(txt_black, (1060, blk_y))
    txt_blk_timer = font.render(black_time, True, (255, 255, 255))
    screen.blit(txt_blk_timer, (1060, (blk_y + 50)))
    txt_blk_remain_pawn = font.render(f"{black_pawn_left} pawns left", True, (255, 255, 255))
    screen.blit(txt_blk_remain_pawn, (1060, (blk_y + 80)))
    txt_blk_remain_pawn = font.render(f"{black_pawn_queen} queens", True, (255, 255, 255))
    screen.blit(txt_blk_remain_pawn, (1060, (blk_y + 110)))

    #white info
    wht_y = 505
    txt_white = font.render("white", True, (255, 255, 255))
    screen.blit(txt_white, (1060, wht_y))
    txt_wht_timer = font.render(white_time, True, (255, 255, 255))
    screen.blit(txt_wht_timer, (1060, (wht_y + 50)))
    txt_wht_remain_pawn = font.render(f"{white_pawn_left} pawns left", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 80)))
    txt_wht_remain_pawn = font.render(f"{white_pawn_queen} queens", True, (255, 255, 255))
    screen.blit(txt_wht_remain_pawn, (1060, (wht_y + 110)))

def unselect_all():
    for i in range (20):
        black_pawn[i].selected = 0

    for i in range (20):
        white_pawn[i].selected = 0

def draw_board():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1010, 1010))
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
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 300)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -100)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, 300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 300)
                    if can_capture:
                        break

    if attempted_move == "up_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, 300)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -100)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, 300)
                    if can_capture:
                        break

    if attempted_move == "down_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 100)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-100, -300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, -300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(300, 100)
                    if can_capture:
                        break

    if attempted_move == "down_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, -300)
                    if can_capture:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100)
                    if can_capture:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, -300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(100, -300)
                    if can_capture:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture = check_if_pawn_can_capture(-300, 100)
                    if can_capture:
                        break

    return can_capture

def check_if_pawn_can_capture(pos_x, pos_y):
    for i in range(20):
        if (not (5 <= event.pos[0] + pos_x <= 1005) or not (5 <= event.pos[1] + pos_y <= 1005) or
            black_pawn[i].x <= event.pos[0] + pos_x <= black_pawn[i].x + 100 and
            black_pawn[i].y <= event.pos[1] + pos_y <= black_pawn[i].y + 100 and black_pawn[i].captured == 0 or
            white_pawn[i].x <= event.pos[0] + pos_x <= white_pawn[i].x + 100 and
            white_pawn[i].y <= event.pos[1] + pos_y <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

            return False

    return True

def check_if_pawn_can_capture_again(pawn, previous_move):
    can_capture_again = False

    if previous_move == "up_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(100, -300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 100)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(100, -300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 100)
                    if can_capture_again:
                        break

    elif previous_move == "up_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, -300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] - 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 100)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, -300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] - 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 100)
                    if can_capture_again:
                        break

    elif previous_move == "down_left":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -100)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] - 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(100, 300)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, -100)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] - 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-300, 300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(100, 300)
                    if can_capture_again:
                        break

    elif previous_move == "down_right":
        if pawn.color == "black":
            for i in range(20):
                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -100)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, 300)
                    if can_capture_again:
                        break

                if (white_pawn[i].x <= event.pos[0] + 200 <= white_pawn[i].x + 100 and
                    white_pawn[i].y <= event.pos[1] + 200 <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 300)
                    if can_capture_again:
                        break

        elif pawn.color == "white":
            for i in range(20):
                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, -100)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(-100, 300)
                    if can_capture_again:
                        break

                if (black_pawn[i].x <= event.pos[0] + 200 <= black_pawn[i].x + 100 and
                    black_pawn[i].y <= event.pos[1] + 200 <= black_pawn[i].y + 100 and black_pawn[i].captured == 0):

                    can_capture_again = check_if_pawn_can_capture(300, 300)
                    if can_capture_again:
                        break

    return can_capture_again

def change_to_queen():
    for i in range (20):
        black_pawn[i].change_to_queen()

    for i in range (20):
        white_pawn[i].change_to_queen()

def check_for_pawn_in_the_way(pos_x, pos_y):
    for i in range(20):
        if (black_pawn[i].x <= pos_x <= black_pawn[i].x + 100 and
            black_pawn[i].y <= pos_y <= black_pawn[i].y + 100 and black_pawn[i].captured == 0 or
            white_pawn[i].x <= pos_x <= white_pawn[i].x + 100 and
            white_pawn[i].y <= pos_y <= white_pawn[i].y + 100 and white_pawn[i].captured == 0):

            return True

    return False

def win():
    font = pygame.font.Font(None, 50)
    txt_wht = font.render("white win", True, (255, 255, 255))
    txt_blk = font.render("black win", True, (255, 255, 255))
    if black_pawn_left == 0:
        screen.fill((0, 0, 0))
        screen.blit(txt_wht, (100, 100))
    if white_pawn_left == 0:
        screen.fill((0, 0, 0))
        screen.blit(txt_blk, (100, 100))

#initialisation de la librairie
pygame.init()

#création de la fenêtre
screen = pygame.display.set_mode((1410,1010))

black_pawn = [Pawn] * 20
white_pawn = [Pawn] * 20

turn = 1

black_pawn_left = 20
white_pawn_left = 20

black_pawn_queen = 0
white_pawn_queen = 0

#timer variable
global_mill_sec_time = 0
global_sec_time = 0
global_min_time = 0
global_time = ""

black_mill_sec_time = 0
black_sec_time = 0
black_min_time = 0
black_time = ""

white_mill_sec_time = 0
white_sec_time = 0
white_min_time = 0
white_time = ""

init_pawns()

#création de la grille
draw_board()
running=True

while running:
    display_info()
    win()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            select_pawns()
            move_pawns()
    pygame.display.update()

pygame.quit()